import React, {Component} from 'react';
import {Link} from "react-router-dom";
import StaffMenu from "./StaffMenu";


class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            client:{},
            isStaff:false,


        }
        this.bagId=0;
    }
    componentDidMount() {
        // this.load_bag_states();
        if(localStorage.getItem('userId')!=='null'){
        this.load_client();
        }
    }
    load_client(){
        const requestOptions = {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                };
        const res = fetch(`http://127.0.0.1:8000/user/${localStorage.getItem('userid')}`, requestOptions)
        .then (res => res.json())
        .then(
            (result) =>{
                this.setState({
                    isLoaded:true,
                    client: result,
                    isStaff:result.is_staff,
                });
            }
        )
            .then(()=>{
                console.log('CLIENT')
                console.log(this.state.client)
                console.log(this.state.isStaff)
            })
    }

    render() {
        const {error, isLoaded,client, isStaff} = this.state;
        // console.log(purchases);
        return (

            <>
                {isStaff?
                <>
                    <StaffMenu/>
                </>
                :
                    <>Hello!</>
                }

            </>

        );


    }
}


export default Home;