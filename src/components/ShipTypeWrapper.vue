<template>
  <div class="ship-type-wrapper">
    <div class="ship-type-selector" v-for="t in shipTypes" v-bind:key="t">{{t}}</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        shipTypes: ["Aircraft Carriers", "Battleships", "Crusiers", "Destroyers"],
      };
    },
  };
</script>

<style lang="less" scoped>
  .ship-type-wrapper {
    grid-area: ship-types;

    display: flex;
    flex-flow: row nowrap;

    justify-content: space-around;
    align-items: center;

    padding: 8px;
  }

  .ship-type-selector {
    width: 15%;
    height: 100%;

    font-weight: 500;
    color: slateblue;
    text-align: center;
    line-height: 48px;

    box-shadow: 0 3px 0px slateblue;

    transition: box-shadow 0.2s ease;
    overflow: hidden;

    &:hover {
      box-shadow: 0 3px 0.01px 5px slateblue;
    }
  }
</style>