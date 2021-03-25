import React from "react";
import "./style.css";

function App() {
  return <ShopSelection title="NIKE" hM="H&M" uniqlo="UNIQLO" forever21="FOREVER21" />;
}

export default App;


function ShopSelection(props) {
  const { title, hM, uniqlo, forever21 } = props;

  return (
    <div className="shop-selection">
      <h1 className="title nanumgothic-regular-normal-black-36px">{title}</h1>
      <div className="hm nanumgothic-regular-normal-black-36px">{hM}</div>
      <div className="uniqlo nanumgothic-regular-normal-black-36px">{uniqlo}</div>
      <div className="forever21 nanumgothic-regular-normal-black-36px">{forever21}</div>
    </div>
  );
}
