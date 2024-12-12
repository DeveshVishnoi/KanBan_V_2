

<template>
  <div>
    <navbar :username="username"></navbar>
    <div class="containers">
      <!-- {% for task in tasks %} -->

      <div class="box" style=""  v-for="(task, index) in lists" :key="index">
        <div class="dropdown">
          <!-- <a class="active">{{task.title}}</a> -->
          <div class="active">
            {{ task.title }}
            <div id="dropdown-desc">
              <p>
                <button class="dbut">{{ task.desc }}</button>
              </p>
            </div>
          </div>
          <div class="drop">
            <a class="icon" v-on:click="dropdown">
              <i class="fa fa-bars"></i>
            </a>

            <div id="dropdown-content">
              <a 
                ><router-link :to="'/edit/list/' + task.list_id"
                  ><button class="butt"><i class="fa fa-edit"></i>&nbsp;&nbsp;Edit</button></router-link
                ></a
              >
              <a
                
                v-on:click="delete_list(task.list_id)"
                ><button class="butt"><i class="fa fa-trash">&nbsp;&nbsp;Delete</i></button></a
              >
              
              
              <a
                
                v-on:click="export_card(task.list_id)"
                ><button class="butt"><i class="fa fa-compass">&nbsp;&nbsp;Export</i></button></a
              >
            </div>

            <!-- <a href="javascript:void(0);" class="icon" onclick="myFunction()">
              <i class="fa fa-bars"></i>
            </a> -->
          </div>
        </div>
        <div class="scroll">
          <!-- {% for card in cd %} {% if card['list_id'] == task['list_id'] %} -->

          <div
            draggable="true"
            style="max-height: fit-content,display:block;"
            class="card"
            v-for="(card, i) in task.cards"
            :key="i"
          >
            <p class="chead">{{ card["card_title"] }}</p>
            <p style="padding: 10px">{{ card["card_desc"] }}</p>

            
            <br />
            <div class="dead">
              <!-- {% if card['completed'] == 'Complete' %}  v-on:click="delete_card(card.card_id, task.list_id)"
              > -->
              <p
                style="margin-left: 10px gap: 1px"
                class="green"
                v-if="card['completed'] == 'Complete'"
              >
                <i class="fa fa-check" style="color: green"></i>
                {{ card["completed"] }}
              </p>
              <!-- {% else %} -->
              <p
                style="margin-left: 10px; gap: 1px"
                class="red"
                v-if="card['completed'] == 'Incomplete'"
              >
                <!-- <p style="margin-left: 10px" class="red"> -->
                <i class="fa fa-exclamation" style="color: red"></i
                >{{ card["completed"] }}
              </p>
              <!-- {% endif %} -->
              <!-- <span>...........</span> -->

              <p style="gap: 5px" class="comp">
                <i class="fas fa-calendar-alt"></i>{{ card["deadline"] }}
              </p>
            </div>
            
            <span style="font-size: 10px; font-weight: bold; padding: 4px;color:black">
              {{ card["last_seen"] }}
              <span class="allbtn">
                <router-link
                  :to="'/edit/card/' + task.list_id + '/' + card.card_id"
                  ><a>
                    <button style="background-color: #add794" class="del">
                      <!-- d4edda -->
                      <i class="fa fa-edit"></i>
                    </button></a
                  ></router-link
                >
  
  
                <button
                  v-on:click="deltask(card.card_id, task.list_id)"
                  style="background-color: #f5b7b1; border-color: #f5c6cb"
                  class="del"
                >
                  <i class="fa fa-trash"></i>
                  
                </button>
              </span>
            </span>
          </div>
          <!-- {% endif %} {% endfor %} -->
          <div class="addcard">
            <!-- :to="'/card/' + task.list_id" -->
            <router-link :to="'/card/' + task.list_id"
              ><a class=""
                ><button class="add">+ Add Card</button></a
              ></router-link
            >
          </div>
        </div>
      </div>
      <div class="gul" style="align-items: center; padding-left: 60px">
        <button class="dev" style="" v-on:click="addtask()">Add List</button>
      </div>
      <div
        style="

          margin: 0;
          padding: 0;
          display: flex;
          justify-content: center;
          align-items: center;
          min-height: 100vh;
          font-family: 'Jost', sans-serif;
        "
      >
        <div
          class="add_task"
          style="

            width: 350px;
            height: 400px;
            padding: 20px;
            overflow: hidden;
            border-radius: 10px;
            background: #dff9fb;
            box-shadow: 5px 20px 50px rgba(0, 0, 0);
            display: none;
          "
        >
          <h2 style="font-size: 30px">Create A New List....</h2>
          <br /><br />
          <div class="title">
            <div class="forms">
              <label
                style="
                  display: inline-block;
                  max-width: 100%;
                  margin-bottom: 5px;
                  font-weight: 700;
                "
                for="chk"
                aria-hidden="true"
                >Title</label
              ><br />
              <input
                style="
                  position: relative;
                  height: auto;

                  box-sizing: border-box;
                  padding: 10px;
                  font-size: 14px;
                  font-weight: bold;
                  width: 100%;
                  outline: none;
                  border: none;
                  border-radius: 5px;
                "
                type="text"
                v-model="title"
                placeholder="Task Name..."
                maxlength="20"
                required
              />
              <br />
              <br />
              <label style="font-weight: 700" for="chk" aria-hidden="true"
                >Description</label
              ><br />

              <textarea
                style="

                  margin-top: 2px;
                  width: 100%;
                  height: 92px;
                  border-radius: 5px;
                  outline: none;
                  resize: none;
                  font-weight: bold;
                  font-size: 15px;

                  border: none;
                "
                v-model="desc"
                id="t"
                rows=""
                spellcheck="false"
                placeholder="Enter description here......
                "
                maxlength="100"
                required
              >
              </textarea>
              <br />
              <br />

              <button
                style="
                  width: 100%;
                  padding: 5px;
                  border-radius: 5px;
                  background: #573b8a;
                  color: #fff;
                  font-weight: bold;
                  cursor: pointer;
                  /* border: none; */
                  box-shadow: 1px black transparent;
                "
                v-on:click="addlist"
              >
                Add List
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <input type="text"> -->
    <div v-on:change="onChange()" class="sdev" style="display: none">
      <div id="myModal" class="modal fade">
        <div class="modal-dialog modal-confirm">
          <div class="modal-content">
            <div class="modal-header flex-column">
              <i class="fa-light fa-file-xmark"></i>
              <h4 class="modal-title w-100">Are you sure?</h4>
              <br />

              <button
                v-on:click="task(c_id,l_id)"
                type="button"
                class="close"
                data-dismiss="modal"
                aria-hidden="true"
              >
                &times;
              </button>
            </div>
            <div class="modal-body">
              <p>
                Do you really want to delete these records? This process cannot
                be undone.
              </p>
            </div>
            <div class="modal-footer justify-content-center">
              <button
                v-on:click="task(card_id,list_id)"
                type="button"
                class="btn btn-secondary"
                data-dismiss="modal"
              >
                Cancel
              </button>

              <button
                v-on:click="delete_card(cd, ld)"
                type="button"
                class="btn btn-danger"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import  "/src/drag.js";
