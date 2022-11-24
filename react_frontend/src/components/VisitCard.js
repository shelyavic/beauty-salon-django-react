import * as React from 'react';
import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import jwtInterceptor from './jwtInterceptor';
import moment from 'moment';

// export default function VisitCard(props) {
//     return (
//         <Paper>
//          <Typography variant="h6" component="div">
//            Some Text {props.asdf}
//          </Typography>
//              <div class={{ display: inline-flex}}>
//              <Button size="small">Edit</Button>
//              <Button size="small">Delete</Button>
             
//         </Paper>
//     );
// }
export default function VisitCard(props) {
  const [visit, setVisit] = useState(props.visit);
  useEffect(() => {
    jwtInterceptor
      .get(`http://127.0.0.1:8000/services/${visit.service}`)
      .then((response) => {
        const service = response.data;
        
        setVisit({
          ...visit,
          service_name: service.name,
          duration: service.duration,
        });
      });
  }, []);
  return (
    <Card sx={{ minWidth: 275, display: "flex"}}>
      <CardContent>
        <Typography variant="body1" component="div">
          {moment(visit.date_time).format('D.M.YYYY HH:mm')} {}
        </Typography>
      </CardContent>
      <CardActions sx={{ "marginLeft": "auto", "marginRight": 0}}>
        <Button size="small">Edit</Button>
        <Button size="small">Delete</Button>
      </CardActions>
    </Card>
  );
}
