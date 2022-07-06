<template>
  <div>
    <!-- Cards, revealed if button is clicked -->
    <DogCardGroup v-if="showDogs"></DogCardGroup>

    <!-- Button, hidden when clicked -->
    <div v-if="!showDogs" class="d-flex justify-content-center align-items-center vw-100 vh-100">
      <b-button variant="primary" @click="showDogs = true">Dogs!</b-button>
    </div>
  </div>
</template>

<script>
import DogCardGroup from "~/components/DogCardGroup.vue";
export default {
  components: { DogCardGroup },
  data() {
    return {

      // state for revealing/hiding cards and button
      showDogs: false,
    }
  },
};
</script>
