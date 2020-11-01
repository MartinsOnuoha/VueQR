<template>
  <div class="url">
    <div class="url__img">
      <img :src="`data:image/png;base64,${url.base64}`" alt="url_image">
    </div>
    <div class="url__link">
      <h2>{{ truncate(url.url) }}</h2>
      <a :href="`data:image/png;base64,${url.base64}`" download>download</a>
    </div>
    <!-- <div class="url__actions">
    </div> -->
  </div>
</template>

<script lang="ts">
import './_url.scss';
import { Vue, Options } from 'vue-class-component';

@Options({
  props: {
    url: Object,
  },
  methods: {
    truncate(text: string): string {
      if (text.length > 26) {
        return `${text.substr(0, 26)}...`;
      }
      return text;
    },
  },
})

export default class Url extends Vue {
}
</script>
