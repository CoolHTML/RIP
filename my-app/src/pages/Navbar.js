import {Link} from "react-router-dom"
import { useState, useEffect } from 'react';

export default function Navbar(){

    return <nav className="nav">
    <Link to = "/" className="site-title">RollPlayWorld</Link>
    <ul>
    {localStorage.getItem('accessToken') === ''?
    <>
    <CustomLink to = "/">На главную</CustomLink>
    <CustomLink to = "/signup">Все игры</CustomLink>
    <CustomLink to = "/register">Регистрация</CustomLink>
    <CustomLink to = "/auth">Авторизация</CustomLink>
    </>
    :
    <>
        <CustomLink to = "/">На главную</CustomLink>
    <CustomLink to = "/signup">Все игры</CustomLink>
    <CustomLink to = "/bag">Мои игры</CustomLink>
    <CustomLink to = "/logout">Деавторизация</CustomLink>
    </>
    }


    </ul>
    </nav>
}

function CustomLink({href, children, ...props}){
const path = window.location.pathname

return(
    <li className={path === href ? "active" : ""}>
        <Link href={href} {...props}>
        {children}
        </Link>
    </li>
    )
}
