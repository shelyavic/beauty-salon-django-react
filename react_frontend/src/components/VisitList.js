import * as React from 'react';
//import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
//import { styled } from '@mui/material/styles';
import VisitCard from './VisitCard';
import { useState, useEffect } from 'react';
import jwtInterceptor from './jwtInterceptor';
//import moment from 'moment';
// const Item = styled(Paper)(({ theme }) => ({
//   backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
//   ...theme.typography.body2,
//   padding: theme.spacing(1),
//   textAlign: 'center',
//   color: theme.palette.text.secondary,
// }));

export default function VisitList(props) {
  const [visits, setVisits] = useState([]);
  useEffect(() => {
    jwtInterceptor
      .get("http://127.0.0.1:8000/visits/")
      .then((response) => {
        setVisits(response.data);
      });
  }, []);
  return (
    <React.Fragment>
      <Stack spacing={2}>
        { 
          visits.map((visit, index) => {
            return (<VisitCard key={index} visit={visit}/>);
          })
        }
      </Stack>
    </React.Fragment>
  );
}