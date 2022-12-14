import React, {Component} from 'react';
import {Link} from "react-router-dom";


function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

class Bag extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            userid:{},
            games:[],
            toDelete:null
        }


    }
    componentDidMount() {
//        this.load_client();
        this.setState({userid: localStorage.getItem('userid')})
        this.load_games();
        // this.load_sum();
    }
    load_games(){
    const requestOptions = {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                };

        const res = fetch('http://127.0.0.1:8000/bag?player='+localStorage.getItem('userid'), requestOptions)
        .then (res => res.json())
        .then(
            (result) =>{
                this.setState({
                    isLoaded:true,
                    games:result
                });
                console.log(result)
            }
        )

    }





    render() {
        const {error, isLoaded,games, userid} = this.state;
        // console.log(purchases);
        const decline=(gameid)=>{
            const deleteOptions = {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                     },
                };
            fetch(`http://127.0.0.1:8000/players_in_game/${gameid}/`, deleteOptions)
                .then(response=> {
                    this.load_games();
                })
            alert(`Удалено из корзины: ${ gameid } `)
        }



        return (
            <div>
                <div className={"bag_title"}>Мои игры</div>
                <div className={'bag'}>
                {games.map((game,index)=>(
                    <div key={"gameId:"+game.game_id} className={'purchase'}>
                        <div className={'game_description'}>
                            {game.game_id.id}: {game.game_id.description}
                            <input id="delete_purchase_button" className={'delete_purchase_button'}
                               type="submit" value="X" onClick={()=>{
                                   decline(game.id)
                        }}/>
                        </div>

                    </div>
                ))}
                </div>

            </div>
        );


    }
}


export default Bag;