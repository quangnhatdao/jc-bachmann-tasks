<template>
  <div>
    <b-card-group columns>
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
