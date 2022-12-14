import React,{useEffect, useState} from 'react';
import {Link, useHistory} from "react-router-dom";

export const StaffMenu = () => {


    return (


            <div>
                <div className={'manager_choices_list'}>
                    <div className={'manager_choice'}>
                        <Link to={"/manager/add"}>Добавить</Link>
                    </div>
                    <div className={'manager_choice'}>
                        <Link to={"/manager/edit"}>Изменить</Link>
                    </div>
                    <div className={'manager_choice'}>
                        <Link to={"/manager/clients"}>Наши клиенты</Link>
                    </div>
                </div>
            </div>


    );
};

export default StaffMenu;