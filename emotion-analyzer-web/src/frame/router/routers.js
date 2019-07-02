import Main from '_views/mian';

export default [
    {
        path: '/',
        name: 'Main',
        component: Main,
        children: [
            {
                path: '/dashboard',
                name: 'dashboard',
                icon: '',
                component: () => import('_views/dashboard/dashboard.vue')
            }
        ]
    },
    {
        path: '/RecordingManagement',
        name: 'RecordingManagement',
        title: 'Recording Management',
        displayInMenu: true,
        component: Main,
        children: [
            {
                path: '/RecordingList',
                name: 'RecordingList',
                title: 'Recording List',
                displayInMenu: true,
                component: () => import('_views/recordingManagement/recordingList.vue')
            },
            {
                path: '/RecordingDetail',
                name: 'RecordingDetail',
                title: 'Recording Detail',
                component: () => import('_views/recordingManagement/recordingDetail.vue')
            },
            {
                path: '/uploadRecording',
                name: 'uploadRecording',
                title: 'Upload Recording',
                component: () => import('_views/recordingManagement/uploadRecording.vue')
            }
        ]
    },
    {
        path: '/staffManagement',
        name: 'staffManagement',
        title: 'Staff Management',
        displayInMenu: true,
        component: Main,
        children: [
            {
                path: '/staffList',
                name: 'staffList',
                title: 'Staff List',
                displayInMenu: true,
                component: () => import('_views/staffManagerment/staffList.vue')
            },
            {
                path: '/staffDetail',
                name: 'staffDetail',
                title: 'Staff Detail',
                component: () => import('_views/staffManagerment/staffDetail.vue')
            }
        ]
    }
];
