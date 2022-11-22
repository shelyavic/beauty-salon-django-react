import * as React from 'react';
import { useContext } from "react";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
import {Link as MUILink} from '@mui/material';
import AuthContext from "./AuthContext"

function LoginControl(props){  
  let buttons;
    if (props.user){
        buttons = (
            <React.Fragment>
                <Button color="inherit" component={Link} to={"/myvisits"}>My visits</Button>
                <Button color="inherit" component={Link} to={"/logout"}> Logout</Button>
            </React.Fragment>
        )
    } else buttons = <Button color="inherit" component={Link} to={"/login"} >Login</Button>;
    return buttons;
}

export default function ButtonAppBar(props) {
  const { user } = useContext(AuthContext);
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <MUILink 
            variant='h6'
            color = '#fff'
            underline='none'
            component={Link} 
            to={"/"} 
            sx={{ flexGrow: 1 }}>
            Beauty Salon
          </MUILink>
          <LoginControl user={user} />
        </Toolbar>
      </AppBar>
    </Box>
  );
}