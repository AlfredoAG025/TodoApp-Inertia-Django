<script setup>
import {QuillEditor} from '@vueup/vue-quill';

import '@vueup/vue-quill/dist/vue-quill.snow.css';
import {Link, router} from '@inertiajs/vue3';
import {reactive, ref} from "vue";

const props = defineProps({
  errors: Object
});

const note = reactive({
  title: "",
  content: "",
  color: "#ffffff",
  timestamp: new Date(),
});

function submitNote(event) {
  router.post('/store_note', note);
}

</script>

<template>
  <div class="m-8">
    {{ errors }}
    <form @submit.prevent="submitNote" class="flex flex-col gap-4">
      <Link href="/notes">Atras</Link>
      <p>{{ new Date().toDateString() }}</p>
      <input
          class="font-bold text-3xl"
          placeholder="title"
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