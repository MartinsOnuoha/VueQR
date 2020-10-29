<template>
  <Nav />
  <router-view/>
</template>

<script>
import '@/assets/scss/_app.scss';
import '@/assets/scss/_mobile.scss';
import { Vue, Options } from 'vue-class-component';
import Nav from './components/Nav/Nav.vue';

@Options({
  components: {
    Nav,
  },
})

export default class App extends Vue {
}
</script>

<style lang="scss">
  #app {font-family: 'VT323', monospace;}
</style>
