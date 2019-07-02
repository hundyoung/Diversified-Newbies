import Vue from 'vue';
import App from './App.vue';
import router from '_frame/router';
import store from '_frame/store';
import iView from 'iview';
import baseAxios from '_frame/ajax/baseAxios';
import './index.less';
import 'font-awesome/scss/font-awesome.scss';
import locale from 'iview/dist/locale/en-US';
Vue.use(iView, { locale });

Vue.config.productionTip = false;

Vue.prototype.$ajax = baseAxios;
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
