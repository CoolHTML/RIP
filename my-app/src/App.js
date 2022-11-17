import { BrowserRouter, Route, Routes, Link, Switch } from "react-router-dom";
import React, { Component }  from 'react';
import Navbar from './pages/Navbar'
import RangeType from "./RangeType"
import CURRGAME from "./games"
import Registration from "./pages/registration"

export default class Ccomponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        }
    }
    componentDidMount(){
        const res = fetch("http://127.0.0.1:8000/games/")
        .then (res => res.json())
        .then(

            (result) =>{
                this.setState({
                    isLoaded:true,
                    items: result,
                });
            },
            (error) =>{
            this.setState({
                isLoaded:true,
                error});
            }
        )
        console.log(res)
    }
    render(){
        const {error, isLoaded, items} = this.state;
        const ebanina=(props)=>{
            return <RangeType {...props}/>
        }
        if(error){
            return <p>ERROR</p>
        } else if(!isLoaded) {
            return <p>LOADING</p>
        } else {
            return(

<React.Fragment>
<BrowserRouter basename="/">
{Navbar()}
          <Switch>
            <Route exact path="/">
              <h1>Это наша стартовая страница</h1>
            </Route>
            <Route exact path="/signup">

              <ul>{items.map(item =>(<div style={{boxShadow: "0 4px 8px 0 rgba(0,0,0,0.2)", transition: "0.3s", width: "49%",float: "left", display:"block"}}>
  <div style={{padding: "2px 16px"}}>
    <h4><b>{item.masters_name}</b></h4>
    <p style={{}}>Максимальное кол-во игроков: {item.number_of_players}</p>
    <p style={{}}>Текущее кол-во игроков: {item.current_number_of_players}</p>
    <p style={{}}>Цена игры: {item.price}</p>
    <p style={{}}>ID: {item.pk}</p>
    <Link to ={`/signup/${item.pk}`}>
    <button className="cardButton" target="_blank" variant="primary">Изучить подробнее</button>
    </Link>
  </div>
</div>))}</ul>
            </Route>
              <Route exact path={"/signup/:id"}>
              <CURRGAME/>
            </Route>
                          <Route exact path={"/register"}>
              <Registration/>
            </Route>
          </Switch>
</BrowserRouter>


</React.Fragment>

)
        }
    }
}