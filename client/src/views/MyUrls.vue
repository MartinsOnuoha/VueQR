<template>
  <div class="myUrls">
    <h1>My URLs <i @click="clearUrls" class="material-icons">delete</i></h1>

    <h2 class="error" v-if="urls.length < 1">Nothing to See here</h2>
    <div class="myUrls__url" v-for="(url, i) in urls" :key="i">
      <Url :url="url"></Url>
    </div>
  </div>
</template>

<script>
import { Vue, Options } from 'vue-class-component';
import Url from '@/components/Url/Url.vue';

@Options({
  data() {
    return {
      urls: JSON.parse(localStorage.getItem('urls')) || [],
    };
  },
  components: {
    Url,
  },
  methods: {
    clearUrls() {
      this.urls = [];
      localStorage.setItem('urls', JSON.stringify(this.urls));
    },
  },
})

export default class MyUrls extends Vue {
}
</script>
