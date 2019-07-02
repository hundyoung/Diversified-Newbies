import axios from 'axios';

axios.defaults.headers.post['Content-Type'] = 'application/json';

let baseAxios = axios.create({
    baseURL: 'http://www.baidu.com',
    timeout: 10000
});

export default baseAxios;
