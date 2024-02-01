user_decks={}

# def get_all_users():
#     global user_decks
#     all_users=List.query.all()
#     for user in all_users:
#         all_decks=[]
#         for deck in user.list_id:
#             all_decks.append(deck.id)
#         user_decks[user.username]=all_decks
#     return