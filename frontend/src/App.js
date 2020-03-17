import React from 'react';
import logo from './logo.svg';
// import './App.css';
import { Router } from '@reach/router';
import 'bootstrap/dist/css/bootstrap.min.css';
import Main from './views/Main';
import Login from './views/Login';

function App() {
  return (
    <Router>
      <Main path='/' />
      <Login path='/' />
    </Router>
  );
}

export default App;
