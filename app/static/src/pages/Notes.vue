<script setup>
import {ref, defineProps, onMounted} from "vue";
import { Link } from '@inertiajs/vue3';
import Note from "../components/Note.vue";

const props = defineProps({
  notes: Array,
});

onMounted(() => {

});

</script>

<template>
  <div class="m-8 flex flex-col gap-4" style="color: #424856">
    <h1 class="font-bold text-3xl">Notes</h1>
    <Link href="/create_note">Create Note</Link>
    <input
        class="border rounded-full w-full p-1"
        placeholder="Search"
    />
    <div>
      <h2 class="font-bold text-xl">Notes</h2>
      <div v-if="props.notes.length > 0">
        <div class="grid grid-cols-4 gap-4">
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