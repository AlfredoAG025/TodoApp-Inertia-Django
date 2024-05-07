<script setup>
import {QuillEditor} from '@vueup/vue-quill';

import '@vueup/vue-quill/dist/vue-quill.snow.css';
import {Link, router} from '@inertiajs/vue3';
import {computed, reactive, ref} from "vue";
import moment from "moment/moment.js";
import {Icon} from "@iconify/vue";

const props = defineProps({
  errors: Object
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
    {{ errors }}
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
          theme="snow"
          placeholder="content..."
          name="content"
          contentType="html"
          v-model:content="note.content"
      />
      <input
          type="color"
          v-model="note.color"
          name="color"
      />
      <button>Create</button>
    </form>
  </div>

</template>

<style scoped>

</style>