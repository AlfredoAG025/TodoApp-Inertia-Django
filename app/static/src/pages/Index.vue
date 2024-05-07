<script setup lang="ts">
import {computed, ref} from "vue";
import { Link } from '@inertiajs/vue3';

defineProps<{
  name: string;
}>();
</script>

<template>
  <div>
    <h1 class="title">Index</h1>
    <Link href="/notes">Notes</Link>
  </div>
</template>

<style scoped>
.title {
  color: green;
}
</style>
