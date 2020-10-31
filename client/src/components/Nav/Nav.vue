<template>
  <nav class="nav bordered__bottom">
    <div class="nav__logo">
      <img width="30" src="/img/fav.png">
      <router-link to="/">Gen.X</router-link>
    </div>
    <ul class="nav__menu">
      <li class="nav__menu-item">
        <router-link to="/" class="nav-link active">
          <i class="material-icons">dashboard</i>
          Home
        </router-link>
      </li>
      <li class="nav__menu-item">
        <router-link to="/my-urls" class="nav-link">
          <i class="material-icons link">link</i>My Urls
        </router-link>
      </li>
      <li class="nav__menu-item">
        <a target="_blank" href="https://webqr.com/" class="nav-link">
          <i class="material-icons">open_in_new</i>Scan Code
        </a>
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