import navbar from "./navbar.vue";
export default {
  components: {
    navbar,
  },
  name: "User_details",

  data() {
    return {
      email_id: "",
      username: JSON.parse(localStorage.getItem("user_info")).username,
      user_id: JSON.parse(localStorage.getItem("user_info")).user_id,
      password: "",
      title: "",
      desc: "",
      ld:"",
      cd:"",
      lists: {},
      cards: {},
    };
  },
  mounted() {
    this.get_user_details();
  },
  methods: {
    task(c,l) {
      localStorage.removeItem("card_id")
      localStorage.removeItem("task_id")
      if (document.querySelector(".sdev").style.display == "block") {
        document.querySelector(".sdev").style.display = "none";
      } else if (document.querySelector(".sdev").style.display == "none") {
        document.querySelector(".sdev").style.display = "block";
      }
    },
    deltask(id, idd) {
      localStorage.setItem("card_id",id)
      localStorage.setItem("task_id",idd)
      if (document.querySelector(".sdev").style.display == "block") {
        document.querySelector(".sdev").style.display = "none";
      } else if (document.querySelector(".sdev").style.display == "none") {
        document.querySelector(".sdev").style.display = "block";
      }
    },
    addtask() {
      if (document.querySelector(".add_task").style.display == "block") {
        document.querySelector(".add_task").style.display = "none";
      } else if (document.querySelector(".add_task").style.display == "none") {
        document.querySelector(".add_task").style.display = "block";
      }
    },
    onChange() {
        // console.log(event.target.value);
        if (document.querySelector(".sdev").style.display == "block") {
        document.querySelector(".sdev").style.display = "none";
      } else if (document.querySelector(".sdev").style.display == "none") {
        document.querySelector(".sdev").style.display = "block";
      }

    },
    get_user_details() {
      fetch("https://kanban-v-2.onrender.com/api/" + this.user_id, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((res) => {
          (this.email_id = res.email_id),
            (this.username = res.username),
            (this.password = res.password),
            (this.user_id = res.user_id),
            (this.lists = res.lists);
        })
        .catch((err) => this.$router.push({ name: "login" }));
    },

    addlist() {
      fetch("https://kanban-v-2.onrender.com/api/list/" + this.user_id, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-access-token": localStorage.getItem("token"),
        },
        body: JSON.stringify({
          title: this.title,
          desc: this.desc,
        }),
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((data) => {
          console.log(data);
          this.get_user_details();
          // this.$router.push({ name: "User_details" });
        })
        .catch((err) => this.$router.push({ name: "login" }));
    },
    delete_list(id) {
      fetch(`https://kanban-v-2.onrender.com/api/${this.user_id}/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "x-access-token": localStorage.getItem("token"),
        },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((data) => {
          console.log(data);
          this.get_user_details();
        })
        .catch((err) => {
          alert(err);
        });
    },
    delete_card(id, idd) {
      console.log(id, idd);
      id = localStorage.getItem("card_id");
      idd = localStorage.getItem("task_id");
      fetch(`https://kanban-v-2.onrender.com/api/${this.user_id}/${idd}/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "x-access-token": localStorage.getItem("token"),
        },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            // throw new Error();
          }
        })
        .then((data) => {
          console.log(data);
          this.get_user_details();
          document.querySelector(".sdev").style.display = "none";
          // querySelector(".sdev").style.display="none";
        })
        .catch((err) => this.$router.push({ name: "login" }));
    },
    export_card(l) {
      fetch("https://kanban-v-2.onrender.com/api/export/" + this.user_id + "/"+l, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      })
        .then((res) => {
          if (res.ok) {
            return res.blob();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((file) => {
          var a = document.createElement("a");
          a.href = window.URL.createObjectURL(file);
          a.download = `${this.user_id}_card.csv`;
          a.click();
        });
    },
  },
};
</script>

