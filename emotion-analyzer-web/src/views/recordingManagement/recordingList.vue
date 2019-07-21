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
            <Table border stripe :columns="columns" :data="tableData" height="520" :loading="tableLoading">
                <template slot-scope="{ row }" slot="record_name">
                    <strong>{{ row.record_name }}</strong>
                </template>
                <template slot-scope="{ row }" slot="overall_evaluation">
                    <Rate disabled v-model="row.overall_evaluation" />
                </template>
                <template slot-scope="{ row }" slot="action">
                    <Button type="primary" size="small" style="margin-right: 5px" @click="view(row)">View</Button>
                    <Button type="error" size="small" @click="remove(row)">Delete</Button>
                </template>
            </Table>
            <br />
            <div style="text-align:right">
                <Page :total="allData.length" :page-size="pageSize" show-elevator @on-change="changePage" />
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
            pageSize: 10,
            allData: [],
            tableLoading: false,
            columns: [
                {
                    title: 'Recording Name',
                    slot: 'record_name',
                    align: 'center',
                    width: 200
                },
                {
                    title: 'Employee ID',
                    key: 'employee_id',
                    align: 'center',
                    width: 120
                },
                {
                    title: 'overall evaluation',
                    slot: 'overall_evaluation',
                    align: 'center'
                },
                {
                    title: 'Record Date',
                    key: 'record_date',
                    align: 'center',
                    width: 200
                },
                {
                    title: 'Record ID',
                    key: 'record_id',
                    align: 'center',
                    width: 120
                },
                {
                    title: 'Customer ID',
                    key: 'customer_id',
                    align: 'center',
                    width: 120
                },
                {
                    title: 'Action',
                    slot: 'action',
                    width: 150,
                    align: 'center'
                }
            ],
            tableData: []
        };
    },
    methods: {
        toUpload() {
            this.$router.push('uploadRecording');
        },
        view(row) {
            this.$router.push({
                path: 'RecordingDetail',
                query: {
                    record_id: row.record_id
                }
            });
        },
        changePage(page) {
            let vm = this;
            this.tableLoading = true;
            this.tableData = [];
            let begin = (page - 1) * this.pageSize;
            let end = this.pageSize * (page - 1) + 10;
            if (end > this.allData.length) {
                end = this.allData.length;
            }
            for (let i = begin; i < end; i++) {
                this.tableData.push(this.allData[i]);
            }
            vm.$nextTick(function() {
                vm.tableLoading = false;
            });
        },
        remove() {}
    },
    mounted() {
        let vm = this;
        vm.tableLoading = true;
        this.$ajax
            .get('/audio_records')
            .then(function(response) {
                vm.allData = response.data;
                for (let i = 0; i < vm.allData.length; i++) {
                    vm.allData[i].overall_evaluation = vm.allData[i].overall_evaluation
                        ? vm.allData[i].overall_evaluation + 2
                        : 3;
                }
                vm.tableData = [];
                for (let i = 0; i < vm.pageSize; i++) {
                    vm.tableData.push(vm.allData[i]);
                }
                vm.tableLoading = false;
            })
            .catch(function(error) {
                vm.tableLoading = false;
                console.log(error);
            });
    }
};
</script>
