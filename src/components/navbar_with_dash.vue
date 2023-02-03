<template>
    <div class="topnav">
      <a class="nav" >
        Welcome {{username}},
      </a>
  
      <a
        ><button class="btn success" v-on:click="signout">
          <i class="fa fa-sign-out" style="font-size: 20px gap"></i>Sign Out
        </button></a
      >
      
        <a><button  v-on:click="dashboard" class="btn info"><i class="fa fa-bar-chart" style="font-size: 20px gap"></i>Dashboard</button></a>
      <a
        ><button class="btnexp exportgreen" v-on:click="export_list" >
          <i class="fa fa-compass" style="font-size: 20px  gap:33px"></i>Export
        </button></a
      >
    </div>
  </template>
  <script>
  export default {
    name: "navbar_with_dash",
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
      get_user_details(){
        fetch("http://127.0.0.1:5000/api/" + this.user_id,{
          method: "GET",
          headers: {'x-access-token':localStorage.getItem("token")}
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
        });
        
      },
      dashboard(){
        this.$router.push({ name: "User_details" });
      },
      export_list() {
      fetch("http://127.0.0.1:5000/api/export/" + this.user_id, {
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
    mounted(){
      this.get_user_details();
    }
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
 
  .topnav {
    background-color: #333;
    overflow: hidden;
    /* box-sizing: border-box; */
    position: fixed;
    width: 100%;
    margin-bottom: none;
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
    background:red
  }
  .btnexp .exportgreen {
    margin-right: 20px;
    background:rgb(50, 228, 50)
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
  .exportgreen {
    border-color:yellow;
    color: black;
    margin-right: 10px;
  }
  .exportgreen:hover {
    background-color: yellow;
    color: black;
    opacity: 1;
  }
  
  </style>