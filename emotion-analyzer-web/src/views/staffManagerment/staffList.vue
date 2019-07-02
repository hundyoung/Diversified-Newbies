<template>
    <div>
        <Card>
            <p slot="title">Staff List</p>
            <Table border stripe :columns="columns" :data="tableData" height="520">
                <template slot-scope="{ row }" slot="staffName">
                    <strong>{{ row.staffName }}</strong>
                </template>
                <template slot-scope="{ row }" slot="goodPerformancePercentage">
                    <span> {{ Math.round((row.todayCheerCalls / row.todayCall) * 10000) / 100 }} &nbsp;%</span>
                </template>
                <template slot-scope="{ row }" slot="action">
                    <Button type="primary" size="small" style="margin-right: 5px" @click="view(row)">
                        View Detail
                    </Button>
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
    name: 'Staff',
    components: {},
    data() {
        return {
            columns: [
                {
                    title: 'Staff Name',
                    slot: 'staffName',
                    align: 'center'
                },
                {
                    title: "Today's calls",
                    key: 'todayCall',
                    align: 'center'
                },
                {
                    title: 'Today cheer calls',
                    key: 'todayCheerCalls',
                    align: 'center'
                },
                {
                    title: 'Today upset calls',
                    key: 'todayUpsetCalls',
                    align: 'center'
                },
                {
                    title: 'Good Performance Percentage',
                    slot: 'goodPerformancePercentage',
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
                    staffName: 'John',
                    todayCall: 15,
                    todayCheerCalls: 10,
                    todayUpsetCalls: 5
                },
                {
                    staffName: 'Michael',
                    todayCall: 18,
                    todayCheerCalls: 9,
                    todayUpsetCalls: 9
                },
                {
                    staffName: 'Sam',
                    todayCall: 33,
                    todayCheerCalls: 30,
                    todayUpsetCalls: 3
                },
                {
                    staffName: 'William',
                    todayCall: 25,
                    todayCheerCalls: 11,
                    todayUpsetCalls: 14
                },
                {
                    staffName: 'Dennis',
                    todayCall: 16,
                    todayCheerCalls: 9,
                    todayUpsetCalls: 7
                },
                {
                    staffName: 'James',
                    todayCall: 17,
                    todayCheerCalls: 10,
                    todayUpsetCalls: 7
                },
                {
                    staffName: 'Emma',
                    todayCall: 28,
                    todayCheerCalls: 15,
                    todayUpsetCalls: 13
                },
                {
                    staffName: 'Lucy',
                    todayCall: 13,
                    todayCheerCalls: 7,
                    todayUpsetCalls: 6
                },
                {
                    staffName: 'Lily',
                    todayCall: 17,
                    todayCheerCalls: 2,
                    todayUpsetCalls: 15
                },
                {
                    staffName: 'Kelly',
                    todayCall: 19,
                    todayCheerCalls: 9,
                    todayUpsetCalls: 10
                }
            ]
        };
    },
    methods: {
        view() {
            this.$router.push('staffDetail');
        }
    },
    mounted() {}
};
</script>
