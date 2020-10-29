<template>
  <div class="home">
    <div class="home__left">
      <img width="" class="home__left-hero" src="/img/boxman.svg">
      <h1>Generate Unique QRCodes for your <span>URLs</span></h1>
    </div>
    <div class="home__right">
      <FormCard></FormCard>
    </div>
  </div>
</template>

<script lang="ts">
import '@/assets/scss/_home.scss';
import { Options, Vue } from 'vue-class-component';
import FormCard from '@/components/FormCard/FormCard.vue';

@Options({
  components: {
    FormCard,
  },
})
export default class Home extends Vue {

}
</script>
