<template>
    <Layout style="height: 100%" class="main">
        <Header class="header">
            <span @click="reload">Sentiment Analyzer Portal</span>
        </Header>
        <Layout class="mainContentLayout">
            <Sider class="mainContentLayoutSider" :width="248">
                <SiderMenu @on-select="turnToPage" />
            </Sider>
            <Content class="content-wrapper">
                <router-view />
            </Content>
        </Layout>
    </Layout>
</template>

<script>
import './main.less';
import SiderMenu from './components/siderMenu';
export default {
    name: 'Main',
    components: {
        SiderMenu
    },
    methods: {
        reload() {
            window.location.reload();
        },
        turnToPage(route) {
            this.$router.push(route);
        }
    },
    mounted() {
        this.$router.push('/dashboard');
    }
};
</script>
