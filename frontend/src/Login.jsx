import {Link, redirect } from "react-router-dom";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook, faGithub, faGoogle } from "@fortawesome/free-brands-svg-icons";

function Login() {

    let clientID = import.meta.env.VITE_CLIENT_ID
    const callbackURL = import.meta.env.VITE_CALLBACK_URL
    const url = "https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=" + callbackURL + "&prompt=consent&response_type=code&client_id=" + clientID + "&scope=openid%20email%20profile&access_type=offline"
   

    return (
        <div className="login-page">
            <p>ENV: {import.meta.env.VITE_my_var}</p>
            <h1 className='app-header'>demo</h1>
            <p className="dots">...</p>
            <p className="title">Login with:</p>
            <div className="social-icons">
                <a href={url}>
                    <FontAwesomeIcon 
                        className="google-icon social-icon"
                        icon={faGoogle} 
                        
                    />
                 </a>
                    <FontAwesomeIcon 
                        className="github-icon social-icon"
                        icon={faGithub} 
                    />
                <FontAwesomeIcon 
                    className="facebook-icon social-icon"
                    icon={faFacebook} 
                />
            </div>
        </div>
    )
}

export default Login