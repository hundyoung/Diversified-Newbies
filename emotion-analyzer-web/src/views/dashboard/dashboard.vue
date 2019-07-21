<template>
    <div>
        <Row :gutter="20">
            <i-col
                :md="8"
                :lg="8"
                v-for="(infor, i) in inforCardData"
                :key="`infor-${i}`"
                style="height: 120px;padding-bottom: 10px;"
            >
                <infor-card shadow :color="infor.color" :icon="infor.icon" :icon-size="36">
                    <count-to :end="infor.count" count-class="count-style" style="font-size: 50px;" />
                    <p>{{ infor.title }}</p>
                </infor-card>
            </i-col>
        </Row>
        <Row :gutter="20" style="margin-top: 10px;">
            <i-col :md="24" :lg="10" style="margin-bottom: 20px;">
                <Card shadow>
                    <chart-pie style="height: 300px;"></chart-pie>
                </Card>
            </i-col>
            <i-col :md="24" :lg="14" style="margin-bottom: 20px;">
                <Card shadow>
                    <chart-bar style="height: 300px;" />
                </Card>
            </i-col>
        </Row>
        <Row>
            <i-col :md="24" :lg="16" style="margin-bottom: 20px;padding:10px;">
                <Card shadow>
                    <chart-line style="height: 300px;"></chart-line>
                </Card>
            </i-col>
            <i-col :md="24" :lg="8" style="margin-bottom: 20px;padding:10px;">
                <Card shadow>
                    <chart-radar style="height: 300px;"></chart-radar>
                </Card>
            </i-col>
        </Row>
        <br />
    </div>
</template>
<script>
import InforCard from './components/info-card';
import CountTo from './components/count-to';
import { ChartPie, ChartBar, ChartLine, ChartRadar } from './components/charts';
export default {
    name: 'dashboard',
    components: {
        InforCard,
        CountTo,
        ChartPie,
        ChartBar,
        ChartLine,
        ChartRadar
    },
    data() {
        return {
            inforCardData: [
                { title: 'No. of Calls Received', icon: 'ios-headset-outline', count: 538, color: '#2d8cf0' },
                { title: 'No. of Positive Call', icon: 'md-thumbs-up', count: 317, color: '#19be6b' },
                { title: 'No. of Negative Call', icon: 'md-thumbs-down', count: 221, color: '#ed4014' }
            ]
        };
    },
    mounted() {}
};
</script>