<style>
.modal-confirm {
  color: #636363;
  width: 400px;
}
.del:hover{
  background:red
}
.modal-confirm .modal-content {
  padding: 20px;
  border-radius: 5px;
  border: none;
  text-align: center;
  font-size: 14px;
}
.modal-confirm .modal-header {
  border-bottom: none;
  position: relative;
}
.modal-confirm h4 {
  text-align: center;
  font-size: 26px;
  margin: 30px 0 -10px;
}
.modal-confirm .close {
  position: absolute;
  top: -5px;
  right: -2px;
  width: 26px;
  height: 25px;
}
.modal-confirm .modal-body {
  color: #999;
}
.modal-confirm .modal-footer {
  border: none;
  text-align: center;
  border-radius: 5px;
  font-size: 13px;
  padding: 10px 45px 25px;
}
.modal-confirm .modal-footer a {
  color: #999;
}
.modal-confirm .icon-box {
  width: 80px;
  height: 80px;
  margin: 0 auto;
  border-radius: 50%;
  z-index: 9;
  text-align: center;
  border: 3px solid #f15e5e;
}
.modal-confirm .icon-box i {
  color: #f15e5e;
  font-size: 46px;
  display: inline-block;
  margin-top: 13px;
}
.modal-confirm .btn,
.modal-confirm .btn:active {
  color: #fff;
  border-radius: 4px;
  background: #60c7c1;
  text-decoration: none;
  transition: all 0.4s;
  line-height: normal;
  min-width: 120px;
  border: none;
  min-height: 40px;
  border-radius: 3px;
  margin: 0 5px;
}
.modal-confirm .btn-secondary {
  background: #c1c1c1;
}
.modal-confirm .btn-secondary:hover,
.modal-confirm .btn-secondary:focus {
  background: #a8a8a8;
}
.modal-confirm .btn-danger {
  background: #f15e5e;
}
.modal-confirm .btn-danger:hover,
.modal-confirm .btn-danger:focus {
  background: #ee3535;
}
.trigger-btn {
  display: inline-block;
  margin: 100px auto;
}
.modal {
  align-items: center;
  border: 1px solid #ee3535;
  width: fit-content;
  margin: auto;
  height: 250px;
  padding: 30px;
}
.sdev {
  align-items: center;
  margin-top: -466px;
  position: absolute;
  margin-left: 500px;

  /* align-items: center; */
  text-align: center;
  background: lightyellow;
  /* margin: auto; */
}

.add_task {
  display: none;
}
.top {
  align-items: center;
}
.dropdown {
  overflow: hidden;
  background-color: #eee8f4;
  position: relative;
}
.butt:hover{
  background: #674fa3;
}
.dropdown #dropdown-desc {
  display: none;
}
#dropdown-content {
  display: none;
  transform: scale(0.9);
  transition: transform 1.2s;
}

