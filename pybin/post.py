import datetime, xmlrpclib

wp_url = "http://s92500497.onlinehome.us/xmlrpc.php"
wp_username = "DBNAdmin"
wp_password = "Nur4ever"
wp_blogid = ""

status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

title = "Title with rob roy"
content = "Body with lots of content<hr>"
date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2019-10-20 21:08", "%Y-%m-%d %H:%M"))
categories = ["somecategory"]
tags = ["sometag", "othertag"]
data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
