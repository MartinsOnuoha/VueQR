<template>
  <nav class="nav bordered__bottom">
    <div class="nav__logo">
      <img width="30" src="/img/code.png">
      <router-link to="/">Gen.X</router-link>
    </div>
    <ul class="nav__menu">
      <li class="nav__menu-item">
        <router-link to="/" class="nav-link active" href="#">
          <i class="material-icons">dashboard</i>
          Home
        </router-link>
      </li>
      <li class="nav__menu-item">
        <router-link to="/my-urls" class="nav-link" href="#">
          <i class="material-icons link">link</i>My Urls
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
import './_nav.scss';
import { Vue } from 'vue-class-component';

export default class Nav extends Vue {

}
</script>
