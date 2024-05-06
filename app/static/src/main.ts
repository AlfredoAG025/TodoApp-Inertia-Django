import "vite/modulepreload-polyfill";
import {createApp, h} from "vue";
import {createInertiaApp} from "@inertiajs/vue3";
import "./styles.css";
import {Twitter} from "vue-color"

createInertiaApp({
    resolve: (name) => import(`./pages/${name}.vue`),
    setup({el, App, props, plugin}) {
        createApp({render: () => h(App, props)})
            .use(plugin)
            .component('twitter-picker', Twitter)
            .mount(el);
    },
});
