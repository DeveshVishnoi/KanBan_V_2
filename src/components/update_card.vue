<template>
  <!-- @format -->

  <div>
    <navbar_dash :username="username"></navbar_dash>
    <div class="container_for_card">
      <div class="row">
        <div class="col-md-12">
          <div class="form">
            <h1>Update Card</h1>

            <fieldset>
              <label class="required-field" for="lname">List Names:</label>
              <select v-model="ln" v-on:change="onChange($event)" class="input" id="lname">
                <!-- {% for i in ld %} -->
                <option
                  v-for="(list, index) in lists"
                  :key="index"
                  :value="list.list_id"
                >
                  {{ list.title }}
                </option>
              </select>

              <label class="required-field" for="cname">Card Name:</label>
              <input
                type="text"
                id="cname"
                class="input"
                v-model="card_name"
                placeholder="Card Name..."
                maxlength="50"
                required
              />

              <label class="required-field" for="deadline">Deadline:</label>
              <input
                type="date"
                :min="currentdate"
                class="input"
                id="deadline"
                v-model="date"
                required
              />

              <label for="cdesc">Card Description:</label>
              <textarea
                id="cdesc"
                class="input"
                v-model="card_desc"
                placeholder="Write something..."
                style="height: 100px"
                maxlength="100"
                required
              ></textarea>

              <label class="required-field">Status</label>
              <input type="radio" value="1" v-model="status" required /><label
                class="light"
                >Incomplete</label
              ><br />
              <input type="radio" value="2" v-model="status" required /><label
                class="light"
                >Complete</label
              ><br />
            </fieldset>
            <br />

            <button class="submit_btn" v-on:click="updatecard">Update Card</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar_dash from "./navbar_with_dash.vue";
export default {
  name: "update_card",
  components: {
    navbar_dash,
  },
  data() {
    return {
      username: JSON.parse(localStorage.getItem("user_info")).username,
      email_id: "",
      user_id: JSON.parse(localStorage.getItem("user_info")).user_id,
      list_id: this.$route.params.id,
      list_name: "",
      card_name: "",
      card_desc: "",
      date: "",
      status: "",
      lists: {},
      card_id: this.$route.params.lid,
      ln:"",
      currentdate:new Date().toJSON().slice(0,10)
    
    };
  },
  methods: {
    get_user_details() {
      let result = fetch("https://kanban-v-2.onrender.com/api/" + this.user_id, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      }
       )
        .then((res) => {if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } })
        .then((res) => {
          this.lists = res.lists;
        }).catch(err=>this.$router.push({ name: "login" }));
    },
    onChange(event) {
        console.log(event.target.value);
        // this.ln = event.target.value;

        
    },
    updatecard() {
      

      fetch("https://kanban-v-2.onrender.com/api/" + this.user_id + "/" + this.list_id + "/" + this.card_id, {
        method: "PUT",
        headers: { "Content-Type": "application/json" ,"x-access-token": localStorage.getItem("token")},
        body: JSON.stringify({
          list_id: this.ln,
          card_title: this.card_name,
          card_desc: this.card_desc,
          deadline : this.date,
          completed: this.status
        })
        
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } })
        .then((data) => {
            
          console.log(data);
          // (this.list_id = data.list_id),
          // (this.card_name = data.card_title);
          // (this.card_desc = data.card_desc);
          // (this.date = data.deadline);
          // (this.status = data.completed);
          // this.get_user_details() 
          this.$router.push({ name: "User_details" });
        }).catch(err=>this.$router.push({ name: "login" }));
        
      },
  },
  mounted() {
    this.get_user_details();
    fetch(
    `https://kanban-v-2.onrender.com/api/${this.user_id}/${this.list_id}/${this.card_id}`,
    {
        method: "GET",
        headers: { "Content-Type": "application/json","x-access-token": localStorage.getItem("token")},
    }
    )
    .then((res) => {
      if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } 
    })
    .then((data) => {
        (this.card_name = data.card_title),
        (this.card_desc = data.card_desc),
        (this.date = data.deadline),
        (this.status = data.completed),
        console.log(this.list_name);
    }).catch(err=>this.$router.push({ name: "login" }));
  },
};
</script>

