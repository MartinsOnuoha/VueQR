import { createStore } from 'vuex';
import arrayOfObject from '../types/arrayOfObjects';
import config from '../config/url';

export default createStore({
  state: {
    urls: arrayOfObject,
  },
  mutations: {
    SAVEURL(state, payload: object) {
      state.urls.push(payload);
      localStorage.setItem('urls', JSON.stringify(state.urls));
    },
  },
  actions: {
    generateCode({ commit }, payload: object) {
      return fetch(`${config.serverUrl}/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      })
        .then((response) => response.json())
        .then((data) => {
          commit('SAVEURL', data.data);
          return data.data.base64;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
  },
  modules: {
  },
});
