<template>
  <div class="nations-wrapper">
    <div class="nation-selector" v-for="n in nations" v-bind:key="n.name">{{n.fullName}}</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        nations: [
          { name: "usa", fullName: "U.S.A." },
          { name: "japan", fullName: "Japan" },
          { name: "uk", fullName: "U.K." },
          { name: "france", fullName: "France" },
          { name: "germany", fullName: "Germany" },
          { name: "ussr", fullName: "U.S.S.R." },
          { name: "panasia", fullName: "Pan-Asia" },
          { name: "paneurope", fullName: "Pan-Europe" },
          { name: "panamerica", fullName: "Pan-America" }
        ]
      };
    }
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
