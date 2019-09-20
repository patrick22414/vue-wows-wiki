<template>
  <div class="nations-wrapper">
    <div
      v-for="n in nations"
      v-on:click="selectNation"
      v-bind:key="n.name"
      class="nation-selector"
    >{{ n.fullName }}</div>
  </div>
</template>

<script>
  import dataNations from "../../data/data-nations.json";

  export default {
    data() {
      return {
        nations: dataNations,
      };
    },

    methods: {
      selectNation: function() {
        console.log(this);
      },
    },
  };
</script>

<style lang="less" scoped>
  .nations-wrapper {
    grid-area: nations;

    display: flex;
    flex-flow: column nowrap;

    justify-content: space-around;
    align-items: center;
  }

  .nation-selector {
    width: 60%;
    height: 30px;

    text-align: center;
    line-height: 30px;

    font-weight: 500;
    color: slateblue;

    overflow: hidden;

    box-shadow: 0 3px 0 slateblue;
    transition: box-shadow 0.2s ease;

    &:hover {
      box-shadow: 0 3px 0.01px 5px slateblue;
    }
  }
</style>