.dropdown a {
  color: Black;
  padding: 14px 5px;
  text-decoration: none;
  font-size: 17px;
}
.dropdown a.icon {
  display: block;
  position: absolute;
  right: 0;
  top: 0;
  height: 80px;
  width: 160px;
  cursor: pointer;
}
.fa-bars {
  padding-right: 5px;
  float: right;
}
.dropdown a:hover {
  /* background-color: ; */
  color: #333;
}
label {
  color: #333;
}

.active {
  /* background-color: #04aa6d; */
  color: black;
  font-weight: bold;
  padding: 14px 16px;
  font-size: 20px;
}
.drop:hover #dropdown-content {
  display: block;
  transition: transform 1.2s;
}
/*.active:hover #dropdown-desc {
  display: flex;
}  */
.comp {
  display: flex;
  border: 1px solid black;
  width: fit-content;

  background-color: lightgray;
  padding: 5px;
}
.container {
  width: fit-content;
}
.red {
  font-size: 10px;
}
.fa-exclamation {
  margin-right: 5px;
  margin-top: 2px;
}
.fa-check {
  margin-right: 5px;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 250px;
  box-sizing: border-box;
  min-width: 250px;
  /* margin: 20px;  */
  margin: 20px 10px 20px 10px;
  /* text-align: center; */
  font-family: arial;
  
  /* height: 100%; */
  /* min-height: 100px; */
  /* display: flex; */
  background: ;
  /* border: 1px solid blue; */
  border-radius: 10px;
  max-height: fit-content;
  min-height: 120px;
  transition: transform 0.5s;
  cursor: pointer;
}

.card:hover {
  box-sizing: border-box;
  transition: transform 0.5s;
  transform: scale(0.95);
}

.add {
  max-width: 250px;
  min-width: 250px;
  margin: 20px 10px 20px 10px;
  background: white;
  color: black;
  border-radius: 5px;
  height: 40px;
  font-weight: bold;
  font-size: 12px;
  border: none;
  cursor: pointer;
  opacity: 1;
  font-size: 15px;
  transition: transform 1s;
}

a .add:hover {
  background: rgb(150, 150, 223);
  color: white;
  opacity: 1;
  transition: transform 1s;
  transform: scale(0.9);
}
.container {
  margin-top: none;
  /* display: flex; */
  /* gap: 30px; */
}

.title {
  color: grey;
  font-size: 18px;
}

/* button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
} */

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover,
a:hover {
  opacity: 1;
  color:black
}

.box {
  border: 1px solid black;

  height: 100%;
  /* background:#D6EAF8; */
  outline: none;
  border: none;
  min-width: 280px;
  max-width: 280px;
  /* border-spacing: 10px; */
  margin-top: 50px;
  margin-left: 10px;
  min-height: 100px;
  /* margin-right: 20px; */
}
.scroll {
  overflow-y: scroll;
  width: 100%;
  /* min-height: 100px; */
  max-height: 450px;
  border: 1px solid #ccc;
  background: #eee8f4;
  border: none;
  opacity: 1;
}
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-thumb {
  border-radius: 30px;
  border: 1px solid #ccc;
  background-color: #fff;
}

/* Handle */

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #ccc;
}

.box h2 {
  padding-left: 25px;
  /* font-family: ; */
  text-decoration: underline;
}

.card hr {
  margin-top: 0px;
}

/* skacmmaslcsmcmslmslcmclsw */

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 250px;
  min-width: 250px;
  /* margin: 20px;  */
  margin: 20px 10px 20px 10px;
  /* text-align: center; */
  font-family: arial;
  /* height: 100%; */
  /* min-height: 100px; */
  /* display: flex; */
  background: white;
  /* border: 1px solid blue; */
  border-radius: 10px;
  max-height: fit-content;
  min-height: 120px;
}

.add {
  max-width: 250px;
  min-width: 250px;
  margin: 20px 10px 20px 10px;
  background: white;
  color: black;
  border-radius: 5px;
  height: 40px;
  font-weight: bold;
  font-size: 12px;
  /* border:none; */
  cursor: pointer;
  font-size: 15px;
  opacity: 1;
}

.containers {
  /* margin-top: 100px; */
  display: flex;
  gap: 30px;
  background-color: #f7f2f9;
  min-width: 100%;
  max-width: fit-content;
}

.title {
  color: grey;
  font-size: 18px;
}

