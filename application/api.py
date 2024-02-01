from flask_restful import Resource,reqparse,marshal, Api,fields, marshal_with, abort
from flask_caching import Cache
from flask import current_app as app,jsonify,send_from_directory
# from application.fieldsandparser import *
from application.models import *
from datetime import datetime as dt
from application import tasks
import matplotlib
from application.jwt_setup import token_required
import matplotlib.pyplot as plt


matplotlib.use('Agg')
import jwt
import json
import time
from datetime import datetime


app.config["CACHE_TYPE"] = "RedisCache"
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"  
app.config['CACHE_DEFAULT_TIMEOUT'] = 30
cache= Cache(app)

api = Api(app)



card_fields = {
    "list_id" : fields.Integer,
    "card_id" : fields.Integer,
    "card_title" : fields.String,
    "card_desc" : fields.String,
    "deadline" :fields.String,
    "completed" :fields.String,
    "last_seen" :fields.String,
    "user_id" : fields.Integer,
}
list_fields = {
    "list_id" : fields.Integer,
    "title" : fields.String,
    "desc" : fields.String,
    "user_id" : fields.Integer,
    # "password" : fields.String,
    "cards" : fields.List(fields.Nested(card_fields)),
    
}

# for User
user_fields = {
    "user_id" : fields.Integer,
    "username" : fields.String,
    "email_id" : fields.String,
    "password" : fields.String,
    "lists" : fields.List(fields.Nested(list_fields))
}
 
create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email_id')
create_user_parser.add_argument('password')

# for list

create_list_parser = reqparse.RequestParser()
create_list_parser.add_argument('title')
create_list_parser.add_argument('desc')

# for cards

create_card_parser = reqparse.RequestParser()
create_card_parser.add_argument('card_title')
create_card_parser.add_argument('card_desc')
create_card_parser.add_argument('deadline')
create_card_parser.add_argument('completed')
# create_card_parser.add_argument('completed')
# create_card_parser.add_argument('user_id')
# create_card_parser.add_argument('list_id')

update_card_parser = reqparse.RequestParser()
update_card_parser.add_argument('list_id')
update_card_parser.add_argument('card_title')
update_card_parser.add_argument('card_desc')
update_card_parser.add_argument('deadline')
update_card_parser.add_argument('completed')

days =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
months = [1,2,3,4,5,6,7,8,9,10,11,12]

@app.route("/hello", methods=["GET","POST"])
def hello():
    now=datetime.now()
    print("now_in_flask = ", now)
    dt_string= now.strftime("%d/%m/%y %H:%M:%S")
    print("date and time ", dt_string)
    job = tasks.print_current_time.apply_async(countdown=10)
    result=job.wait()
    return str(result), 200

###########   Caching check  ###############
     
@app.route('/eheboy')
@cache.cached(timeout=50)
def testingcache():
    time.sleep(10)
    return "le beta hogya cache"


# =======================================================================================================
# ====================================================================================
class Login(Resource):
    def post(self):
        # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        args = create_user_parser.parse_args()
        print(args)
        # username = args.get("username" ,None)
        email_id = args.get("email_id" ,None)
        password = args.get("password" ,None)

        # if username is None: 
        #     return {
        #         "message" : "pls give username"
        #     } , 404

        if email_id is None:
            return {
                "message" : "pls give email_id also"
            } , 404
            
        if password is None:
           return {
                "message" : "pls give password also"
            } ,404     

        user = User.query.filter(User.email_id == email_id).first()
        if user:
            if(user.password == password):
                u_id = user.user_id
                return jsonify({
                    "username":user.username,
                    "email":user.email_id,
                    "password":user.password,
                    "user_id":u_id,
                    "token" : jwt.encode({"email":
                    user.email_id, "iat": time.time(),"exp":time.time()+1800}, app.config['SECRET_KEY'])
  


                })
            else:
                abort(404, message="email_id or password not match")    

        else:
            abort(404, message="No user exists")
        # newuser = User(username = username, email_id = email_id, password=password)
        # db.session.add(newuser)
        # db.session.commit()
        # return marshal(newuser,user_fields)




class Register(Resource):
    def post(self):
        
            # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        args = create_user_parser.parse_args()
        username = args.get("username" ,None)
        email_id = args.get("email_id" ,None)
        password = args.get("password" ,None)

        if username is None: 
            abort(404, message="pls give username")

        if email_id is None:
            abort(404, message="pls give email_id")
            
        if password is None:
            abort(404, message="pls give correct password")

        user = User.query.filter(User.email_id == email_id).first()
        if user:
            abort(404, message="sale dusplicate maal bhejta")  

        
        newuser = User(username = username, email_id = email_id, password=password)
        db.session.add(newuser)
        db.session.commit()
        return {
            "username":newuser.username,
            "email":newuser.email_id,
            "password":newuser.password,
            "user_id":newuser.user_id,
            "token" : jwt.encode({"email":
             newuser.email_id, "iat": time.time(),"exp":time.time()+1800}, app.config['SECRET_KEY'])
        }


