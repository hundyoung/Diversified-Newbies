<template>
    <div>
        <Card>
            <p slot="title">Staff List</p>
            <Table border stripe :columns="columns" :data="tableData" height="520">
                <template slot-scope="{ row }" slot="staffName">
                    <strong>{{ row.staffName }}</strong>
                </template>
                <template slot-scope="{ row }" slot="goodPerformancePercentage">
                    <span> {{ Math.round((row.todayPositiveCalls / row.todayCall) * 10000) / 100 }} &nbsp;%</span>
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
                    title: 'Today Positive calls',
                    key: 'todayPositiveCalls',
                    align: 'center'
                },
                {
                    title: 'Today Negative calls',
                    key: 'todayNegativeCalls',
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
                    todayPositiveCalls: 10,
                    todayNegativeCalls: 5
                },
                {
                    staffName: 'Michael',
                    todayCall: 18,
                    todayPositiveCalls: 9,
                    todayNegativeCalls: 9
                },
                {
                    staffName: 'Sam',
                    todayCall: 33,
                    todayPositiveCalls: 30,
                    todayNegativeCalls: 3
                },
                {
                    staffName: 'William',
                    todayCall: 25,
                    todayPositiveCalls: 11,
                    todayNegativeCalls: 14
                },
                {
                    staffName: 'Dennis',
                    todayCall: 16,
                    todayPositiveCalls: 9,
                    todayNegativeCalls: 7
                },
                {
                    staffName: 'James',
                    todayCall: 17,
                    todayPositiveCalls: 10,
                    todayNegativeCalls: 7
                },
                {
                    staffName: 'Emma',
                    todayCall: 28,
                    todayPositiveCalls: 15,
                    todayNegativeCalls: 13
                },
                {
                    staffName: 'Lucy',
                    todayCall: 13,
                    todayPositiveCalls: 7,
                    todayNegativeCalls: 6
                },
                {
                    staffName: 'Lily',
                    todayCall: 17,
                    todayPositiveCalls: 2,
                    todayNegativeCalls: 15
                },
                {
                    staffName: 'Kelly',
                    todayCall: 19,
                    todayPositiveCalls: 9,
                    todayNegativeCalls: 10
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
