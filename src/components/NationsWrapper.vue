<template>
  <div class="nations-wrapper">
    <div v-for="n in nations" :key="n.name" class="nation-selector">{{ n.full_name }}</div>
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

    justify-content: space-between;
    align-items: center;
    padding: 60px 0;
  }

  .nation-selector {
    width: 80%;
    height: 40px;

    border-radius: 20px;
    box-shadow: 0 3px 9px rgba(0, 0, 0, 0.1);

    text-align: center;
    line-height: 40px;

    font-weight: 500;
    color: slateblue;

    transition: box-shadow 1s;

    &:hover {
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
  }
</style>
