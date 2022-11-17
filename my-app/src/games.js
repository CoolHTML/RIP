import React, {Component} from 'react';
import {
    BrowserRouter,
    Switch,
    Route,
    Link,
    useParams,
    useRouteMatch
} from "react-router-dom";


class CURRGAME extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],

        }
        this.gameId=1;


    }
    componentDidMount(){
        let combo=window.location.pathname.split('/');
        this.rangeId=combo[2]
        const res = fetch("http://127.0.0.1:8000/games/"+this.gameId)
        .then (res => res.json())
        .then(

            (result) =>{
                this.setState({
                    isLoaded:true,
                    items: result,
                });
                // this.range=result;

            },
            (error) =>{
            this.setState({
                isLoaded:false,
                error});
            }
        )
    }
    render() {
        const {error, isLoaded, items} = this.state;
        console.log('AAAAAAAAAAAAAAA');
        return (

            <div>

                <div><h1>Описание: {items.description}</h1></div>
                <div><h1>Имя мастера: {items.masters_name}</h1></div>
                <div><h1>Максимальное количество игроков: {items.number_of_players}</h1></div>
                <div><h1>Текущее число игроков: {items.current_number_of_players}</h1></div>
                <div><h1>Цена игры: {items.price}</h1></div>






            </div>
        );
    }
}

export default CURRGAME;