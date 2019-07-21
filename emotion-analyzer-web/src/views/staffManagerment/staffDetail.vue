<template>
    <div>
        <h1>Staff Detail</h1>
        <Divider />
        <Card shadow>
            <Divider orientation="left">Recording Detail</Divider>
            <Form label-position="top">
                <Row>
                    <i-col span="6" class="formCol">
                        <FormItem label="Staff Name">
                            <Input v-model="staffDetail.name" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Today total calls">
                            <Input v-model="staffDetail.todayCall" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Number of Today Positive Calls">
                            <Input v-model="staffDetail.todayPositiveCalls" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Number of Today Negative calls">
                            <Input v-model="staffDetail.todayNegativeCalls" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Today Performance Evaluation">
                            <div style="text-align:center;">
                                <span class="fa fa-thumbs-up fa-5x"></span>
                            </div>
                        </FormItem>
                    </i-col>
                </Row>
            </Form>
            <Row>
                <i-col span="8" class="formCol">
                    <Divider orientation="left">Staff skill</Divider>
                    <div ref="chartDom" style="height:300px;"></div>
                </i-col>
                <i-col span="16" class="formCol">
                    <Divider orientation="left">Today's call</Divider>
                    <Table border stripe :columns="columns" :data="tableData">
                        <template slot-scope="{ row }" slot="recordingName">
                            <strong>{{ row.recordingName }}</strong>
                        </template>
                        <template slot-scope="{ row }" slot="performanceEvaluation">
                            <span
                                class="fa fa-thumbs-up fa-2x"
                                style="color:#19be6b"
                                v-if="row.performanceEvaluation === 'good'"
                            ></span>
                            <span
                                class="fa fa-thumbs-down fa-2x"
                                style="color:#ed4014"
                                v-if="row.performanceEvaluation === 'bad'"
                            ></span>
                        </template>
                        <template slot-scope="{ row }" slot="action">
                            <Button type="primary" size="small" style="margin-right: 5px" @click="viewRecording(row)">
                                View
                            </Button>
                        </template>
                    </Table>
                    <br />
                    <div style="text-align:right">
                        <Page :total="100" show-elevator />
                    </div>
                </i-col>
            </Row>
        </Card>
    </div>
</template>
<script>
import echarts from 'echarts';

import { on, off } from '@/libs/tools';
export default {
    name: 'staffDetail',
    components: {},
    data() {
        return {
            chartDom: null,
            staffDetail: {
                name: 'John',
                todayCall: 20,
                todayPositiveCalls: 15,
                todayNegativeCalls: 5
            },
            columns: [
                {
                    title: 'Recording Name',
                    slot: 'recordingName',
                    align: 'center'
                },
                {
                    title: 'Lenth',
                    key: 'lenth',
                    align: 'center'
                },
                {
                    title: 'Upload Time',
                    key: 'uploadTime',
                    align: 'center'
                },
                {
                    title: 'Performance Evaluation',
                    slot: 'performanceEvaluation',
                    align: 'center'
                },
                {
                    title: 'Action',
                    slot: 'action',
                    width: 150,
                    align: 'center'
                }
            ],
            tableData: [
                {
                    recordingName: '201906300001',
                    lenth: '12:30',
                    performanceEvaluation: 'good',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300002',
                    lenth: '09:24',
                    performanceEvaluation: 'good',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300004',
                    lenth: '08:33',
                    performanceEvaluation: 'bad',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100004',
                    lenth: '08:20',
                    performanceEvaluation: 'good',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100005',
                    lenth: '05:20',
                    performanceEvaluation: 'good',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100033',
                    lenth: '04:17',
                    performanceEvaluation: 'bad',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100158',
                    lenth: '03:17',
                    performanceEvaluation: 'good',
                    uploadTime: '2019-06-30 15:30'
                }
            ]
        };
    },
    methods: {
        viewRecording() {
            this.$router.push('RecordingDetail');
        },
        resize() {
            this.dom.resize();
        }
    },
    mounted() {
        let option = {
            radar: {
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
        this.chartDom = echarts.init(this.$refs.chartDom, 'tdTheme');
        this.chartDom.setOption(option);
        on(window, 'resize', this.resize);
    },
    beforeDestroy() {
        off(window, 'resize', this.resize);
    }
};
</script>
