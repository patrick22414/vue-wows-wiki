<template>
  <div id="app">
    <Header />
    <GridWrapper />
  </div>
</template>

<script>
  import Header from "./components/Header";
  import GridWrapper from "./components/GridWrapper";

  export default {
    name: "App",
    components: {
      Header,
      GridWrapper,
    },
  };
</script>

<style>
  * {
    margin: 0;
    padding: 0;

    box-sizing: border-box;
  }

  #app {
    font-family: -apple-system, "Segoe UI", "Open Sans", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    max-height: 100vh;
  }
</style>
