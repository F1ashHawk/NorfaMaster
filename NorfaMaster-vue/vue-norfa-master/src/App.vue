<template>
<div id="app">
  <IndexHeader/>
  <router-view/>
  </div>
</template>

<script>
import IndexHeader from '@/components/IndexHeader'

export default {
  name: 'App',
  components: {
    IndexHeader
  }
}
</script>

<style>
*,*::after,*::before{
  margin: 0;
  box-sizing: border-box;
  text-decoration: none;
  list-style: none;
  transition: .5s;
}
a{
  text-decoration: none;
  color: #ffffff;
}

#app {
    @font-face {
      font-family: 'Montserrat', sans-serif;
      src: url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
    }
    @font-face {
      font-family:  'Roboto', sans-serif;;
      src: url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    }

  }

</style>
