// App.js
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Login from './Login';
import Dashboard from './db'; 
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Route exact path="/" component={Login} />
        {/* <Route exact path="/ok" component={Dashboard} />
        <Route exact path="/db" component={Dashboard} /> */}
      </div>
    </Router>
  );
}

export default App;


