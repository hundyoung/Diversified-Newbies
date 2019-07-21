<template>
    <div ref="dom" class="charts chart-bar"></div>
</template>

<script>
import echarts from 'echarts';
import tdTheme from './theme.json';
import { on, off } from '@/libs/tools';
echarts.registerTheme('tdTheme', tdTheme);
export default {
    name: 'ChartBar',
    props: {},
    data() {
        return {
            dom: null
        };
    },
    methods: {
        resize() {
            this.dom.resize();
        }
    },
    mounted() {
        this.$nextTick(() => {
            let xAxisData = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
            let option = {
                title: {
                    text: 'Number of Calls'
                },
                xAxis: {
                    type: 'category',
                    data: xAxisData
                },
                yAxis: {
                    type: 'value'
                },
                legend: {
                    left: 'right',
                    top: 'bottom'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} : {c}'
                },
                series: [
                    { name: 'Insurance', stack: 'numberOfCall', type: 'bar', data: [124, 185, 154, 221, 157, 128, 81] },
                    { name: 'Investment', stack: 'numberOfCall', type: 'bar', data: [118, 84, 56, 76, 57, 68, 35] },
                    {
                        name: 'Credit Card',
                        stack: 'numberOfCall',
                        type: 'bar',
                        data: [125, 131, 124, 145, 186, 127, 81]
                    },
                    {
                        name: 'General Inquiry',
                        stack: 'numberOfCall',
                        type: 'bar',
                        data: [253, 195, 78, 52, 165, 177, 88]
                    },
                    { name: 'Complaint', stack: 'numberOfCall', type: 'bar', data: [23, 56, 85, 45, 66, 15, 65] }
                ]
            };
            this.dom = echarts.init(this.$refs.dom, 'tdTheme');
            this.dom.setOption(option);
            on(window, 'resize', this.resize);
        });
    },
    beforeDestroy() {
        off(window, 'resize', this.resize);
    }
};
</script>
