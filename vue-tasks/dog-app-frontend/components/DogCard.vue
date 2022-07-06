<template>
  <!-- Dog card -->
  <div>

    <!-- Use Bootstrap Vue card -->
    <b-card
      :title="title"
      :img-src="imgSrc"
      :img-alt="imgAlt"
      img-top
      tag="article"
      class="dog-card mb-2"
    >
      <b-card-text>
        {{text}}
      </b-card-text>

      <b-button href="#" variant="primary">Go somewhere</b-button>
    </b-card>
  </div>
</template>

<script>
const axios = require("axios").default;

export default {
  data() {
    return {

      // place holder image
      imgSrc: "https://via.placeholder.com/300",
    }
  },
  props: {
    title: String,
    imgAlt: String,
    text: String
  },
  mounted() {
    // used to access data
    var vm = this;

    // make HTTP Get request
    axios
      .get(
        "https://dog.ceo/api/breeds/image/random"
      )
      .then(function (response) {

        // handle success
        // change image to new dog image
        vm.imgSrc = response.data.message;
      })
      .then(function () {});
  },
}
</script>

<style scoped>
.dog-card {
}
</style>
