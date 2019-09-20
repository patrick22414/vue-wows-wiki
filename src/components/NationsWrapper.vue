<template>
  <div class="nations-wrapper">
    <div v-for="n in nations" :key="n.name" class="nation-selector">{{ n.fullName }}</div>
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

    box-shadow: 0 3px 0 slateblue;

    text-align: center;
    line-height: 30px;

    font-weight: 500;
    color: slateblue;

    transition: box-shadow 0.2s ease;
    overflow: hidden;

    &:hover {
      box-shadow: 0 3px 0 5px slateblue;
    }
  }
</style>
