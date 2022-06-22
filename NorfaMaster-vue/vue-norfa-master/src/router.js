import { createRouter, createWebHashHistory} from 'vue-router';
import Home from './views/Home.vue';
import Registration from './views/Registration.vue';
import Login from './views/Login.vue';
import Services from './views/Services.vue'


export default createRouter({
    history:createWebHashHistory(),
    routes:[
        {path: '/', component: Home},
        {path: '/Registration', component: Registration},
        {path: '/Login', component: Login},
        {path: '/Services', component:Services }
    ]
})