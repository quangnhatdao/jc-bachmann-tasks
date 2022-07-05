<template>
  <div>
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
      imgSrc: "https://via.placeholder.com/300",
    }
  },
  props: {
    title: String,
    imgAlt: String,
    text: String
  },
  mounted() {
    var vm = this;

    axios
      .get(
        "https://dog.ceo/api/breeds/image/random"
      )
      .then(function (response) {
        console.log(response.data);
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
