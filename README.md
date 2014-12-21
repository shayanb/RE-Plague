#[Plague] Reverse Engineering 
##a.k.a Plague Python API


Available Functions:
* vote_repost(post_id)
* vote_skip(post_id)
* send_text(text)
* comment(post_id, text)
* photo_post(file,text) #Not yet working
* post_link(media_link, media_link_preview, text)
* post_delete(post_id)

fill in the UID and Token and it's good to go.
to find these out just use any proxy to get the url Plague is calling, it would be something like this: 
> http://plague.io/api/posts/105725/?token=TOKEN&uid=UID

Also you can change the longitude and latitude to any of your choosing.
```
token = 'TOKEN'
u_id = 'USERID'
lon = '90.0000'
lat = '0.0000'
```
------------
__Note__: While doing this my account needed to be verified and I've been receiving multiple verification emails but haven't yet been verified. so watch out for trolling :)

__UPDATE__: My user got banned API_BANNED

![alt text](https://github.com/shayanb/RE-Plague/raw/master/img/verification_needed.jpg "verification")



[Plague]:http://plague.io/
