// front/src/api.js

import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true, // This is crucial for sending cookies
});

// This configures Axios to automatically handle the Django CSRF token
apiClient.defaults.xsrfCookieName = 'csrftoken';
apiClient.defaults.xsrfHeaderName = 'X-CSRFToken';

export default apiClient;