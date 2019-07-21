<template>
    <div>
        <h1>Recording Detail</h1>
        <Divider />
        <Card shadow>
            <Divider orientation="left">Recording Detail</Divider>
            <Form label-position="top">
                <Row>
                    <i-col span="6" class="formCol">
                        <FormItem label="Recording Name">
                            <Input v-model="recording.record_name" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Employee ID">
                            <Input v-model="recording.employee_id" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Record Date">
                            <Input v-model="recording.record_date" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Record Name">
                            <Input v-model="recording.record_name" readonly></Input>
                        </FormItem>
                    </i-col>
                </Row>
            </Form>

            <Row>
                <i-col span="6" class="formCol">
                    <Divider orientation="left"> Overall performance evaluation</Divider>
                    <div style="text-align:center">
                        <Rate disabled v-model="recording.overall_evaluation" />
                    </div>
                </i-col>
                <i-col span="18" class="formCol">
                    <Divider orientation="left">Sentiment Analyzer</Divider>
                    <div>
                        <lineChart ref="lineChart" style="height: 300px;"></lineChart>
                        <!-- <Timeline>
                            <TimelineItem v-for="item in recording.analyzer_result" :key="item.end_time">
                                <p class="time">{{ item.start_time / 1000 }} - {{ item.end_time / 1000 }}</p>
                                <p class="content">
                                    <span
                                        v-if="item.status === 'female_happy' || item.status === 'male_happy'"
                                        class="fa fa-smile-o fa-3x"
                                    ></span>
                                    <span
                                        v-if="item.status === 'female_calm' || item.status === 'male_calm'"
                                        class="fa fa-meh-o fa-3x"
                                    ></span>
                                    <span
                                        v-if="
                                            item.status === 'female_angry' ||
                                                item.status === 'female_fearful' ||
                                                item.status === 'female_sad' ||
                                                item.status === 'male_sad' ||
                                                item.status === 'male_fearful' ||
                                                item.status === 'male_angry'
                                        "
                                        class="fa fa-frown-o fa-3x"
                                    ></span>
                                </p>
                            </TimelineItem>
                        </Timeline> -->
                    </div>
                </i-col>
            </Row>
        </Card>
    </div>
</template>
<script>
import lineChart from './recordingDetailLineChart';
export default {
    name: 'recordingList',
    components: { lineChart },
    data() {
        return {
            charData: [],
            recording: {}
        };
    },
    methods: {
        drawChart() {
            this.$refs.lineChart.doDrawNewChart(this.recording.analyzer_result);
        }
    },
    mounted() {
        let vm = this;
        this.$ajax
            .get('/audio_details?record_id=' + this.$route.query.record_id)
            .then(function(response) {
                vm.recording = response.data;
                vm.recording.overall_evaluation = vm.recording.overall_evaluation
                    ? vm.recording.overall_evaluation + 2
                    : 3;
                vm.drawChart();
            })
            .catch(function(error) {
                console.error(error);
            });
    }
};
</script>
