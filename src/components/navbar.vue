<template>
  <div class="topnav">
    <a class="nav"> KanBan: {{ username }}, </a>

    <a
      ><button class="btn success" v-on:click="signout">
        <i class="fa fa-sign-out" style="font-size: 20px gap"></i>Sign Out
      </button></a
    >
    <router-link :to="this.user_id + '/summary'"
      ><a
        ><button class="btn info">
          <i
            class="fa fa-bar-chart"
            aria-hidden="true"
            style="font-size: 20px"
          ></i
          >Summary
        </button></a
      ></router-link
    >
    <a
      ><button class="btnexp exportgreen" v-on:click="export_list">
        <i class="fa fa-compass" style="font-size: 20px gap:33px"></i>Export
      </button></a
    >
  </div>
</template>
<script>
export default {
  name: "navbar",
  props: ["username"],
  data() {
    return {
      email_id: "",
      username: JSON.parse(localStorage.getItem("user_info")).username,
      user_id: JSON.parse(localStorage.getItem("user_info")).user_id,
      password: "",
      title: "",
      desc: "",
      lists: {},
      cards: {},
    };
  },

  methods: {
    signout() {
      localStorage.clear();
      this.$router.replace({ name: "login" });
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
          
            
        });
    },
    export_list() {
      fetch("https://kanban-v-2.onrender.com/api/export/" + this.user_id, {
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
          a.download = `${this.user_id}_list.csv`;
          a.click();
        });
    },
  },
  mounted() {
    this.get_user_details();
  },
};
</script>
<style>
body {
  margin: 0;
  overflow-y: hidden;
}
i.fa.fa-bar-chart {
  margin-right: 6px;
}
i.fa.fa-compass {
  margin-right: 6px;
}

.exportgreen:hover {
  opacity: 1;
}
.exportgreen {
  margin-right: 10px;
}
.btnexp {
  border: 2px solid yellow;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  float: right;
  margin-top: 15px;
  /* padding: 10px; */
  border-radius: 5px;
  /* margin-right: 10px; */
}

.btnexp:hover {
  color: black;
}
.topnav {
  background-color: #333;
  overflow: hidden;
  /* box-sizing: border-box; */
  position: fixed;
  width: 100%;
  margin-bottom: none;
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
  font-weight: bold;
}
.topnav a.split {
  float: right;
  /* background-color: #04AA6D; */
  color: white;
}
.topnav .nav:hover {
  color: yellow;
  opacity: 1;
}

/* #######################for button ########################## */

.btn {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 14px 28px;
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
  background: #2196f3;
  color: white;
}

.required-field::after {
  content: "*";
  color: red;
}
.info {
  border-color: #2196f3;
  color: dodgerblue;
  margin-right: 10px;
}

.info:hover {
  background: blue;
  color: white;
  opacity: 2;
}
.success:hover {
  background-color: red;
  color: white;
  opacity: 1;
}
.success {
  border-color: red;
  color: red;
  margin-right: 10px;
}
</style>