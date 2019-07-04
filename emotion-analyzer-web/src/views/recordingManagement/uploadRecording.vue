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
                        <FormItem label="Employee Id">
                            <Input v-model="uploadDataObject.employee_id" readonly />
                            <!-- <AutoComplete
                                v-model="uploadDataObject.customer_id"
                                :data="autoCompleteData"
                                @on-search="autoCompleteDataOnSearch"
                                placeholder="Search Customer ID"
                            ></AutoComplete> -->
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Record Id">
                            <Input v-model="uploadDataObject.customer_id" readonly />
                            <!-- <AutoComplete
                                v-model="uploadDataObject.employee_id"
                                :data="autoCompleteData1"
                                @on-search="autoCompleteDataOnSearch1"
                                placeholder="Search Customer ID"
                            ></AutoComplete> -->
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
                        <!-- <FormItem label="Record File ">
                            <Upload
                                ref="uploadCom"
                                type="drag"
                                action="//jsonplaceholder.typicode.com/posts/"
                                :before-upload="beforeUpload"
                                :data="uploadDataObject"
                                :on-success="handleSuccess"
                                :on-error="handleError"
                                :format="['wav']"
                                :headers="uploadHeader"
                            >
                                <div style="padding: 20px 0">
                                    <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                                    <p>Click or drag files here to upload</p>
                                </div>
                            </Upload>
                        </FormItem> -->
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
        },
        autoCompleteDataOnSearch(value) {
            if (!value) {
                this.autoCompleteData = [];
            } else if (value.length < 8) {
                this.autoCompleteData = [];
                let length = 8 - value.length;
                for (let i = 0; i < 5; i++) {
                    let numberNew = value + '';
                    for (let j = 0; j < length; j++) {
                        numberNew += Math.floor(Math.random() * 10) + '';
                    }
                    this.autoCompleteData.push(numberNew);
                }
            }
        },
        autoCompleteDataOnSearch1(value) {
            if (!value) {
                this.autoCompleteData1 = [];
            } else if (value.length < 8) {
                this.autoCompleteData1 = [];
                let length = 8 - value.length;
                for (let i = 0; i < 5; i++) {
                    let numberNew = value + '';
                    for (let j = 0; j < length; j++) {
                        numberNew += Math.floor(Math.random() * 10) + '';
                    }
                    this.autoCompleteData1.push(numberNew);
                }
            }
        },
        beforeUpload(file) {
            this.file = file;
            if (file.name.indexOf('wav') < 0) {
                this.$Message.error('The portal only accept "wav" file');
                this.$refs.uploadCom.clearFiles();
                return false;
            }
            if (this.uploadDataObject.customer_id === '') {
                this.$Message.error('You must input Customer Id');
                this.$refs.uploadCom.clearFiles();
                return false;
            }
            if (this.uploadDataObject.employee_id === '') {
                this.$Message.error('You must input Employee Id');
                this.$refs.uploadCom.clearFiles();
                return false;
            }
            if (this.uploadDataObject.record_type === '') {
                this.$Message.error('You must select recording Type');
                this.$refs.uploadCom.clearFiles();
                return false;
            }
            this.$Spin.show();
        },
        handleSuccess() {
            this.$Spin.hide();
            this.$Message.info('Upload completed.');
            this.$router.push('RecordingList');
        },
        handleError() {
            this.$refs.uploadCom.clearFiles();
            this.$Spin.hide();
            this.$Message.error('Upload error.');
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