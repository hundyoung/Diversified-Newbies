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
                        <FormItem label="Employee Id">
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
                        <span class="fa fa-thumbs-up fa-5x"></span>
                    </div>
                </i-col>
                <i-col span="6" class="formCol">
                    <Divider orientation="left">Sentiment Analyzer</Divider>
                    <div>
                        <Timeline>
                            <TimelineItem v-for="item in recording.analyzer_result" :key="item.end_time">
                                <p class="time">{{ item.start_time / 1000 }} - {{ item.end_time / 1000 }}</p>
                                <p class="content">
                                    <span
                                        v-if="item.status === 'female_happy' || item.status === 'male_angry'"
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
                        </Timeline>
                    </div>
                </i-col>
            </Row>
        </Card>
    </div>
</template>
<script>
export default {
    name: 'recordingList',
    components: {},
    data() {
        return {
            recording: {}
        };
    },
    methods: {},
    mounted() {
        let vm = this;
        this.$ajax
            .get('/audio_details?record_id=' + this.$route.query.record_id)
            .then(function(response) {
                vm.recording = response.data;
            })
            .catch(function(error) {
                console.error(error);
            });
    }
};
</script>
