<script setup>
import {QuillEditor} from '@vueup/vue-quill';

import '@vueup/vue-quill/dist/vue-quill.bubble.css';
import {Link, router} from '@inertiajs/vue3';
import {computed, onMounted, reactive, ref} from "vue";
import moment from "moment/moment.js";
import {Icon} from "@iconify/vue";

import "@melloware/coloris/dist/coloris.css";
import Coloris from "@melloware/coloris";

onMounted(() => {
  Coloris.init();
  Coloris(
      {
        el: "#coloris",
        theme: 'polaroid',
        wrap: true,
        swatchesOnly: true,
        format: 'hex',
        swatches: [
          '#264653',
          '#2a9d8f',
          '#e9c46a',
          'rgb(244,162,97)',
          '#e76f51',
          '#d62828',
          'navy',
          '#07b',
          '#0096c7',
          '#00b4d880',
          'rgba(0,119,182,0.8)'
        ],
      });
  Coloris.close();
});

const note = reactive({
  title: "",
  content: "",
  color: "#ffffff",
  timestamp: new Date(),
});

const formattedTimeStamp = computed(() => {
  let dateMoment = moment(note.timestamp);
  return `Today is ${dateMoment.format('dddd, MMMM DD, YYYY')} ${dateMoment.format('LTS')}`
});

function submitNote(event) {
  note.title = note.title.trim();

  router.post('/store_note', note);
}

setInterval(() => {
  note.timestamp = new Date();
}, 1000);

</script>

<template>
  <div class="m-8">
    <div class="mb-4 flex justify-between gap-2">
      <Link href="/notes" class="rounded-full hover:bg-[#D5BC8E]">
        <Icon icon="ep:back" class="w-8 h-8"/>
      </Link>
      <Link href="/notes">
        <Icon icon="solar:menu-dots-bold" class="w-8 h-8"/>
      </Link>
    </div>

    <div class="mb-4 bg-rose-100 py-4 px-10 rounded shadow-md" v-if="Object.keys($page.props.errors).length > 0">
      <div v-for="(value, name, index) in $page.props.errors" class="text-rose-600">
        <strong class="capitalize">{{ name }}</strong>
        <ul v-for="error in value">
          <li>{{ error }}</li>
        </ul>
      </div>
    </div>

    <form @submit.prevent="submitNote" class="flex flex-col gap-4">

      <small class="font-bold">{{ formattedTimeStamp }}</small>
      <input
          class="font-bold text-3xl bg-transparent outline-none"
          placeholder="Title"
          autofocus
          name="title"
          v-model="note.title"
      />
      <QuillEditor
          ref="editor"
          theme="bubble"
          placeholder="content..."
          name="content"
          contentType="html"
          v-model:content="note.content"
      />
      Characteres {{ $refs.editor.content.length}}


      <input type="text"
             id="coloris"
             v-model="note.color"
             name="color"
      />
      <div class="flex justify-center">
        <button class="bg-gray-700 text-white rounded-full font-bold py-2 px-8">Create</button>
      </div>
    </form>
  </div>

</template>

<style scoped>

</style>