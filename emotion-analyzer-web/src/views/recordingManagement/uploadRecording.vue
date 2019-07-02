<template>
    <div>
        <Card>
            <p slot="title">Upload Record</p>
            <Form label-position="top">
                <Row>
                    <i-col span="6" class="formCol">
                        <FormItem label="Customer Id">
                            <AutoComplete
                                v-model="uploadDataObject.customer_id"
                                :data="autoCompleteData"
                                @on-search="autoCompleteDataOnSearch"
                                placeholder="Search Customer ID"
                            ></AutoComplete>
                        </FormItem>
                    </i-col>
                    <i-col span="6" class="formCol">
                        <FormItem label="Employee Id">
                            <AutoComplete
                                v-model="uploadDataObject.employee_id"
                                :data="autoCompleteData1"
                                @on-search="autoCompleteDataOnSearch1"
                                placeholder="Search Customer ID"
                            ></AutoComplete>
                        </FormItem>
                    </i-col>
                    <i-col span="12" class="formCol">
                        <FormItem label="Record Type ">
                            <Select v-model="uploadDataObject.record_type">
                                <Option v-for="item in recordTypeList" :value="item.name" :key="item.name">
                                    {{ item.name }}
                                </Option>
                            </Select>
                        </FormItem>
                    </i-col>
                    <i-col span="24" class="formCol">
                        <FormItem label="Record File ">
                            <Upload
                                ref="uploadCom"
                                type="drag"
                                action="//jsonplaceholder.typicode.com/posts/"
                                :before-upload="beforeUpload"
                                :data="uploadDataObject"
                                :on-success="handleSuccess"
                                :on-error="handleError"
                            >
                                <div style="padding: 20px 0">
                                    <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                                    <p>Click or drag files here to upload</p>
                                </div>
                            </Upload>
                        </FormItem>
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
            autoCompleteData: [],
            autoCompleteData1: [],
            uploadDataObject: {
                customer_id: '',
                employee_id: '',
                record_type: ''
            },
            file: null,
            list: [],
            recordTypeList: [
                { name: 'Insurance' },
                { name: 'Investment' },
                { name: 'Credit card' },
                { name: 'Consultation' },
                { name: 'Complaint' }
            ]
        };
    },
    methods: {
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
                this.$Message.error('You must select Record Type');
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
    mounted() {}
};
</script>
