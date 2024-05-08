<script setup>
import {ref, defineProps, onMounted} from "vue";
import {Link} from '@inertiajs/vue3';
import Note from "../components/Note.vue";
import {Icon} from '@iconify/vue';
import anime from 'animejs/lib/anime.es.js';

const isShrinkBtnCreate = ref(false);

const shrinkButton = () => {
  anime({
    targets: '#btnCreate',
    width: ['40px', '100px'],
    easing: 'easeInOutQuad',
    duration: 300
  });

  anime({
    targets: 'span',
    hidden: [false, true],
    easing: 'easeInOutQuad',
    duration: 300
  });
};

const shrinkButton2 = () => {
  anime({
    targets: '#btnCreate',
    width: ['100px', '40px'],
    easing: 'easeInOutQuad',
    duration: 300
  });

  anime({
    targets: 'span',
    hidden: [true, false],
    easing: 'easeInOutQuad',
    duration: 300
  });
};

const props = defineProps({
  notes: Array,
  favorite_notes: Array,
});

onMounted(() => {
  anime({
    targets: '.note',
    scale: [0.8, 1.02, 1],
    easing: 'easeInOutQuad',
  });
});

</script>

<template>
  <div class="m-8 flex flex-col gap-4" style="color: #424856">
    <h1 class="font-bold text-3xl flex items-center gap-2"><Icon icon="material-symbols:note"/> Notes</h1>

    <Link
          @mouseleave="shrinkButton2"
          @mouseenter="shrinkButton"
          id="btnCreate"
          href="/create_note"
          class="flex items-center overflow-hidden z-10 fixed bottom-8 right-8 w-10 h-10 bg-[#424856] rounded-md shadow shadow-[#424856]">
      <Icon icon="mdi-light:plus" class="w-10 h-10 text-white"/>
      <span id="create-text" class="text-white" hidden>Create</span>
    </Link>

    <div class="flex items-center border rounded-full px-4 py-2 gap-2 bg-white">
      <Icon icon="material-symbols:search" class="w-8 h-8"/>
      <input
          class="w-full outline-none bg-transparent"
          placeholder="Search"
      />
    </div>

    <div class="flex flex-col gap-2">
      <h2 class="font-bold text-xl flex items-center gap-2"><Icon icon="mdi:heart"/> Favorite Notes</h2>
      <div v-if="props.favorite_notes.length > 0">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          <Note :id="`favorite-note-${note.id}`" class="note" :key="note.id" :note="note" v-for="note in props.favorite_notes"/>
        </div>
      </div>
      <div v-else>
        <p>You don't have any favorite notes.</p>
      </div>
    </div>

    <div class="flex flex-col gap-2">
      <h2 class="font-bold text-xl flex items-center gap-2"><Icon icon="material-symbols:note"/> My Notes</h2>
      <div v-if="props.notes.length > 0">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          <Note :id="`note-${note.id}`" class="note" :key="note.id" :note="note" v-for="note in props.notes"/>
        </div>
      </div>
      <div v-else>
        <p>You don't have any notes.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>