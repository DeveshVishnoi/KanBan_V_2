<template>
    <div class="dev">
      <div class="container">
        <!--Data or Content-->
        <div class="box-1">
          <div class="content-holder">
            <h2>Hello!</h2>
  
            <button class="button-1" v-on:click="signuppage()">Sign up</button>
            <button class="button-2" v-on:click="loginpage()">Sign In</button>
          </div>
        </div>
  
        <!--Forms-->
        <div class="box-2">
          <div class="login-form-container">
            <h1>Sign In Form</h1>
            <input
              type="text"
              v-model="email_id"
              placeholder="Enter Email Id"
              class="input-field"
            />
            <br /><br />
            <input
              type="text"
              v-model="password"
              placeholder="Password"
              class="input-field"
            />
            <br /><br />
            <button class="login-button" v-on:click="login" type="button">
              Sign In
            </button>
          </div>
  
          <!--Create Container for Signup form-->
          <div class="signup-form-container">
            <h1>Sign Up Form</h1>
            <input
              type="text"
              v-model="username"
              placeholder="Username"
              class="input-field"
            />
            <br /><br />
            <input
              type="text"
              v-model="email_id"
              placeholder="Email Id"
              class="input-field"
            />
            <br /><br />
            <input
              type="text"
              v-model="password"
              placeholder="Password"
              class="input-field"
            />
            <br /><br />
            <button class="signup-button" v-on:click="signup" type="button">
              Sign Up
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Signup",
    data() {
      return {
        email_id: "",
        password: "",
        user_id: "",
      };
    },
    methods: {
      login() {
        //   console.log(new FormData(document.querySelector("#login").entries));
        if (this.email_id == "") {
          this.$router.push({ name: "login" });
        }
        fetch("https://kanban-v-2-mb2w.onrender.com/api/Login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email_id: this.email_id,
            password: this.password,
          }),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            localStorage.setItem("user_id", data.user_id);
            this.$router.push({ name: "User_details" });
          })
          .catch("galat hai behenchdo");
      },
      signuppage() {
        document.querySelector(".login-form-container").style.cssText =
          "display: none;";
        document.querySelector(".signup-form-container").style.cssText =
          "display: block;";
        document.querySelector(".container").style.cssText =
          "background: linear-gradient(to bottom, rgb(56, 189, 149),  rgb(28, 139, 106));";
        document.querySelector(".button-1").style.cssText = "display: none";
        document.querySelector(".button-2").style.cssText = "display: block";
      },
  
      loginpage() {
        document.querySelector(".signup-form-container").style.cssText =
          "display: none;";
        document.querySelector(".login-form-container").style.cssText =
          "display: block;";
        document.querySelector(".container").style.cssText =
          "background: linear-gradient(to bottom, rgb(6, 108, 224),  rgb(14, 48, 122));";
        document.querySelector(".button-2").style.cssText = "display: none";
        document.querySelector(".button-1").style.cssText = "display: block";
      },
    },
  };
  </script>
  
  <style>
  * {
    margin: 0px;
    padding: 0px;
    
    
  }
  
  body {
    font-family: Arial, Helvetica, sans-serif;
   
    
  }
  #dev{
    background: aqua;
  }
  
  .container {
    display: grid;
    grid-template-columns: 1fr 2fr;
    background-color: red;
    background: linear-gradient(to bottom, rgb(6, 108, 100), rgb(14, 48, 122));
    width: 800px;
    height: 400px;
    margin: 10% auto;
    border-radius: 5px;
    
    
  }
  
  .content-holder {
    text-align: center;
    color: white;
    font-size: 14px;
    font-weight: lighter;
    letter-spacing: 2px;
    margin-top: 15%;
    padding: 50px;
  }
  
  .content-holder h2 {
    font-size: 34px;
    margin: 20px auto;
  }
  
  .content-holder p {
    margin: 30px auto;
  }
  
  .content-holder button {
    border: none;
    font-size: 15px;
    padding: 10px;
    border-radius: 6px;
    background-color: white;
    width: 150px;
    margin: 20px auto;
    cursor: pointer;
   
  }
  
  .box-2 {
    background-color: white;
  
    margin: 5px;
  }
  
  .login-form-container {
    text-align: center;
    margin-top: 10%;
  }
  
  .login-form-container h1 {
    color: black;
    font-size: 24px;
    padding: 20px;
  }
  
  .input-field {
    box-sizing: border-box;
    font-size: 14px;
    padding: 10px;
    border-radius: 7px;
    border: 1px solid rgb(168, 168, 168);
    width: 250px;
    outline: none;
  }
  
  .login-button {
    box-sizing: border-box;
    color: white;
    font-size: 14px;
    padding: 13px;
    border-radius: 7px;
    border: none;
    width: 250px;
    outline: none;
    background-color: rgb(56, 102, 189);
    cursor: pointer;
    
  }
  
  .button-2 {
    display: none;
    cursor: pointer;
    
  }
  
  .signup-form-container {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -60%);
    text-align: center;
    display: none;
  }
  
  .signup-form-container h1 {
    color: black;
    font-size: 24px;
    padding: 20px;
  }
  
  .signup-button {
    box-sizing: border-box;
    color: white;
    font-size: 14px;
    padding: 13px;
    border-radius: 7px;
    border: none;
    width: 250px;
    outline: none;
    cursor: pointer;
    background-color: rgb(56, 189, 149);
   
  }
  </style>