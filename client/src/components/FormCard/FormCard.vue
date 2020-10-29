<template>
  <div class="bordered card">
    <div class="card__img">
      <img width="250" :src="generatedUrl" alt="">
    </div>
    <div class="card__action">
      <div class="card__action-color">
        <div class="color"
          @click="setColor(color)"
          :id="`${color}`"
          v-for="(color, i) in colors"
          :key="i"
          :style="`background-color: ${color}`"
        ></div>
      </div>
      <input v-model="url" placeholder="Enter Your URL" name="" id="" class="" type="text">
      <button
        :disabled="loading || !url"
        @click="generateColor"
      >
        {{ loading? 'Hang on...' : 'Generate' }}
      </button>
      <small>
        <a download :href="generatedUrl">Download</a>
      </small>
    </div>
  </div>
</template>

<script lang="ts">
import './_card.scss';
import { Vue, Options } from 'vue-class-component';

@Options({
  data() {
    return {
      colors: ['#FFA726', '#26C6DA', '#7E57C2', '#66BB6A', '#FF5678'],
      url: 'www.genx.app',
      codeColor: '#000000',
      generatedUrl: '/img/code.png',
      loading: false,
    };
  },
  methods: {
    generateColor() {
      this.loading = true;
      let { url } = this;
      const { codeColor } = this;

      if (!url) {
        url = 'www.genx.app';
      }
      this.$store.dispatch('generateCode', { url, bgColor: '#FFFFFF', codeColor }).then((response: string) => {
        this.generatedUrl = `data:image/png;base64,${response}`;
        this.loading = false;
      });
    },
    setColor(color: string) {
      const elems = document.querySelectorAll('.color');

      [].forEach.call(elems, (el: HTMLDivElement) => {
        el.classList.remove('active-color');
      });

      this.codeColor = color;
      const el: HTMLElement | null = document.getElementById(color);
      if (el) {
        el.classList.add('active-color');
      }
    },
  },
})

export default class FormCard extends Vue {
}
</script>
