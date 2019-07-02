import Vue from 'vue';
import Router from 'vue-router';
import routers from './routers';
import iView from 'iview';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routers
});

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    next(); // 跳转
});

router.afterEach(() => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});
export default router;
