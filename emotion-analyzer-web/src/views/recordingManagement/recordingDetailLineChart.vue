<template>
    <div ref="dom"></div
></template>
<script>
import echarts from 'echarts';
import { on, off } from '@/libs/tools';
export default {
    name: 'recordingDetailLineChart',
    components: {},
    data() {
        return {
            dom: null,
            charData: []
        };
    },
    methods: {
        doDrawNewChart(charData) {
            this.charData = charData;
            let tableXAxisData = ["00:00"];
            let tableData = [0];
            if (this.charData && this.charData.length > 0) {
                for (let i = 0; i < this.charData.length; i++) {
                    let time = this.charData[i].end_time / 1000;
                    let min = Math.floor(time / 60);
                    let second = Math.round(time % 60);
                    tableXAxisData.push((min < 10 ? '0' + min : min) + ':' + (second < 10 ? '0' + second : second));
                    tableData.push(this.getSentimetNumber(this.charData[i].status));
                }
            }
            const option = {
                grid: {
                    left: 20,
                    right: 20,
                    bottom: 20,
                    top: 20
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: [
                    {
                        type: 'category',
                        data: tableXAxisData,
                        boundaryGap: false
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        minInterval: 1,
                        max: 1,
                        min: -1
                    }
                ],
                series: [
                    {
                        name: 'Sentiment',
                        type: 'line',
                        lineStyle: {
                            color: '#2d8cf0',
                            width: 6
                        },
                        itemStyle: {
                            color: '#2d8cf0'
                        },
                        data: tableData
                    }
                ]
            };
            this.$nextTick(() => {
                echarts.dispose(this.$refs.dom);
                this.dom = echarts.init(this.$refs.dom);
                this.dom.setOption(option);
                on(window, 'resize', this.resize);
            });
        },
        getSentimetNumber(sentiment) {
            if (sentiment === 'female_happy' || sentiment === 'male_happy') {
                return 1;
            } else if (sentiment === 'female_calm' || sentiment === 'male_calm') {
                return 0;
            } else if (
                sentiment === 'female_angry' ||
                sentiment === 'female_fearful' ||
                sentiment === 'female_sad' ||
                sentiment === 'male_sad' ||
                sentiment === 'male_fearful' ||
                sentiment === 'male_angry'
            ) {
                return -1;
            } else {
                return 0;
            }
        }
    },
    mounted() {},
    beforeDestroy() {
        off(window, 'resize', this.resize);
    }
};
</script>
