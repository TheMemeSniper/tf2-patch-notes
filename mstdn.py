from mastodon import Mastodon
from random import randint
from os import path
"""
Mastodon.create_app(
   'TF2 Markov Generator',
   api_base_url = 'https://wetdry.world',
    to_file = 'pytooter_clientcred.secret'
)
"""

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
mastodon.log_in(
    'rivers@weezer.org',
    'the password of all time',
    to_file = 'pytooter_usercred.secret'
)

def gen(model):
    if model == 0:
        import models.main as model
        text = model.generate()
    elif model == 1:
        import models.worse as model
        text = model.generate()
    elif model == 2:
        import models.clusterfuck as model
    
    buffer = ""

    for i in range(randint(3,20)):
        text = model.generate()
        buffer = buffer + (f"- {text}\n")
    
    return buffer

def post(text, model):
    if model == 0:
        prelude = "An update to Team Fortress 2 has been released. The update will be applied automatically when you restart Team Fortress 2. The major changes include:"
    elif model == 1:
        prelude = "An awful update to Team Fortress 2 has been released. The bullshit will be applied automatically when you restart Team Fortress 2. The major changes include:"
    elif model == 2:
        prelude = "An absolute clusterfuck of an update to Team Fortress 2 has been released. The shitstorm will be applied automatically when you restart Team Fortress 2. The major changes include:"
    mastodon.status_post(f"{prelude} \n\n {text}", visibility="unlisted")

def returnpost(text, model):
    """
    debugging function
    """
    if model == 0:
        prelude = "An update to Team Fortress 2 has been released. The update will be applied automatically when you restart Team Fortress 2. The major changes include:"
    elif model == 1:
        prelude = "An awful update to Team Fortress 2 has been released. The bullshit will be applied automatically when you restart Team Fortress 2. The major changes include:"
    elif model == 2:
        prelude = "An absolute clusterfuck of an update to Team Fortress 2 has been released. The shitstorm will be applied automatically when you restart Team Fortress 2. The major changes include:"
    return f"{prelude} \n\n {text}"


choice = randint(0,2)

text = gen(choice)

post(text, choice)
    

