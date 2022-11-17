import React, {Component} from 'react';
import {
    BrowserRouter,
    Switch,
    Route,
    Link,
    useParams,
    useRouteMatch
} from "react-router-dom";

class RangeType extends Component {

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
    }

    render() {
            const {error, isLoaded, items} = this.state;
            console.log(items);

            let rangeId=parseInt(this.props.match.params.id);
        return (
            <div>
                <h2>Эту игру организовал мастер {rangeId} </h2>

            </div>
        );
    }
}

export default RangeType;