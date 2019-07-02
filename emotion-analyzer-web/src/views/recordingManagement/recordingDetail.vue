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
                            <Input v-model="recording.recordingName" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Staff Name">
                            <Input v-model="recording.staff" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="lenth">
                            <Input v-model="recording.lenth" readonly></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="upload time">
                            <Input v-model="recording.uploadTime" readonly></Input>
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
                    <Divider orientation="left">Emotion Analyzer</Divider>
                    <div>
                        <Timeline>
                            <TimelineItem>
                                <p class="time">01:00</p>
                                <p class="content"><span class="fa fa-meh-o fa-3x"></span></p>
                            </TimelineItem>
                            <TimelineItem>
                                <p class="time">06:00</p>
                                <p class="content"><span class="fa fa-frown-o fa-3x"></span></p>
                            </TimelineItem>
                            <TimelineItem>
                                <p class="time">08:30</p>
                                <p class="content"><span class="fa fa-frown-o fa-3x"></span></p>
                            </TimelineItem>
                            <TimelineItem>
                                <p class="time">04:00</p>
                                <p class="content"><span class="fa fa-meh-o fa-3x"></span></p>
                            </TimelineItem>
                            <TimelineItem>
                                <p class="time">09:37</p>
                                <p class="content"><span class="fa fa-smile-o fa-3x"></span></p>
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
            recording: {
                recordingName: '201906300001',
                lenth: '09:40',
                staff: 'John',
                uploadTime: '2019-06-30 15:30'
            }
        };
    },
    methods: {},
    mounted() {}
};
</script>
