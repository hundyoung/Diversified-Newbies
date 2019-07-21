<template>
    <div>
        <Row :gutter="20">
            <i-col
                :xs="12"
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
                    <chart-pie
                        style="height: 300px;"
                        :value="pieData"
                        text="The Proportion of Calling type"
                    ></chart-pie>
                </Card>
            </i-col>
            <i-col :md="24" :lg="14" style="margin-bottom: 20px;">
                <Card shadow>
                    <chart-bar style="height: 300px;" :value="barData" text="Number of Calls" />
                </Card>
            </i-col>
        </Row>
        <Row>
            <Card shadow>
                <chart-line style="height: 300px;"></chart-line>
            </Card>
        </Row>
        <br />
    </div>
</template>
<script>
import InforCard from '_components/info-card';
import CountTo from '_components/count-to';
import { ChartPie, ChartBar, ChartLine } from '_components/charts';
export default {
    name: 'dashboard',
    components: {
        InforCard,
        CountTo,
        ChartPie,
        ChartBar,
        ChartLine
    },
    data() {
        return {
            inforCardData: [
                { title: 'No. of Calls Received', icon: 'ios-headset-outline', count: 538, color: '#2d8cf0' },
                { title: 'Number of Positive Call', icon: 'md-thumbs-up', count: 317, color: '#19be6b' },
                { title: 'Number of Negative Call', icon: 'md-thumbs-down', count: 221, color: '#ed4014' }
            ],
            pieData: [
                { value: 335, name: 'Insurance' },
                { value: 135, name: 'Investment' },
                { value: 1548, name: 'Credit card' },
                { value: 310, name: 'General Inquiry' },
                { value: 234, name: 'Complaint' }
            ],
            barData: {
                Mon: 13253,
                Tue: 34235,
                Wed: 26321,
                Thu: 12340,
                Fri: 24643,
                Sat: 1322,
                Sun: 1324
            }
        };
    },
    mounted() {}
};
</script>
