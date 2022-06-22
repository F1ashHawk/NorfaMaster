<template>
    <div class="container">
        <div class="input-box">
            <input type="text" name="" id="">
            <input type="button" value="Filters">
            <input type="submit" value="Искать">
        </div>
        <div class="results-items">
            <h3>Найдено результатов:</h3>
            <CardServiceSesult/>
            <CardServiceSesult/>
            <CardServiceSesult/>
            <CardServiceSesult/>
        </div>
    </div>
</template>

<script>
import CardServiceSesult from '@/components/CardServiceResult.vue'

export default {
  name: 'App',
  components: {
    CardServiceSesult
  }
}
</script>