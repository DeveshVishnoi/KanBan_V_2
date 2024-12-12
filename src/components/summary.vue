<template>
  <div>
    <div class="topnav">
        <a class="nav" >
          Welcome {{username}},
        </a>
  
        <a 
          ><button v-on:click="signout" class="btn success">
            <i class="fa fa-sign-out" style="font-size: 20px gap"></i>Sign Out
          </button></a
        >
        <a 
          ><button v-on:click="dashboard" class="btn info"><i class='fa fa-newspaper-o'></i>&nbsp;Dashboard</button></a
        >
        <a
      ><button class="btnexp exportgreen" v-on:click="export_list">
        <i class="fa fa-compass" style="font-size: 20px gap"></i>Export
      </button></a
    >
      </div>
  
    <div class="summarycontainer">
      <!-- {% for i in range(data|length) %} -->

      <div class="summarybox" v-for="(image,index) in images" :key="index">
        <p
          style="
            margin-top: 2px;
            text-align: center;
            font-size: 25px;
            font-weight: bold;
          "
        >
          {{lists[index].title}}
        </p>
        <div class="sbox">
          <!-- {% set point = 0 -%} {% set point = point + data[i][0] + data[i][1]
                -%} -->
          <p style="padding: 5px;text-align:center; font-weight: bold; color:green">
            Complete : {{all[index][0] }} / {{all[index][0]+all[index][1]}}
          </p>
          <p style="padding: 5px;text-align:center; font-weight: bold; padding-top: 5px; color:blue">
            Incomplete : {{all[index][1]}}  / {{all[index][0]+all[index][1]}}
          </p>
          <p style="padding: 5px; text-align:center;font-weight: bold; padding-top: 5px; color:red">
            Deadline Passed : {{all[index][2]}}  / {{all[index][0]+all[index][1]}}
          </p>
        </div>
        <div style="margin-top: 10px" class="tbox">
          <img style="width: 450px; height: 333px" :src=images[index] >
        </div>
      </div>
      <!-- {% endfor %}D:\21f1002760_2\vue_kanban\vue-project\static -->
    </div>
  </div>
</template>

<script>
import navbar from "./navbar.vue";
export default {
  components: {
    navbar,
  },
  name: "summary",
  data() {
    return {
      images: "",
      all: "",
      lists:"",
      username: JSON.parse(localStorage.getItem("user_info")).username,
      
      user_id: JSON.parse(localStorage.getItem("user_info")).user_id,
    };
  },
  mounted() {
    this.get_user_details(),
    fetch("https://kanban-v-2.onrender.com/api/" +"summary/"+ this.user_id, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      }).
    then(res => {
      if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } 
    }).
    then(data =>{
        this.images = data.images;
        this.all = data.all;
        console.log(Object.keys(this.images).length);
        console.log(Object.keys(this.all));
        this.get_user_details()
    }).catch(err=>this.$router.push({ name: "login" }))
  },
  methods:{
    dashboard(){
        this.$router.push({ name: "User_details" });
    },
    signout(){
        localStorage.clear();
        this.$router.replace({ name: 'login' });
    },
    get_user_details() {
      let result = fetch("https://kanban-v-2.onrender.com/api/" + this.user_id, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      }
     )
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } 
        })
        .then((res) => {
          this.lists = res.lists;
        }).catch(err=>this.$router.push({ name: "login" }));
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
  }
};
</script>

<style>
.summarycontainer {
  padding-top: 100px;
  margin-left: 20px;
  /* background-color:grey */
  display: flex;
  gap: 20px;
  width: fit-content;
}

.summarybox {
  border: 1px solid black;

  height: 500px;
  background: white;
  outline: none;
  min-width: 450px;
  margin-left: 5px;
  padding-right: 10px;
  min-height: 100px;
  border-radius: 3px;
  border: none;
  /* margin-right: 20px; */
}
.sbox {
  width: 400px;
  margin: 10px 25px 10px 25px;
  border: 1px solid blueviolet;
  border-radius: 5px;
  height: 100px;
}
img {
  /* padding: 1px; */
  /* margin-left: 5px; */
  width: 450px;
  height: 300px;
}
.tbox {
  width: 350px;
  /* margin: 10px; */
  height: 300px;
  margin-top: 10px;

  border-radius: 5px;
  overflow: fit-content;
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
.btnexp .exportgreen {
  margin-right: 20px;
  background:yellow
}
</style>