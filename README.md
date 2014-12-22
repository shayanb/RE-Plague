#[Plague] Social Platform Python API

>All Plague users are connected to each other right from the start.
Infection starts at the source of the information…
and spreads to the nearest users like a virus.
Infected users spread the information further by infecting the users closest to them.
Plague allows you to incubate information epidemics of any size.
The possibilities are endless. 
 -plague.io

Available Functions:
* login(user,password)
* vote_repost(post_id)
* vote_skip(post_id)
* send_text(text)
* comment(post_id, text)
* photo_post(file,text) #Not yet working
* post_link(media_link, media_link_preview, text)
* post_delete(post_id)

to get UserId and Token run this:
> python ./plague_python_api.py -e 'name@mailinator.com' -p 'PAs$w0R1)'

to post a text plague:
> python ./plague_python_api.py -u UserId -T Token -t 'Text goes here'

to Spread (Vote up) a plague:
> python ./plague_python_api.py -u UserId -T Token -p Post_Id

to comment on a plague:
> python ./plague_python_api.py -u UserId -T Token -p Post_Id -c 'Comment Text'

for more options:
> python ./plague_python_api.py -h

Also you can change the longitude and latitude to any of your choosing.
```
token = 'TOKEN'
u_id = 'USERID'
lon = '90.0000'
lat = '0.0000'
```
------------


###Disclaimer

This is for personal and research use only. No one likes spammers.


[Plague]:http://plague.io/