.gul .dev {
  margin-right: 10px;
  margin-top: 300px;
  /* border: none; */
  height: 40px;
  min-width: 100px;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  padding: 0px;
  flex-direction: row;
  background-color: #674fa3;
  color: white;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
}

.gul .dev:hover {
  opacity: 1;
  background-color: lightgreen;
  color: black;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover,
a:hover {
  opacity: 1;
  color: black;
}

.box {
  border: 1px solid black;

  height: 100%;
  /* background:#D6EAF8; */
  outline: none;
  border: none;
  min-width: 280px;
  max-width: 280px;
  /* border-spacing: 10px; */
  margin-top: 100px;
  margin-left: 10px;
  /* display: flex; */
  /* margin-right: 20px; */
}
/* .scroll{
overflow-y:scroll;
width: 100%;
max-width: 350px;
border: 1px solid #ccc;
background:pink;
border: none;

} */
/* ::-webkit-scrollbar {
width: 8px;
}
::-webkit-scrollbar-thumb {

border-radius: 30px;
border: 1px solid #ccc;
background-color:#fff
} */

/* Handle */

/* Handle on hover */
/* ::-webkit-scrollbar-thumb:hover {
background:#ccc; 
} */

.box h2 {
  padding-left: 25px;
  /* font-family: ; */
  margin-bottom: 20px;
  text-decoration: underline;
}

a.task {
  margin-right: 10px;
  margin-top: 300px;
}

.drop {
  display: flex;
}
.chead {
  /* margin-left:2px; */
  text-align: center;
  margin-right: 4px;
  /* margin-left: 5px; */
  font-weight: bold;
  font-size: 15px;
}

.comp {
  display: flex;
  border: 1px solid black;
  width: fit-content;
  border-radius: 10px;
  background-color: lightgray;

}

.edit {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
  background-color: green;
  /* float: right; */
  margin-top: 15px;
  /* padding: 10px; */
  border-radius: 5px;
  margin-left: 15px;
  opacity:0.8
}
.del {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
  background-color: #42b72a;
  /* float: right; */
  margin-top: 15px;
  /* padding: 10px; */
  border-radius: 5px;
  opacity:0.8
  /* margin-right: 10px; */
}

.dead {
  display: flex;
  gap: 50px;
  font-size: 13px;
  overflow: hidden;
  padding-top: 0px;
  font-weight: bold;
  width: fit-content;
}
.chead {
  /* margin-left:2px; */
  text-align: center;
  margin-right: 4px;
  margin-top: 10px;
  font-weight: bold;
  font-size: 20px;
  font-family: "Times New Roman", Times, sans-serif;
}
.cdesc {
  /* margin-left:2px; */
  text-align: center;
  margin-right: 4px;
  /* margin-left: 5px; */
  font-weight: bold;
  font-size: 10px;
  font-style: serif;
}
.edit {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
  background-color: green;
  /* float: right; */
  margin-top: 15px;
  /* padding: 10px; */
  border-radius: 5px;
  margin-left: 15px;
  opacity:0.8
}

.del {
  background-color: #42b72a;
  border: none;
  cursor: pointer;
  padding: 5px 10px 5px 10px;
  color: black;
  font-weight: bold;
  opacity:0.8;

  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.9);
}
.del:hover {
  background-color: lightgreen;
  color: black;
  font-weight: bold;
}

.alert {
  padding: 10px;
  background-color: #f0ffff;
  color: black;
}

.closebtn {
  margin-left: 15px;
  color: black;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: #0000ff;
}
.butt {
  background-color: white;
  border: none;
  cursor: pointer;
  padding: 5px 10px 5px 10px;
  color: black;
  font-weight: bold;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.9);
}
.butt:hover {
  background-color: rgb(20, 252, 252);
  color: black;
}
.dbut {
  background-color: white;
  border: none;

  font-weight: bold;
  text-align: center;
  padding: 5px 15px 5px 15px;
  color: black;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.9);
}
.allbtn {
  display: inline-flex;
    margin: 1px;
    padding-bottom: 15px;
    padding-left: 26px;
    flex-direction: row;
    flex-wrap: nowrap;
    /* align-items: center; */
    justify-content: center;
    gap: 20px;
    align-items: center;
}  
.green {
  display: flex;
  border: 1px solid black;
  width: fit-content;
  border-radius: 15px;
  background-color: ; 
  padding: 5px;
  font-size: 13px;
  margin-left: 10px;
  background: rgb(173, 221, 173);
}
.red {
  display: flex;
  border: 1px solid black;
  width: fit-content;
  border-radius: 15px;
  background-color: rgb(223, 172, 172);
  padding: 5px;
  font-size: 13px;
  
}
</style>


