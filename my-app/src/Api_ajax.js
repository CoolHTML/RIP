import React, {Component} from 'react';




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
        fetch("http://127.0.0.1:8000/games/")
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
    render(){
        const {error, isLoaded, items} = this.state;
        if(error){
            return <p> ERROR </p>
        } else {
            return <p>LOADED</p>
        }
    }
}