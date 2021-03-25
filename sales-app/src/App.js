/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
**/

import React from "react";
import "./styles.scss";

function App() {
  return (
    <Homepage
      text=""
      title="SALES TRACKER"
      text1="browse sales catalogs from your favorite sites"
      nike="NIKE"
      hM="H&M"
      uniqlo="UNIQLO"
      forever21="FOREVER21"
    />
  );
}

export default App;


function Homepage(props) {
  const { text, title, text1, nike, hM, uniqlo, forever21 } = props;

  return (
    <div className="homepage">
      <div className="overlap-group">
        <div className="text roboto-regular-normal-black-12px">{text}</div>
        <h1 className="title robotocondensed-regular-normal-black-72px">{title}</h1>
      </div>
      <div className="text-1 nanumgothic-regular-normal-black-24px">{text1}</div>
      <div className="shop-selection">
        <div className="nike nanumgothic-regular-normal-black-36px">{nike}</div>
        <div className="hm nanumgothic-regular-normal-black-36px">{hM}</div>
        <div className="uniqlo nanumgothic-regular-normal-black-36px">{uniqlo}</div>
        <div className="forever21 nanumgothic-regular-normal-black-36px">{forever21}</div>
      </div>
      <div className="backdrop"></div>
    </div>
  );
}
