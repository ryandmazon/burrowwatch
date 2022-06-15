export const navigations = [
    {
        name: 'Dashboard',
        path: '/dashboard/default',
        icon: 'dashboard',
    },
    {
        label: 'PAGES',
        type: 'label',
    },
    {
        name: 'Burrow',
        type: 'label',
    },
    {
        name: 'Burrow',
        children: [
            {
                name: 'Discovery',
                path: '/burrow/discover',
            },
            {
                name: 'Tracking',
                path: '/burrow/track',
            }
        ]
    },
]
