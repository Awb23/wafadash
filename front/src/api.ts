import axios from 'axios';

// This gets the live backend URL from Railway's variables, or defaults to localhost
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true, // IMPORTANT: This allows the browser to send cookies (like the CSRF token)
});

// This tells Axios to automatically find the CSRF token cookie from the browser
// and send it in a header that Django understands.
apiClient.defaults.xsrfCookieName = 'csrftoken';
apiClient.defaults.xsrfHeaderName = 'X-CSRFToken';

export default apiClient;