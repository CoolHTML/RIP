import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';
import {BrowserRouter} from "react-router-dom"


ReactDOM.render(
<React.StrictMode>
<BrowserRouter>
	<App />
	</BrowserRouter>
</React.StrictMode>,
document.getElementById('root')
);
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function() {
    navigator.serviceWorker
      .register("/serviceWorker.js")
      .then(res => console.log("service worker registered"))
      .catch(err => console.log("service worker not registered", err))
  })
}
