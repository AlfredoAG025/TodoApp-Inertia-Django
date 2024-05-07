<script setup>
import {computed, ref, defineProps} from "vue";
import {router} from "@inertiajs/vue3";

const props = defineProps({
  note: {}
});

function deleteNote(id) {
  router.delete(`destroy_note/${id}`)
}

</script>

<template>
  <div class="py-4 px-8 rounded-lg border overflow-hidden w-max-32 shadow bg-white">
    <div class="flex justify-between">
      <h2 class="font-bold">{{ props.note.title }}</h2>
      <div class="w-5 h-5 border rounded-full" :style="{'background-color': props.note.color}"></div>
    </div>
    <p class="">{{ new Date(props.note.timestamp).toLocaleDateString() }}</p>
    <div class="no-tailwindcss">
      <div v-html="props.note.content"></div>
    </div>
    <button @click="deleteNote(props.note.id)">Delete</button>
  </div>
</template>

<style scoped>
</style>