import React, { useState, useEffect } from 'react';
import {Link, Route} from "react-router-dom";



function AddForm(props) {
    const [access, setAccess] = useState(localStorage.getItem('accessToken'))
    const [refresh, setRefresh] = useState(localStorage.getItem('refreshToken'))
    // const [refreshRequired, setRefreshRequired] = useState(false)
    const [userID, setUserId] = useState(localStorage.getItem('ID'))
    // const [loading, setLoading] = useState()
    // const [error, setError] = useState()
    const [newRange, setNewRange] = useState()


    const add_range= e=>{
        e.preventDefault();
            const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${access}`  },
            body: JSON.stringify({
                    name:newRange
                })
            };
            fetch(`http://127.0.0.1:8000/name`, requestOptions)
            setNewRange("")
        }


        return (
            <div className="AddForm">

                <div>
                <h1>Добавление </h1>
                    <form className="AddForm" onSubmit={add_range}>
                        <div>Название Игры</div>
                        <input type="text" name="название игры" value={newRange}
                               onChange={e => setNewRange(e.target.value)} placeholder="Название"/>
                        <input type="submit" name="submit" value="+"/>
                    </form>

                </div>

            </div>
        );

}


export default AddForm;