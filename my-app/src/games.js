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
        this.load_game();
    }
    load_game(){
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

        const buy=(game)=> {
            if(game) {
                const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json',
                 'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                 },


                body: JSON.stringify({ 'user':localStorage.getItem('userid'), 'player':'test', 'approved_to_play': false,
                 game_id:game.id})
                };
                console.log(game)

                fetch(`http://localhost:8000/players_in_game/`, requestOptions)
                    .then(()=>{this.load_game()})

                alert(`Добавлено в корзину: ${ game.id } `)
                        }
                    }

        return (

            <div>

                <div><h1>Описание: {items.description}</h1></div>
                <div><h1>Имя мастера: {items.masters_name}</h1></div>
                <div><h1>Максимальное количество игроков: {items.number_of_players}</h1></div>
                <div><h1>Текущее число игроков: {items.current_number_of_players}</h1></div>
                <div><h1>Цена игры: {items.price}</h1></div>

<input id="buy_button" className="buy_button" type="submit" value="В корзину" onClick={()=>{buy(items)}}/>




            </div>
        );
    }
}

export default CURRGAME;