<template>
    <div class="header">
        <div class="header-container">
            
        <a href="/Home.vue"><img  src="@/assets/NORfA_MASTER.svg" width="307px" height="38px" alt="Logo norfa"></a>
        <ul>
            <li>
                <a href="#">Ваши заказы</a>
            </li>
            <li>
                <a href="#">Поиск заказов</a>
            </li>
            <li>
                <a href="#">Мой профиль</a>
            </li>
            <li>
                <a href="#">Настройка</a>
            </li>
        </ul>
        <div class="sing_in">
        <a href="#/Registration" class="">Зарегистрироваться</a>
        <a href="#/Login" class="">Войти</a>
        </div>
        </div>
    </div>
</template>
<script></script>
<style scoped>
.header{
    background-color: #0073BE;
    font-family: 'Montserrat';
    font-size: 18px;
    color: #FFFFFF;
}
.header-container{
    padding: 23px 25px; 
    width: 1440px;
    margin: 0 auto;
    display: flex;
    align-items: center;
}

ul{
    display: flex;
    justify-content: space-around;
    width: 700px;
}
.sing_in{
    margin-left: auto;
    display: grid;
    height: 50px;
    align-content: space-between;
}
a{
  text-decoration: none;
  color: #ffffff;
}
</style>