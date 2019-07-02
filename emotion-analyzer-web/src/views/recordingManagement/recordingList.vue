<template>
    <div>
        <Card>
            <p slot="title">Recording List</p>
            <Form label-position="top">
                <Row>
                    <i-col span="6" class="formCol">
                        <FormItem label="Recording Name">
                            <Input v-model="searchObject.recordingName" placeholder="Search Recording Name"></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Staff Name">
                            <Input v-model="searchObject.staffName" placeholder="Search Staff Name"></Input>
                        </FormItem>
                    </i-col>
                    <i-col span="4" class="formCol">
                        <FormItem label="Date">
                            <DatePicker
                                type="daterange"
                                placement="bottom-end"
                                placeholder="Select date range"
                            ></DatePicker>
                        </FormItem>
                    </i-col>
                    <i-col span="8" class="formCol">
                        <FormItem label="Action">
                            <Button type="success">Search</Button>
                            &nbsp;&nbsp;
                            <Button type="warning" @click="toUpload">Upload Recording</Button>
                        </FormItem>
                    </i-col>
                </Row>
            </Form>
            <Divider orientation="left" size="small">Data table</Divider>
            <Table border stripe :columns="columns" :data="tableData" height="520">
                <template slot-scope="{ row }" slot="recordingName">
                    <strong>{{ row.recordingName }}</strong>
                </template>
                <template slot-scope="{ row }" slot="action">
                    <Button type="primary" size="small" style="margin-right: 5px" @click="view(row)">View</Button>
                    <Button type="error" size="small" @click="remove(row)">Delete</Button>
                </template>
            </Table>
            <br />
            <div style="text-align:right">
                <Page :total="100" show-elevator />
            </div>
        </Card>
        <br />
    </div>
</template>
<script>
export default {
    name: 'recordingList',
    components: {},
    data() {
        return {
            searchObject: {},
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
                    title: 'Staff',
                    key: 'staff',
                    align: 'center'
                },
                {
                    title: 'Upload Time',
                    key: 'uploadTime',
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
                    staff: 'John',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300002',
                    lenth: '09:24',
                    staff: 'Michael',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300004',
                    lenth: '08:33',
                    staff: 'Sam',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100004',
                    lenth: '08:20',
                    staff: 'Sam',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100134',
                    lenth: '06:30',
                    staff: 'Emma',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300001',
                    lenth: '12:30',
                    staff: 'John',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300002',
                    lenth: '09:24',
                    staff: 'Michael',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '201906300004',
                    lenth: '08:33',
                    staff: 'Sam',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100004',
                    lenth: '08:20',
                    staff: 'Sam',
                    uploadTime: '2019-06-30 15:30'
                },
                {
                    recordingName: '2019070100134',
                    lenth: '06:30',
                    staff: 'Emma',
                    uploadTime: '2019-06-30 15:30'
                }
            ]
        };
    },
    methods: {
        toUpload() {
            this.$router.push('uploadRecording');
        },
        view() {
            this.$router.push('RecordingDetail');
        },
        remove() {}
    },
    mounted() {}
};
</script>
