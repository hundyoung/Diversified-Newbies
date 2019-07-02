<template>
    <Menu theme="dark" width="auto" accordion @on-select="handleSelect">
        <Submenu v-for="menu in menuList" :name="menu.name" :key="menu.path">
            <template slot="title">
                <Icon type="ios-paper" />
                {{ menu.title }}
            </template>
            <template v-for="subMenu in menu.children">
                <MenuItem v-if="subMenu.displayInMenu" :name="subMenu.name" :key="subMenu.path">
                    {{ subMenu.title }}
                </MenuItem>
            </template>
        </Submenu>
    </Menu>
</template>

<script>
import roters from '_frame/router/routers';
import { forEach } from '@/libs/tools';

export default {
    name: 'SiderMenu',
    props: {},
    data() {
        return {
            menuList: []
        };
    },

    methods: {
        handleSelect(name) {
            this.$emit('on-select', name);
        }
    },
    computed: {},
    mounted() {
        const vm = this;
        forEach(roters, item => {
            if (item.displayInMenu) {
                vm.menuList.push(item);
            }
        });
    }
};
</script>