<style>
.container_for_card {
  margin-left: 100px;

  padding: 100px;
}

body {
  margin: 0;
  /* overflow-y: hidden; */
}
.topnav {
  background-color: #333;
  overflow: hidden;
  /* box-sizing: border-box; */
  position: fixed;
  width: 100%;
  margin-bottom: none;
  margin: auto;
}

.topnav .nav {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 24px 16px;
  text-decoration: none;
  font-size: 27px;
  /* word-spacing: 10px; */
  font-style: fantasy;
}
.topnav a.split {
  float: right;
  /* background-color: #04AA6D; */
  color: white;
}

/* #######################for button ########################## */

.btn {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 14px 14px;
  font-size: 16px;
  cursor: pointer;
  float: right;
  margin-top: 15px;
  /* padding: 10px; */
  border-radius: 5px;
  /* margin-right: 10px; */
}
.btn .success {
  margin-right: 20px;
}

.info {
  border-color: #2196f3;
  color: dodgerblue;
  margin-right: 10px;
}

.info:hover {
  background: blue;
  color: white;
}
.success:hover {
  background-color: red;
  color: white;
}
.success {
  border-color: red;
  color: red;
  margin-right: 10px;
}

.card_container {
  /* margin-top: 100px; */
  padding: 100px;
}

*,
*:before,
*:after {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

body {
  font-family: "Nunito", sans-serif;
  color: #384047;
  overflow: scroll;
}

.rwa form {
  max-width: 300px;
  margin: 10px auto;
  padding: 10px 20px;
  background: #f4f7f8;
  border-radius: 8px;
}

h1 {
  margin: 0 0 30px 0;
  text-align: center;
}

.input,
select {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  font-size: 16px;
  height: auto;
  margin: 0;
  outline: 0;
  padding: 15px;
  width: 100%;
  background-color: #e8eeef;
  color: black;
  font-weight: 17px;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03) inset;
  margin-bottom: 30px;
  resize: none;
  /*border: 1px solid blue */
}

input[type="radio"] {
  margin: 0 4px 8px 0;
  font-weight: 17px;
}
input {
  border: 0.4px solid blue;
}

select {
  padding: 6px;
  height: 32px;
  border-radius: 2px;
}

.submit_btn {
  padding: 9px 20px 9px 20px;
  color: #fff;
  background-color: rgb(88, 208, 88);
  font-size: 18px;
  text-align: center;
  font-style: normal;
  border-radius: 5px;
  width: 100%;
  border: 1px solid black;
  border-width: 1px 1px 3px;
  box-shadow: 0 -1px 0 rgba(255, 255, 255, 0.1) inset;
  margin-bottom: 10px;
  cursor: pointer;
}

.submit_btn:hover {
  background-color: rgb(127, 191, 212);
  color: black;
  font-weight: bold;
  opacity: 1;
}

fieldset {
  /* margin-bottom: 30px; */
  border: none;
}

legend {
  font-size: 1.4em;
  margin-bottom: 10px;
}

label {
  display: block;
  /* margin-bottom: 8px; */
  font-weight: bold;
}

label.light {
  font-weight: 17px;
  display: inline;
}

.number {
  background-color: #5fcf80;
  color: #fff;
  height: 30px;
  width: 30px;
  display: inline-block;
  font-size: 0.8em;
  margin-right: 4px;
  line-height: 30px;
  text-align: center;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.2);
  border-radius: 100%;
}
.required-field::after {
  content: "*";
  color: red;
}
.form {
  max-width: 500px;
  margin: 10px auto;
  padding: 10px 20px;
  background: #cde4ec;
  border-radius: 8px;
}

@media screen and (min-width: 480px) {
  form {
    max-width: 480px;
  }
}
</style>