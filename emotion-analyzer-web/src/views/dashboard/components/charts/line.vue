<template>
    <div ref="dom"></div>
</template>

<script>
import echarts from 'echarts';
import { on, off } from '@/libs/tools';
export default {
    name: 'serviceRequests',
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
        var positiveData = [376, 358, 299, 120, 290, 330, 310];
        var negativeData = [89, 220, 81, 200, 90, 230, 210];
        var positiveRate = [];
        for (var i = 0; i < positiveData.length; i++) {
            positiveRate.push(Math.round((positiveData[i] / (positiveData[i] + negativeData[i])) * 10000) / 100);
        }
        const option = {
            title: {
                text: 'Performance of the Past 7 Days',
                subtext: this.subtext
            },
            tooltip: {
                trigger: 'axis'
            },
            grid: {
                left: '1.2%',
                right: '1%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [
                {
                    type: 'category',
                    boundaryGap: false,
                    data: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    minInterval: 1
                },
                {
                    type: 'value',
                    max: 100,
                    min: 0
                }
            ],
            series: [
                {
                    name: 'Positive Call',
                    type: 'line',
                    yAxisIndex: 0,
                    lineStyle: {
                        color: '#19be6b'
                    },
                    areaStyle: {
                        normal: {
                            color: '#19be6b'
                        }
                    },
                    itemStyle: {
                        color: '#19be6b'
                    },
                    data: positiveData
                },
                {
                    name: 'Negative Call',
                    type: 'line',
                    yAxisIndex: 0,
                    lineStyle: {
                        color: '#ed4014'
                    },
                    itemStyle: {
                        color: '#ed4014'
                    },
                    areaStyle: {
                        normal: {
                            color: '#ed4014'
                        }
                    },
                    data: negativeData
                },

                {
                    name: 'Positive Call Proportion',
                    type: 'line',
                    yAxisIndex: 1,
                    lineStyle: {
                        color: '#2d8cf0',
                        width: 6
                    },
                    itemStyle: {
                        color: '#2d8cf0'
                    },

                    data: positiveRate
                }
            ]
        };
        this.$nextTick(() => {
            this.dom = echarts.init(this.$refs.dom);
            this.dom.setOption(option);
            on(window, 'resize', this.resize);
        });
    },
    beforeDestroy() {
        off(window, 'resize', this.resize);
    }
};
</script>
