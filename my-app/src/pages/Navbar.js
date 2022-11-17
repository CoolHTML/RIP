import {Link} from "react-router-dom"
export default function Navbar(){
    return <nav className="nav">
    <Link to = "/" className="site-title">RollPlayWorld</Link>
    <ul>
    <CustomLink to = "/">На главную</CustomLink>
    <CustomLink to = "/signup">Все игры</CustomLink>
    <CustomLink to = "/register">Регистрация</CustomLink>
    <CustomLink to = "/realsignup">Авторизация</CustomLink>
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
