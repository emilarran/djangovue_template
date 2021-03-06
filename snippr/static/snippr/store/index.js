import Vue from 'vue';
import Vuex from 'vuex';
import auth from 'source/store/auth';

Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
        auth
    }
});

export default store;
