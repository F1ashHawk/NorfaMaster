<template>
    <div class="home-page-start">
        <h2>Найдем специалистов<br> для любой задачи</h2>
        <div class="home-button-block">
        <a href="#/Registration" class="home-registration-button">Зарегистрироваться</a>
        <a href="#/Login" class="home-login-button">Войти</a>
        </div>
    </div>
</template>
<style>
h2 {
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 600;
    font-size: 50px;
    line-height: 127.4%;
    color: #1A2A2F;
}

.home-page-start {
    display: grid;
    align-content: center;
    margin-left: auto;
    background-image: url('@/assets/Home-backgroundjpg.jpg');
    background-repeat: no-repeat;
    height: 834px;
    width: 1356px;

}


.home-button-block{
    margin-top: 65px;
    display: grid;
    width: 369px;
    height: 152px;
    align-content: space-between;
    align-items: center;
}
.home-registration-button {
    font-family: 'Montserrat';
    text-align: center;
    color: #faf7f7;
    font-size: 23px;
    line-height: 102%;
    display: flex;
    justify-content: center;
    align-items: center;
    letter-spacing: 0.18em;
    width: 396px;
    height: 67px;
    background: #0CC0EE;
    border: 1px solid #5ECCE9;
    border-radius: 33px;
    transition: .5s;
}
.home-registration-button:hover{
    background-color: #0073BE;
}

.home-login-button{
    font-family: 'Montserrat';
    text-align: center;
    color: #faf7f7;
    font-size: 23px;
    line-height: 102%;
    display: flex;
    justify-content: center;
    align-items: center;
    letter-spacing: 0.18em;
    width: 238px;
    height: 67px;
    background: #0CC0EE;
    border: 1px solid #5ECCE9;
    border-radius: 33px;
    transition: .5s;
}
.home-login-button:hover{
    background-color: #0073BE;
}
</style>
