<template>
  <div class="grid-wrpper">
    <NationsWrapper></NationsWrapper>
  </div>
</template>
<script>
  import NationsWrapper from "./NationsWrapper";
  export default {
    components: {
      NationsWrapper
    }
  };
</script>

<style lang="less" scoped>
  .grid-wrpper {
    display: grid;

    grid-template-columns: 180px auto;
    grid-template-rows: 120px auto;
    grid-template-areas:
      "empty    ship-types"
      "nations  content";

    border: solid thick slateblue;
    height: calc(100vh - 120px);
  }
</style>
