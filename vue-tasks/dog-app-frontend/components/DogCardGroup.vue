<template>
  <!-- Columns of dog cards -->
  <div>

    <!-- Use Bootstrap Vue card group -->
    <b-card-group columns>

      <!-- Use v-for to create 20 cards -->
      <DogCard v-for="index in 20" :key="index" :title="'Dog # ' + index" imgAlt="Dog" text="Dog"></DogCard>
    </b-card-group>
  </div>
</template>

<script>
import DogCard from "./DogCard.vue";

export default {
    components: { DogCard }
}
</script>
