<template>
    <div ref="dom" class="charts chart-pie"></div>
</template>

<script>
import echarts from 'echarts';
import tdTheme from './theme.json';
import { on, off } from '@/libs/tools';
echarts.registerTheme('tdTheme', tdTheme);
export default {
    name: 'ChartPie',
    props: {
        value: Array
    },
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
            var data = [
                { value: 335, name: 'Insurance' },
                { value: 135, name: 'Investment' },
                { value: 1548, name: 'Credit card' },
                { value: 310, name: 'General Inquiry' },
                { value: 234, name: 'Complaint' }
            ];
            let legend = data.map(_ => _.name);
            let option = {
                title: {
                    text: 'Inquiry Distribution',
                    shadowColor: 'rgba(0, 0, 0, 0.5)',
                    shadowBlur: 20
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{b} : {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    top: 'bottom',
                    data: legend
                },
                series: [
                    {
                        type: 'pie',
                        radius: '55%',
                        center: ['65%', '60%'],
                        data: data,
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
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