# @token_required
@app.route('/api/export/<int:user_idd>', methods=['GET'])
def export_list(user_idd):
    user = User.query.filter_by(user_id=user_idd).first()
    with open(f'csvs/{user_idd}_list.csv', 'w') as list_csv:
        list_csv.write("SNo,List_Name,List_Description\n")
        for i in range(len(user.lists)):

            list = user.lists[i]
            print(list)
            list_csv.write(f'{i+1},{list.title},{list.desc}\n')
            # list_csv.write(i,list.title,list.desc)
        
    return send_from_directory("csvs",f'{user_idd}_list.csv')



# @token_required
@app.route('/api/export/<int:user_idd>/<int:list_idd>', methods=['GET'])
def export_card(user_idd,list_idd):
    user = Card.query.filter_by(user_id=user_idd,list_id=list_idd).all()
    with open(f'csvs/{user_idd}_card.csv', 'w') as list_csv:
        list_csv.write("SNo,Card_Name,Card_Description,Card_Status,Card_deadline,last_seen\n")
        for i in range(len(user)):

            # list = user.lists[i]
            # print(list)
            list_csv.write(f'{i+1},{user[i].card_title},{user[i].card_desc},{user[i].completed},{user[i].deadline},{user[i].last_seen}\n')
            # list_csv.write(i,list.title,list.desc)
        
    return send_from_directory("csvs",f'{user_idd}_list.csv')








class userApi(Resource):
    # @token_required
    @marshal_with(user_fields)
    # @cache.memoize(timeout=5)
    def get(self, user_id):
        # print("get userid", user_id)
        user_Det = User.query.all()
        print(user_Det)
        print(user_Det[0].email_id)
        user = User.query.filter(User.user_id == user_id).first()
        # print(user)
        list = List.query.filter(List.user_id == user_id).all()
        # print(list)
        if user:
            return user
        else:
            return "", 4
    # @token_required
    def put(self, user_id):
        # print("put userid", user_id)
        return {"message" :"You cant update user details"}
    # @token_required
    def delete(self, user_id):
        # print("delt userid", user_id)
        return {"message" : "You could not delete user details"}

    # @marshal_with(user_fields) 
    # @token_required    
    def post(self):
        # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        # args = create_user_parser.parse_args()
        # username = args.get("username" ,None)
        # email_id = args.get("email_id" ,None)
        # password = args.get("password" ,None)

        # if username is None: 
        #     return {
        #         "message" : "pls give username"
        #     } , 404

        # if email_id is None:
        #     return {
        #         "message" : "pls give email_id also"
        #     } , 404
            
        # if password is None:
        #    return {
        #         "message" : "pls give password also"
        #     } ,404     

        # user = User.query.filter(User.email_id == email_id).first()
        # if user:
        #     return "sale dusplicate maal bhejta"  

        
        # newuser = User(username = username, email_id = email_id, password=password)
        # db.session.add(newuser)
        # db.session.commit()
        # return marshal(newuser,user_fields)
        # print("put userid", user_id)
        return {"message" :"You cant update user details"}







         
class ListApi(Resource):
    # @marshal_with(list_fields)
    # @token_required
    def get(self, user_id, list_id):
        # print("get userid", user_id, list_id)
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            list = List.query.filter_by(list_id = list_id, user_id = user_id).first()
            print(list)
            if list:
                return marshal(list, list_fields)
            else:
                # return "apke pass iss index pe list nhin hai ", 404
                abort(404,message="apke pass iss index pe list nhin hai")
        else:
            # return {
            #     "message" : "bina user ke list mang rha"
            # }        
            abort(404,message="user not found")
        
    # @token_required
    def put(self, user_id, list_id):
        # print("put userid", user_id)

        args = create_list_parser.parse_args()
        title = args.get("title" ,None)
        # print(type(title))
        desc = args.get("desc" ,None)
        

        
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            list = List.query.filter_by(list_id = list_id, user_id = user_id).first()

            
            if list :
                if title is None:
                    list.title = list.title
                else:
                    list.title = title
        

                if desc is None: 
                    list.desc = list.desc

                else:
                    list.desc= desc
            else:
                abort(404,message="Not founda list of that index")            
        # list = List(title = title, desc = desc, user_id= user_id)
        db.session.add(list)
        db.session.commit()
        return marshal(list,list_fields)


    # @token_required
    def delete(self, user_id, list_id):
        # print("delt userid", user_id)
        list = List.query.filter_by(list_id = list_id, user_id = user_id).first()

        if list :
            card_of_particular_list = db.session.query(Card).filter(Card.list_id == list_id).all()

            if len(card_of_particular_list) > 0:
                for card in card_of_particular_list:
                    db.session.delete(card)

        else:
            abort(404,message="Not found any list of this index on this user")            
        db.session.delete(list)
        db.session.commit()

        return {
            "message" : "Successfully deleted"
        }, 200

    # @token_required
    def post(self,user_id):
        # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        args = create_list_parser.parse_args()
        title = args.get("title" ,None)
        
        desc = args.get("desc" ,None)
        

        if title is None: 
            abort(404, message="No title specified!, pls give first title ")


        if desc is None: 
            desc = ""

        
        list = List(title = title, desc = desc, user_id= user_id)
        db.session.add(list)
        db.session.commit()
        return marshal(list,list_fields)


