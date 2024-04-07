import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Login from './Login';
import App from './App'
import Transactions from './db'
import Accounts from './ok'
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <Accounts />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
