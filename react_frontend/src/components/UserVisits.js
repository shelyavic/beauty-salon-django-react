import * as React from 'react';
//import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
//import { styled } from '@mui/material/styles';
import VisitCard from './VisitCard';
import { useState, useEffect, useContext } from 'react';
import jwtInterceptor from './jwtInterceptor';
import AuthContext from "./AuthContext";

export default function UserVisits(props) {
  const [visits, setVisits] = useState([]);
  const { user } = useContext(AuthContext);
  useEffect(() => {
    jwtInterceptor
      .get(`http://127.0.0.1:8000/users/${user.user_id}/visits/`)
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