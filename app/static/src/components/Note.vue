<script setup>
import {computed, ref, defineProps} from "vue";
import {Link, router} from "@inertiajs/vue3";
import moment from "moment/moment.js";
import anime from "animejs";
import {Icon} from '@iconify/vue';

const props = defineProps({
  note: {
    title: String,
    is_favorite: Boolean,
  }
});

const dateFormatted = computed(() => {
  return moment(props.note.timestamp).format('llll')
});

function toggleFavoriteNote(id) {
  router.patch(`toggle_is_favorite_note/${id}`);

  if (props.note.is_favorite) {
    anime({
      targets: `#note-${id}`,
      translateX: [
        {value: '-10px', duration: 100},
        {value: '10px', duration: 100},
        {value: '-10px', duration: 100},
        {value: '10px', duration: 100},
        {value: '0px', duration: 100}
      ],
      easing: 'easeInOutQuad',
    });
  } else {
    anime({
      targets: `#note-${id}`,
      translateY: [
        {value: '-10px', duration: 100},
        {value: '10px', duration: 100},
        {value: '-10px', duration: 100},
        {value: '10px', duration: 100},
        {value: '0px', duration: 100}
      ],
      easing: 'easeInOutQuad',
    });
  }
}

async function deleteNote(id) {
  try {
    anime({
      targets: `#note-${id}`,
      scale: [1, 0],
      opacity: ['100%', '0%'],
      duration: 300,
      easing: 'easeInOutQuad',
    });

    await new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 400); // 300 milliseconds delay (0.3 seconds)
    });

    await router.delete(`destroy_note/${id}`);

    anime({
      targets: `.note`,
      scale: [0.8, 1.02, 1],
      easing: 'easeInOutQuad',
    });

  } catch (error) {
    console.error("Error deleting note:", error);
  }
}

</script>

<template>
  <div class="note-container">
    <div class="py-4 px-8 rounded-lg overflow-hidden w-max-32 shadow"
         :style="{ 'background-color': props.note.color }">
      <div class=" flex justify-between
    ">
        <h2 class="font-bold">{{ props.note.title }}</h2>
        <div class="w-5 h-5 border-2 border-gray-500 rounded-full"
             :style="{'background-color': props.note.color}"></div>
      </div>
      <small class="">{{ dateFormatted }}</small>
      <div class="h-16 my-8 w-full note-content">
        <div v-html="props.note.content"></div>
        ...
      </div>
      <div class="flex justify-end gap-2">
        <Link href="/edit_note"
              class="bg-white border-2 border-gray-500 shadow-lg flex flex-col items-center justify-center w-8 h-8 rounded-full group hover:bg-gray-200 transition duration-300 ease-in-out"
        >
          <Icon icon="mdi:pencil" class="w-5 h-5 group-hover:text-emerald-500 transition duration-300 ease-in-out"/>
        </Link>
        <button @click="deleteNote(props.note.id)"
                class="bg-white shadow-lg border-2 border-gray-500 flex flex-col items-center justify-center w-8 h-8 rounded-full group hover:bg-gray-200 transition duration-300 ease-in-out">
          <Icon icon="mdi:trash" class="w-5 h-5 group-hover:text-red-700 transition duration-300 ease-in-out"/>
        </button>
        <button @click="toggleFavoriteNote(props.note.id)"
                class="bg-white shadow-lg border-2 border-gray-500 flex flex-col items-center justify-center w-8 h-8 rounded-full group hover:bg-gray-200 transition duration-300 ease-in-out">
          <Icon icon="mdi:heart"
                class="w-5 h-5 transition duration-300 ease-in-out"
                :class="{
            'text-rose-400': props.note.is_favorite,
            'hover:text-rose-400': !props.note.is_favorite,
            'hover:text-gray-700': props.note.is_favorite,
          }"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.note-content {
  white-space: nowrap;
  overflow: hidden;
}

</style>