import User_details from './components/User_details.vue'
import login from './components/login.vue'
import list_details from './components/list_details.vue'
import addcard from './components/addcard.vue'
import update_card from './components/update_card.vue'
import summary from './components/summary.vue'
import Signup from './components/Signup.vue'

import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        name: 'User_details',
        component: User_details,
        path: '/dashboard'
    },
    {
        name: 'login',
        component: login,
        path: '/'
    },
    {
        name: 'list_details',
        component: list_details,
        path: '/edit/list/:id',
    },
    {
        name: 'addcard',
        component: addcard,
        path: '/card/:id',
    },
    {
        name: 'summary',
        component: summary,
        path: '/:id/summary',
    },
    {
        name: 'update_card',
        component: update_card,
        path: '/edit/card/:id/:lid',
    },
    
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router