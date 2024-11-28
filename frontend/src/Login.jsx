import {Link, redirect } from "react-router-dom";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook, faGithub, faGoogle } from "@fortawesome/free-brands-svg-icons";

function Login() {

    const googleClientID = import.meta.env.VITE_GOOGLE_CLIENT_ID
    const googleCallbackURL = import.meta.env.VITE_GOOGLE_CALLBACK_URL

    const googleSignInURL = "https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=" + googleCallbackURL + "&prompt=consent&response_type=code&client_id=" + googleClientID + "&scope=openid%20email%20profile&access_type=offline"
    
    const githubClientID = import.meta.env.VITE_GITHUB_CLIENT_ID
    const githubCallbackURL = import.meta.env.VITE_GITHUB_CALLBACK_URL

    const githubSignInURL = "https://github.com/login/oauth/authorize?redirect_uri=" + githubCallbackURL + "&prompt=consent&response_type=code&client_id=" + githubClientID + "&scope=user&access_type=offline"

    
    return (
        <div className="login-page">
            <h1 className='app-header'>demo</h1>
            <p className="dots">...</p>
            <p className="title">Login with:</p>
            <div className="social-icons">

                <a href={googleSignInURL} className="social-icon-box">
                    <FontAwesomeIcon 
                        className="google-icon social-icon"
                        icon={faGoogle} 
                    />
                </a>

                <a href={githubSignInURL} className="social-icon-box">
                    <FontAwesomeIcon 
                        className="github-icon social-icon"
                        icon={faGithub} 
                    />
                </a>

                <a href="#" className="social-icon-box">
                    <FontAwesomeIcon 
                        className="facebook-icon social-icon"
                        icon={faFacebook} 
                    />
                </a>

            </div>
        </div>
    )
}

export default Login