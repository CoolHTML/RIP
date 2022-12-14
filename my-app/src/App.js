import { BrowserRouter, Route, Routes, Link, Switch } from "react-router-dom";
import React, { Component }  from 'react';
import Navbar from './pages/Navbar'
import RangeType from "./RangeType"
import CURRGAME from "./games"
import Registration from "./pages/registration"
import Auth from './autharisation'
import Logout from './logout'
import Home from './pages/Home'
import Bag from './pages/Bag'
import AddForm from './pages/add'
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
        const requestOptions = {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                };
        const res = fetch("http://127.0.0.1:8000/games/", requestOptions)
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
              <Home/>
            </Route>
            <Route exact path="/signup">

              <ul>{items.map(item =>(<div style={{boxShadow: "0 4px 8px 0 rgba(0,0,0,0.2)", transition: "0.3s", minWidth: "500px",float: "left", display:"inline-block", margin:"auto"}}>
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
             <Route exact path={"/auth"}>
              <Auth/>
            </Route>
             <Route exact path={"/logout"}>
              <Logout/>
            </Route>
            <Route exact path={"/bag"}>
              <Bag/>
            </Route>
            <Route exact path={"/add"}>
            <AddForm/>
            </Route>
          </Switch>
</BrowserRouter>


</React.Fragment>

)
        }
    }
}