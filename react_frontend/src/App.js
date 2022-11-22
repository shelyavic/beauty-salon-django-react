import './App.css';
import React from 'react';
import Container from '@mui/material/Container';

import { Route, Routes } from "react-router-dom";

import Header from './components/Header'
import VisitList from './components/VisitList';
import Login from './components/Login';
import { AuthContextProvider } from './components/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import UserVisits from './components/UserVisits';

function App() {
  return (
    <React.Fragment>
      <AuthContextProvider>
        <Header />
        <Container sx={{ paddingTop: '16px' }}>
          <Routes>
            <Route path="/" element={<VisitList />} />
            <Route path="/login" element={<Login />} />
            <Route path="/myvisits" element={
              <ProtectedRoute>
                <UserVisits/>
              </ProtectedRoute>
            }/>
          </Routes>
        </Container>
      </AuthContextProvider>
    </React.Fragment>
  );
}

export default App;
