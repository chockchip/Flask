import json
from os import popen
from flaskblog import db
from flaskblog.models import Post

path = "/Users/watcharapongwongrattanasirikul/Documents/Git/Flask_Blog/posts.json"

with open(path) as json_file:
    data = json.load(json_file)
    
    for post_dict in data:
        post = Post(title=post_dict['title'], content=post_dict['content'], user_id=post_dict['user_id'])
        db.session.add(post)
        
db.session.commit()
# test_post = {'title': 'Best Videos For Learning Python', 'content': 'Mei ei mazim dicunt feugait? Ludus mandamus ne est, per ne iusto facilisis moderatius! Has agam utamur ad! Ius reque aeterno cu, fabellas facilisi repudiare eu sit, te cibo convenire similique est. Ea cum viderer imperdiet liberavisse.\r\n\r\nPro minim iuvaret ad. No nam ornatus principes euripidis, at sale vituperatoribus eos, eros regione scripserit id mea. Has ne inermis nostrum, quo tantas melius dissentias at! Ut vim tibique omnesque. An mel modo ponderum, eum at probo appetere imperdiet? Natum quaeque intellegebat per ex. Cu viris clita sit?\r\n\r\nReque menandri dissentias sed ne, no tota nonumes eos, vix in tempor maiestatis erant.', 'user_id': 1}

# post = Post(title=test_post['title'], content=test_post['content'], user_id=test_post['user_id'])

# db.session.add(post)
# db.session.commit()