import axios from 'axios';

const instance = axios.create({
    baseURL: window.location.origin,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    headers: {
        'X-Requested-With': 'XMLHttpRequest'

    }
});

instance.interceptors.response.use(
    response => Promise.resolve(response.data),
    error => Promise.reject(error)
);

export default instance;
