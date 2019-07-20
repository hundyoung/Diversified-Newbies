import axios from 'axios';

axios.defaults.headers.post['Content-Type'] = 'application/json';

let baseAxios = axios.create({
    baseURL: 'http://localhost:5000/',
    timeout: 6000000
});

export default baseAxios;
