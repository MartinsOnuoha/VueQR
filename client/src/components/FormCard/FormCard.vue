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
      url: 'www.genxqrcode.web.app',
      codeColor: '#000000',
      generatedUrl: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAABrElEQVR4nO3aS66DMAwFUEssgCWxdZbEApD8Gn+BZtAndXKr60EL5DCKE5yA6L9iF3p6enp6evoveYlYVLZj0bxmp9m20eN6O9FjAD3FjnRf86gJPagf3T5Swbr+ddkS4KxrC/1v+FdYFoybMh/of8ibCiof5AM9hLe/o57XRfvxTQ/sIwLcfrKNHtd3GMiTM1QHPajvAT6UrHltRLTSA/v3BIibNKZyemDv3b5LrqdUq9ReT5/oPeghfRTYQ+0SS6lWlhn3/KGH8vGUPmrZlEM94njmDz2UV/WndObDdaiLNzznf3ogL5dY+84lUmGfzv/0QN53ucZx73yJxM71JB/okfyFViqIZD7I234mPZa/rp36yZ2Tut9OD+y3LLUzC6Qqb53N5/RgvgqwrU/FZnbJ10/0wF5jqEestxqt97DpIX1HUBvluQsyXX/RA/ns+Ho3nJVZj3xvocf01tm+rZULZL9py9ZnPUYP5ft94rFci+6az+l/yXsCdBU229+mx/RSC+RaY03qc3oob382n+dX0vnlpfo1emQf8VA3So/rPw56enp6enr6L/g/VwbX7IAzwZ4AAAAASUVORK5CYII=',
      loading: false,
    };
  },
  methods: {
    generateColor() {
      this.loading = true;
      let { url } = this;
      const { codeColor } = this;

      if (!url) {
        url = 'www.genxqrcode.web.app';
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
