import * as React from 'react';
import { useContext } from "react";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
import { Link as MUILink } from '@mui/material';
import AuthContext from "./AuthContext"

function LoginControl(props) {
  const { user, logout } = useContext(AuthContext);
  let buttons;
  if (user) {
    buttons = (
      <React.Fragment>
        <Button color="inherit" component={Link} to={"/myvisits"}>My visits</Button>
        <Button color="inherit" onClick={() => logout()}> Logout</Button>
      </React.Fragment>
    );
  } else buttons = <Button color="inherit" component={Link} to={"/login"} >Login</Button>;
  return buttons;
}

export default function ButtonAppBar(props) {

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <MUILink
            variant='h6'
            color='#fff'
            underline='none'
            component={Link}
            to={"/"}
            sx={{ flexGrow: 1 }}>
            Beauty Salon
          </MUILink>
          <LoginControl />
        </Toolbar>
      </AppBar>
    </Box>
  );
}