class cardApi(Resource):
    # @token_required
    def get(self ,user_id, list_id, card_id):

        user = User.query.filter(User.user_id == user_id).first()
        if user:
            list = List.query.filter_by(list_id = list_id, user_id = user_id).first()
            print(list)

            if list:
                card = Card.query.filter_by(user_id= user_id,list_id = list_id , card_id = card_id).first()
                if card:
                    return marshal(card, card_fields)
                else:
                    abort(404, message="Not found any card")
            else:
                abort(404, message="You have no list , so cant get card")

        else:
            abort(404, message="You have no user, so cant get card ") 

    # @token_required
    def post(self, user_id, list_id):
        args = create_card_parser.parse_args()
        card_title = args.get("card_title" ,None)
        card_desc = args.get("card_desc" ,None)
        deadline = args.get("deadline" ,None)
        completed = args.get("completed" ,None)
        last_seen=dt.now().strftime("%I:%M:%S %p %d-%b-%Y")
        print(completed)
        

        if completed == "1":
            st = "Incomplete"
        
        else:
            st = "Complete"

        if card_title is None: 
            abort(404, message="No title specified!, pls give first title ")


        if card_desc is None: 
            abort(404, message="No card desc specified")

        if deadline is None: 
            abort(404, message="pls give specifc date whether you have done your task!")
        
                #   2002-12-31
        else:
            checkdate = deadline.split("-")

            if len(checkdate) == 3 :
                if(len(checkdate[0]) == 4 and len(checkdate[1]) == 2  ):
                    if(int(checkdate[1]) in months  and int(checkdate[2]) in days ):
                        deadline = deadline
                    else:
                        abort(404, message="Invalid check months and date should be in proper range")    

                else:
                    abort(404, message="Invalid date format!, dateformat should be YYYY-MM-DD")    

            else:
                abort(404, message="Invalid date format!, acca ji dateformat should be YYYY-MM-DD")    


                  


        
        card = Card(card_title=card_title, deadline=deadline, card_desc=card_desc,
                        completed=st, user_id=user_id, list_id=list_id, last_seen = last_seen)
        db.session.add(card)
        db.session.commit()
        return marshal(card,card_fields)

    # @token_required
    def put(self,user_id , list_id , card_id):
        args = update_card_parser.parse_args()
        print("------------")
        print(args)
        list_id = args.get("list_id", None)
        print(list_id)
        card_title = args.get("card_title" ,None)
        card_desc = args.get("card_desc" ,None)
        deadline = args.get("deadline" ,None)
        print(deadline)
        completed = args.get("completed" ,None)
        last_seen=dt.now().strftime("%I:%M:%S %p %d-%b-%Y")
        if completed == "1":
            st = "Incomplete"
        
        else:
            st = "Complete"

        user = User.query.filter(User.user_id == user_id).first()
        if user:
            list = List.query.filter_by(list_id = list_id, user_id = user_id).first()
            print(list)

            if list:
                card = Card.query.filter_by(user_id= user_id, card_id = card_id).first()
                print(card)
                if card:
                    card.last_seen = dt.now().strftime(" %I:%M:%S %p %d-%b-%Y")
                    if card_title is None:
                        card_title = card.card_title
                    else:
                        card.card_title = card_title    

                    if card_desc is None:
                        card_desc = card.card_desc
                    else:
                        card.card_desc = card_desc  

                    if deadline is None:
                        deadline = card.deadline
                    else:
                        checkdate = deadline.split("-")

                        if len(checkdate) == 3 :
                            if(len(checkdate[0]) == 4 and len(checkdate[1]) == 2  ):
                                if(int(checkdate[1]) in months  and int(checkdate[2]) in days ):
                                    card.deadline = deadline
                                else:
                                    abort(404, message="Invalid check months and date should be in proper range")    

                            else:
                                abort(404, message="Invalid date format!, dateformat should be YYYY-MM-DD")    

                        else:
                            abort(404, message="Invalid date format!, acca ji dateformat should be YYYY-MM-DD") 

                    if completed is None:
                        completed = card.completed
                        

                    else:
                        card.completed = st  
                        

                    if list_id is None:
                        list_id = card.list_id
                    else:
                        card.list_id = int(list_id) 


                    # card = Card(card_title=card_title, deadline=deadline, card_desc=card_desc,
                    #     completed=st, user_id=user_id, list_id=list_id)
                    db.session.add(card)
                    db.session.commit()
                    return marshal(card,card_fields)    

                else:
                    abort(404, message="for update , card is not found")    

            else:
                abort(404, message="for update , list where card, is not found") 

        else:
            abort(404, message="for update ,userhas list , list has card , is not found")                  




    # @token_required
    def delete(self, user_id, list_id, card_id):
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            list = List.query.filter_by(list_id = list_id, user_id = user_id).first()
            print(list)

            if list:
                card = Card.query.filter_by(user_id= user_id,list_id = list_id , card_id = card_id).first()
                if card:
                    db.session.delete(card)
                    db.session.commit()

                    return {
                        "message": f"succesfully deleted {card.card_title}"
                    }
                else:
                    abort(404, message="Not found any card")
            else:
                abort(404, message="You have no list , so cant get/delete card")

        else:
            abort(404, message="You have no user, so cant get/delete card ") 


