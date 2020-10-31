import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from '../views/Home.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  { path: '/:pathMatch(.*)*', name: 'not-found', redirect: '/' },
  {
    path: '/my-urls',
    name: 'MyUrls',
    component: () => import('../views/MyUrls.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
