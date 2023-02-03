<template>
  <!-- creating nav bar  -->
  <div>
    <navbar_dash :username="this.username"></navbar_dash>
    <div
      style="
        margin: 0;
        padding: 20px;
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
          display: block;
        "
      >
        <h2 style="font-size: 30px">Update A List....</h2>
        <br /><br />
        <div class="title">
          <div class="forms">
            <label
              class="required-field"
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
              
              placeholder="Task Name..."
              
              maxlength="20"
              v-model="task"
              required
            />
            <br />
            <br />
            <label
              class="required-field"
              style="font-weight: 700"
              for="chk"
              aria-hidden="true"
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
              v-model="description"
              id="t"
              rows=""
              spellcheck="false"
              placeholder="Enter description here......
                  "
              maxlength="50"
              required
            >
            </textarea
            >
            <br />
            <br />

            <!-- <input
                  type="submit"
                  class="btn btn-dark"
                  value="Create"
                  style="position: absolute; left: 200px"
                /> -->
            <a 
              ><button
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
                v-on:click="updatelist"
              >
                Update List
              </button></a
            >
            </div>

          <!-- <button class="addbtn">Add Task</button> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar_dash from "./navbar_with_dash.vue";
export default {
  components: {
    navbar_dash,
  },
  name: "list_details",
  data() {
    return {
      username: JSON.parse(localStorage.getItem("user_info")).username,
      user_id: JSON.parse(localStorage.getItem("user_info")).user_id,
      lists:{},
      list_id:this.$route.params.id,
      task: "",
      description: "",
      cards: {},

    };
  },
   mounted() {
        // fetch("")
        fetch(`http://127.0.0.1:5000/api/${this.user_id}/${this.list_id}` , {
            method: "GET",
            headers:{"Content-Type": "application/json",
            "x-access-token": localStorage.getItem("token")
            }
        }).then(res=> res.json())
        .then(data=> {
            this.task = data.title;
            console.log(this.list_name);
        })
  },
  
  
  methods: {
    updatelist() {
      console.log(this.list_id); 
      console.log(this.user_id); 
      fetch("http://127.0.0.1:5000/api/" + this.user_id + "/" + this.list_id ,{
        method:"PUT",
        headers:{"Content-Type":"application/json",
        "x-access-token": localStorage.getItem("token")
        },
        body:JSON.stringify({
          title:this.task,
          desc:this.description,
        })
      }).then(res => {if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          } })
      .then(data => {
        this.title = data.title,
        this.desc = data.desc
        this.$router.push({ name: "User_details" });
      });


    },
    dashboard(){
        this.$router.push({ name: "User_details" });
    }
  },
};
</script>

<style>

</style>