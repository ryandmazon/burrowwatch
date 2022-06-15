import React, { lazy } from 'react';
import Loadable from 'app/components/Loadable/Loadable';
import { authRoles } from '../../auth/authRoles';

const Discover = Loadable(lazy(() => import('./BurrowDiscovery')));
const Track = Loadable(lazy(() => import('./BurrowTracker')));

const burrowRoutes = [
    {
        path: '/burrow/discover',
        element: <Discover />,
        auth: authRoles.admin,
    },
    {
        path: '/burrow/track',
        element: <Track />,
        auth: authRoles.admin,
    }
]

export default burrowRoutes;