// front/src/api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true, // IMPORTANT: This allows sending cookies
});

// This automatically reads the 'csrftoken' cookie and puts it in the 'X-CSRFToken' header
apiClient.defaults.xsrfCookieName = 'csrftoken';
apiClient.defaults.xsrfHeaderName = 'X-CSRFToken';

export default apiClient;