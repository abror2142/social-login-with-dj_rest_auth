import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook, faGithub, faGoogle } from "@fortawesome/free-brands-svg-icons";
function Login() {

    return (
        <div className="login-page">
            <h1 className='app-header'>demo</h1>
            <p className="dots">...</p>
            <p className="title">Login with:</p>
            <div className="social-icons">
                <FontAwesomeIcon 
                    className="google-icon social-icon"
                    icon={faGoogle} 
                />
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