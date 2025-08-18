import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import apiClient from '../../api'; // Standardized import path
import { FiUser, FiLock, FiAlertCircle } from 'react-icons/fi';
import './Login.css';
import logo from './assets/logo.png';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string>('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');

    try {
      // Send the login request using our configured API client
      const response = await apiClient.post('/api/apilogin/', {
        username,
        password,
      });

      // Get the token and user info from the response
      const { access, is_admin, username: loggedInUsername } = response.data;

      // Save the token and user info in the browser's local storage
      localStorage.setItem('token', access);
      localStorage.setItem('isAdmin', is_admin ? 'true' : 'false');
      localStorage.setItem('username', loggedInUsername);

      // After a successful login, send all users to the home page
      navigate('/home');

    } catch (err: any) {
      // If the API sends an error, display it to the user
      if (err.response && err.response.data && err.response.data.error) {
        setError(err.response.data.error);
      } else {
        setError('Login failed. Please check your connection or contact support.');
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