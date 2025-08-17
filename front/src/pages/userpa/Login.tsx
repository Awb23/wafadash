import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { FiUser, FiLock, FiAlertCircle } from 'react-icons/fi';
import './Login.css';
import logo from './assets/logo.png';

// ✅ This is the line to change. It now uses the smart environment variable.
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string>('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');

    try {
      // Use the API_BASE_URL variable for the request
      const response = await axios.post(`${API_BASE_URL}/api/apilogin/`, {
        username,
        password,
      });

      const { access, is_admin, username: loggedInUsername } = response.data; // Also get username

      // Save user info to localStorage
      localStorage.setItem('token', access);
      localStorage.setItem('isAdmin', is_admin ? 'true' : 'false');
      localStorage.setItem('username', loggedInUsername); // Save the username

      if (is_admin) {
        navigate('/admin');
      } else {
        navigate('/home');
      }
    } catch (err: any) {
      if (axios.isAxiosError(err) && err.response) {
        setError(err.response.data?.error || 'Échec de la connexion. Vérifiez vos identifiants.');
      } else {
        setError('Échec de la connexion en raison d\'une erreur de réseau ou de serveur.');
      }
    }
  };

  return (
    <div className="login-container">
      <form onSubmit={handleLogin} className="login-form" noValidate>
        <div className="logo-wrapper">
          <img src={logo} alt="Tamanar Assistance Logo" className="login-logo" />
        </div>
        <h2 className="form-title">Bienvenue</h2>

        {error && (
          <div className="error-message" role="alert">
            <FiAlertCircle aria-hidden="true" />
            <span>{error}</span>
          </div>
        )}

        <div className="input-group">
          <input
            type="text"
            id="username"
            value={username}
            onChange={e => setUsername(e.target.value)}
            placeholder="Nom d'utilisateur"
            className="input-field"
            required
            autoComplete="username"
          />
          <FiUser className="input-icon" aria-hidden="true" />
        </div>

        <div className="input-group">
          <input
            type="password"
            id="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            placeholder="Mot de passe"
            className="input-field"
            required
            autoComplete="current-password"
          />
          <FiLock className="input-icon" aria-hidden="true" />
        </div>

        <button type="submit" className="login-btn">
          Se connecter
        </button>
      </form>
    </div>
  );
}