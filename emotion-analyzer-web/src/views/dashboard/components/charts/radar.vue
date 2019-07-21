<template>
    <div ref="dom" class="charts chart-pie"></div>
</template>

<script>
import echarts from 'echarts';
import tdTheme from './theme.json';
import { on, off } from '@/libs/tools';
echarts.registerTheme('tdTheme', tdTheme);
export default {
    name: 'ChartRadar',
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
            let option = {
                title: {
                    text: 'Performance Radar',
                    shadowColor: 'rgba(0, 0, 0, 0.5)',
                    shadowBlur: 20
                },
                radar: {
                    center: ['60%', '65%'],
                    radius: '65%',
                    name: {
                        textStyle: {
                            color: '#fff',
                            backgroundColor: '#999',
                            borderRadius: 3,
                            padding: [3, 5]
                        }
                    },
                    indicator: [
                        { name: 'Insurance Business', max: 100 },
                        { name: 'Investment Business', max: 100 },
                        { name: 'Credit card business', max: 100 },
                        { name: 'General Inquiry', max: 100 },
                        { name: 'Complaint', max: 100 }
                    ]
                },
                series: [
                    {
                        name: 'Skill',
                        type: 'radar',
                        data: [
                            {
                                value: [56, 80, 34, 75, 99, 25],
                                name: 'Skill'
                            }
                        ]
                    }
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
