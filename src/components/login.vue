<template>
  <div class="dev">
    <div class="span">KanBan</div>
    <br><br>
    <div class="login_container">
      <!--Data or Content-->
      <div class="box-1">
        <div class="content-holder">
          <h2>Hello!</h2>
          <!-- <br> -->
          <!-- <router-link to="/signup"><button>Signup</button></router-link> -->
          <p id="note">
            If you are new user ,<span>Click </span> on a
            <span>Signup </span>button 👇
          </p>
          <button style="color:black"   class="button-1" v-on:click="signuppage()">Sign up</button>
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
            class="input-fields"
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
            class="input-fields"
          />
          <br /><br />
          <input
            type="text"
            v-model="email_id"
            placeholder="Email Id"
            class="input-fields"
          />
          <br /><br />
          <input
            type="text"
            v-model="password"
            placeholder="Password"
            class="input-fields"
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

<script >
export default {
  name: "login",
  data() {
    return {
      username: "",
      email_id: "",
      password: "",
      user_id: "",
    };
  },
  methods: {
    login() {
      //   console.log(new FormData(document.querySelector("#login").entries));
      if (this.email_id == "" || this.password == "") {
        // this.$router.push({ name: "login" });
        alert("bhai sari information toh de");
      } else {
        fetch("http://127.0.0.1:5000/api/Login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email_id: this.email_id,
            password: this.password,
          }),
        })
          .then((res) => res.json())
          .then((data) => {
           
            if (data.message == "email_id or password not match") {
              alert("email_id or password not match");
            } else if (data.message == "No user exists") {
              alert("No user exists");
            } else {
               console.log(data.message);
              localStorage.setItem("user_info", JSON.stringify(data));
              localStorage.setItem("token", data.token);
              // localStorage.setItem("user_id", data.user_id);
              this.$router.push({ name: "User_details" });
            }
          })
          .catch("galat hai behenchdo");
      }
    },
    signup() {
      if (this.username != "" && this.email_id != "" && this.password != "") {
        fetch("http://127.0.0.1:5000/api/Register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.username,
            email_id: this.email_id,
            password: this.password,
          }),
        })
          .then((res) => {
            if (res.status === 404) {
              return res.json();
            }
            if (!res.ok) {
              throw new error("something wromng from server");
            }
            return res.json();
          })
          .then((data) => {
            if (data["message"] == "sale dusplicate maal bhejta") {
              alert("This Email_id is also used, pls try different email_id");
            }

            console.log(data);
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_info",  JSON.stringify(data));
            this.$router.push({ name: "User_details" });
          });
      } else {
        alert("pls give all information!!");
        // we will handle for all case
      }
    },
    signuppage() {
      document.querySelector(".login-form-container").style.cssText =
        "display: none;";
      document.querySelector(".signup-form-container").style.cssText =
        "display: block;";
      document.querySelector("#note").innerHTML =
        "if you are already register <span>click </span> on a <span>Sigin </span> button 👇";

      document.querySelector(".login_container").style.cssText =
        "background: linear-gradient(to bottom, rgb(56, 189, 149),  rgb(28, 139, 106));";
      document.querySelector(".button-1").style.cssText = "display: none";
      document.querySelector(".button-2").style.cssText = "display: block";
    },

    loginpage() {
      document.querySelector(".signup-form-container").style.cssText =
        "display: none;";
      document.querySelector(".login-form-container").style.cssText =
        "display: block;";
      document.querySelector("#note").innerHTML =
        " if you are new user <span>click </span> on <span>signup </span>button 👇";
      document.querySelector(".login_container").style.cssText =
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
.span{
  text-align: center;
  font-size: 5.5em;
  justify-content: center;
  color:rgb(56, 102, 189);
  font-weight: bold;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  background: #f7f2f9;
}

.dev .login_container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  background-color: red;
  background: linear-gradient(to bottom, rgb(6, 108, 100), rgb(14, 48, 122));
  width: 800px;
  height: 400px;
  margin: auto;
  border-radius: 5px;
}
.button-1{
  color: black;
}
span {
  font-size: 15px;
  color: rgb(255, 230, 0);
}

.dev .content-holder {
  text-align: center;
  color: white;
  font-size: 14px;
  font-weight: lighter;
  letter-spacing: 2px;
  margin-top: 15%;
  padding: 50px;
}

.dev .content-holder h2 {
  font-size: 34px;
  margin: 20px auto;
}

.dev .content-holder p {
  margin: 30px auto;
}

.dev .content-holder button {
  border: none;
  font-size: 15px;
  padding: 10px;
  border-radius: 6px;
  background-color: white;
  width: 150px;
  margin: 20px auto;
  cursor: pointer;
}

.dev .box-2 {
  background-color: white;

  margin: 5px;
}

.dev .login-form-container {
  text-align: center;
  margin-top: 10%;
}

.dev .login-form-container h1 {
  color: black;
  font-size: 24px;
  padding: 20px;
}

.dev .input-fields {
  box-sizing: border-box;
  font-size: 14px;
  padding: 10px;
  border-radius: 7px;
  border: 1px solid rgb(168, 168, 168);
  width: 250px;
  outline: none;
}

.dev .login-button {
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
  color:black
}

.dev .button-2 {
  display: none;
  cursor: pointer;
  color:black
}

.dev .signup-form-container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -60%);
  text-align: center;
  display: none;
}

.dev .signup-form-container h1 {
  color: black;
  font-size: 24px;
  padding: 20px;
}

.dev .signup-button {
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