<template>
  <div class="grid-wrpper">
    <ShipTypeWrapper />
    <NationsWrapper />
  </div>
</template>
<script>
  import NationsWrapper from "./NationsWrapper";
  import ShipTypeWrapper from "./ShipTypeWrapper";

  export default {
    components: {
      NationsWrapper,
      ShipTypeWrapper,
    },
  };
</script>

<style lang="less" scoped>
  .grid-wrpper {
    display: grid;

    grid-template-columns: 240px auto;
    grid-template-rows: 60px auto;
    grid-template-areas:
      "empty    ship-types"
      "nations  content";

    border: solid thick slateblue;
    height: calc(100vh - 120px);
  }
</style>
