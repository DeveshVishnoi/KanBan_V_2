<!-- @format -->

# Kanban-Board 📋

This project is an implementation of a Kanban Board created in Vuejs.

# Local Setup

- Make sure you have the necessary requirements installed and updated, mentioned in the requirements.txt file. If not, just to be sure, go to terminal and run command `pip install -r requirements.txt`.

# Local Development Run

- Simply run `npm install` , it will initiate the node app in development for create `node modules` file
- then run `npm run dev` then your link will be generated



# Folder Structure

- `root` has the `kanaban.sqlite3` DB.
- `application` has the all python files.
- `src` has all the Vue  files in component folder.

```

│   main.py
│   kanaban.sqlite3
│   readme.md
|   models.py
│
|
│
├───application
|        |
|        api.py
|        database.py
|        flask_celery.py
|        jwt_setup.py
|        mail_sent.py
|        models.py
|        task.py
|        worker.py
|
|
|
│
├───src--
|     |__components
        │       add_cards.vue
        │       list_details.vue
        │       user_details.vue
        │       navbar.vue
        │       login.vue
        │       navbar_with_dash.vue
        │       summary.vue
        |       updatecards.vue
        |       updateList.vue
|       APp.vue
│
|      main.js
|      router.js
└───    
      static
      |_______Images
                    all_images
        
```
