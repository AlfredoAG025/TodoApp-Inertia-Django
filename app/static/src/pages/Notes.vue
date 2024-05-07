<script setup>
import {ref, defineProps, onMounted} from "vue";
import {Link} from '@inertiajs/vue3';
import Note from "../components/Note.vue";
import { Icon } from '@iconify/vue';

const props = defineProps({
  notes: Array,
});

onMounted(() => {

});

</script>

<template>
  <div class="m-8 flex flex-col gap-4" style="color: #424856">
    <h1 class="font-bold text-3xl">Notes</h1>
    <Link href="/create_note" class="fixed bottom-8 right-8 w-10 h-10 bg-[#424856] rounded-full shadow shadow-[#424856]">
      <Icon icon="mdi-light:plus" class="w-10 h-10 text-white"/>
    </Link>
    <div class="flex items-center border rounded-full px-4 py-2 gap-2 bg-white">
      <Icon icon="material-symbols:search" class="w-8 h-8"/>
      <input
        class="w-full outline-none bg-transparent"
        placeholder="Search"
      />
    </div>

    <div class="flex flex-col gap-2">
      <h2 class="font-bold text-xl">Notes</h2>
      <div v-if="props.notes.length > 0">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          <Note :note="note" v-for="note in props.notes"/>
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