class SummaryPage(Resource):
    
    # @token_required
    def get(self , user_idd):

        user = User.query.filter_by(user_id=user_idd).first()
        list_details = List.query.filter_by(user_id=user_idd).all()

        l_name = []
        l_id = []
        for i in list_details:
            l_id.append(i.list_id)
            l_name.append(i.title)
        st = []
        date_comp = []
        for j in l_id:
            status = []
            date = []
            card_details = Card.query.filter_by(list_id=j).all()
            for k in card_details:
                date.append(k.deadline)
                status.append(k.completed)

            st.append(status)
            date_comp.append(date)
        # print(date_comp) today.strftime("%b-%d-%Y")
        all = []
        d = dt.today()
        # da = d.strftime("%m-%d-%Y")



        for i in range(len(st)):
            mom = []
            T = 0
            F = 0
            d_passed = 0
            d_left = 0
            for elem in date_comp[i]:
                if dt.strptime(elem, "%Y-%m-%d") > d:
                    d_left += 1
                else:
                    d_passed += 1

            for elem in st[i]:
                if elem == 'Incomplete':
                    F += 1
                else:
                    T += 1
            mom.append(T)
            mom.append(F)
            # mom.append(d_left)
            mom.append(d_passed)
            all.append(mom)
        # print(all)
        images = []
        for i in range(len(all)):
            x = ["Complete", "Incomplete", "Deadline_passed"]
            y = all[i]
            plt.clf()
            plt.bar(x, y, color=['#641E16', 'blue', 'red'], width=0.3)

            plt.ylabel("Number of Task")
            plt.title("Summary of Task")

            # plt.savefig(f'vue-project\src\assets\images\plot_{i}.png')static

            # images.append(f'vue-project/src/assets/images/plot_{i}.png')static\image
            plt.savefig(f'static/image/plot_{i}.png')
            x = f'/static/image/plot_{i}.png'
            print(x)

            images.append(f'/static/image/plot_{i}.png')

        print(images)
        dict={}
        dict['images'] = images
        dict['all'] = all

        print(dict['all'])
        
        # username = 'cars2'
        # basepath = "static/images"

        # dir = os.walk(basepath)
        # print(dir)
        # file_list = []

        # for path, subdirs, files in dir:
        #     for file in files:
        #         temp = os.path.join('/' + path + '/', file)
        #         file_list.append(temp)
        # print(file_list)
        return  dict


api.add_resource(Register, "/api/Register")
api.add_resource(Login, "/api/Login")
api.add_resource(userApi, "/api/<int:user_id>")
# api.add_resource(export, "/api/export/<int:user_id>")
api.add_resource(SummaryPage, "/api/summary/<int:user_idd>")
api.add_resource(ListApi, "/api/list/<int:user_id>","/api/<int:user_id>/<int:list_id>")
api.add_resource(cardApi, "/api/card/<int:user_id>/<int:list_id>","/api/<int:user_id>/<int:list_id>/<int:card_id>")


# [['2022-09-13', '2022-08-29'], ['2022-09-13', '2022-09-30', '2022-09-21'],
#  ['2022-09-13', '2022-09-13'], ['2022-09-12']]

# from datetime import datetime as dt
# a = dt.strptime("9/2/22", "%m/%d/%y")
# print(a)
# b = dt.strptime("10/15/13", "%m/%d/%y")
# d = dt.today()
# print(d)
# print(a > b) #12 oct 2023 > 15 oct 2013
# print(a < b) #12 oct 2023 < 15 oct 2013
# print(a <= d) #12 oct 2023 < 3 sept 2022