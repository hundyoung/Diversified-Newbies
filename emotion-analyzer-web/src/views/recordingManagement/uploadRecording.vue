<template>
    <div>
        <h1>Upload Voice</h1>
        <Divider />
        <Upload multiple type="drag" action="//jsonplaceholder.typicode.com/posts/" :default-file-list="list">
            <div style="padding: 20px 0">
                <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                <p>Click or drag files here to upload</p>
            </div>
        </Upload>
    </div>
</template>
<script>
export default {
    name: 'uploadVoice',
    components: {},
    data() {
        return {
            list: []
        };
    },
    methods: {},
    mounted() {}
};
</script>
