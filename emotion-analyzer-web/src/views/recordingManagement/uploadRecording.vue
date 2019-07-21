<template>
    <div>
        <Card>
            <p slot="title">Upload Record</p>
            <Form
                label-position="top"
                action="http://116.23.229.30:5000/upload_records"
                method="POST"
                enctype="multipart/form-data"
                ref="uploadForm"
            >
                <Row>
                    <i-col span="6" class="formCol">
                        <FormItem label="Employee ID">
                            <Input v-model="uploadDataObject.employee_id" readonly />
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Customer ID">
                            <Input v-model="uploadDataObject.customer_id" readonly />
                        </FormItem>
                    </i-col>
                    <i-col span="12" class="formCol">
                        <FormItem label="Record Type ">
                            <Select v-model="uploadDataObject.record_type">
                                <Option v-for="item in recordTypeList" :value="item.type_id" :key="item.type_id">
                                    {{ item.type_name }}
                                </Option>
                            </Select>
                        </FormItem>
                    </i-col>
                    <i-col span="24" class="formCol">
                        <input name="file" type="file" id="fileInput" />
                    </i-col>
                    <i-col span="24" class="formCol">
                        <br />
                        <Button type="success" long @click="submit">SUBMIT</Button>
                    </i-col>
                </Row>
            </Form>
        </Card>
    </div>
</template>
<script>
export default {
    name: 'uploadVoice',
    components: {},
    data() {
        return {
            uploadHeader: {
                'Access-Control-Allow-Origin': '*'
            },
            autoCompleteData: [],
            autoCompleteData1: [],
            uploadDataObject: {
                customer_id: '44500001',
                employee_id: '44000001',
                record_type: 1
            },
            file: null,
            list: [],
            recordTypeList: []
        };
    },
    methods: {
        submit() {
            var vm = this;
            let param = new FormData();
            if (document.getElementById('fileInput').value.indexOf('wav') < 0) {
                this.$Message.info('Portal only accept .wav file');
                return;
            }
            param.append('customer_id', this.uploadDataObject.customer_id);
            param.append('employee_id', this.uploadDataObject.employee_id);
            param.append('type', this.uploadDataObject.record_type + '');
            param.append('file', document.getElementById('fileInput').files[0]);
            let config = {
                headers: { 'Content-Type': 'multipart/form-data' }
            };
            this.$Spin.show({
                render: h => {
                    return h('div', [
                        h('Icon', {
                            class: 'demo-spin-icon-load',
                            props: {
                                type: 'ios-loading',
                                size: 18
                            }
                        }),
                        h('div', 'Analyzing')
                    ]);
                }
            });
            this.$ajax
                .post('upload_records', param, config)
                .then(function() {
                    vm.$Spin.hide();
                    vm.$Message.info('Upload completed.');
                    vm.$router.push('RecordingList');
                })
                .catch(function(error) {
                    console.error(error);
                    vm.$Spin.hide();
                    vm.$Message.error('Upload error.');
                });
        }
    },
    mounted() {
        let vm = this;
        this.$ajax
            .get('/add_records')
            .then(function(response) {
                vm.recordTypeList = response.data;
            })
            .catch(function(error) {
                console.log(error);
            });
    }
};
</script>
<style>
.demo-spin-icon-load {
    animation: ani-demo-spin 1s linear infinite;
}
</style>
