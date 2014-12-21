import requests
import json
import time


token = 'TOKEN'
u_id = 'USERID'
lon = '90.0000'
lat = '0.0000'


headers = { 'Host':'plague.io',
            'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
            'Connection':'keep-alive',
            'Proxy-Connection':'keep-alive',
            'Accept':'application/json',
            'User-Agent':'Plague/1.1.25 (iPhone; iOS 8.1; Scale/2.00)',
            'Accept-Language':'en',
            'Accept-Encoding':'gzip, deflate'}



def vote_repost(post_id):
    '''
    Vote up post_id
    '''
    url = "http://plague.io/api/votes/repost/"
    payload = { 'latitude':lat,
                'longitude':lon,
                'repost_id':str(post_id),
                'token':token,
                'uid':u_id}
    r = requests.post(url, data=payload, headers=headers)
    print str(post_id)+ " " + r.text



def vote_skip(post_id):
    '''
    Vote down post_id
    '''
    url = "http://plague.io/api/votes/skip/"
    payload = { 'latitude':lat,
                'longitude':lon,
                'repost_id':str(post_id),
                'token':token,
                'uid':u_id}
    r = requests.post(url, data=payload, headers=headers)
    print str(post_id)+ " " + r.text


def send_text(text):
    url = "http://plague.io/api/posts/"
    send_text_payload = {
            'latitude':lat,
            'longitude':lon,
            'meta':'{"administrativeArea":"Quebec","country":"Canada","locality":"Montreal"}',
            'text':text,
            'token':token,
            'uid':u_id}
    r = requests.post(url, data=send_text_payload, headers=headers)
    print text + " - " + r.text



def comment(post_id, text):
    '''
    Comment on post_id
    '''
    url = "http://plague.io/api/posts/"+str(post_id)+"/comments/"
    comment_payload = {'text':str(text),
                        'token':token,
                        'uid':u_id}
    r = requests.post(url, data=comment_payload, headers=headers)
    print str(post_id) + " - "+ text + " - " + r.text


def photo_post(file,text):
    '''
    Upload a picture
    NOT YET WORKING
    {u'error': {u'info': u'uid+token required', u'code': u'API_AuthRequired'}}
    '''
    url = "http://plague.io/api/upload/"
    headers_upload = { 'Host':'plague.io',
                'Content-Type':'multipart/form-data; boundary=Boundary+207E2F629F02A0A1',
                'Connection':'keep-alive',
                'Proxy-Connection':'keep-alive',
                'Accept':'application/json',
                'User-Agent':'Plague/1.1.25 (iPhone; iOS 8.1; Scale/2.00)',
                'Accept-Language':'en',
                'Accept-Encoding':'gzip, deflate'}
    upfile = {'file': open(file, 'rb')}
    upload_payload = {'token':token,
                        'uid':u_id,
                        'file':upfile}
    r = requests.post(url, data=upload_payload, headers=headers_upload)
    print text + " - " + r.text



def post_link(media_link, media_link_preview, text):
    url = "http://plague.io/api/posts/"
    post_payload = {
                    'latitude':lat,
                    'longitude':lon,
                    'media':str(media_link),
                    'media_preview':str(media_link_preview),
                    'meta':'{"administrativeArea":"Quebec","country":"Canada","locality":"Montreal"}',
                    'text':text,
                    'token':token,
                    'uid':u_id}
    r = requests.post(url, data=post_payload, headers=headers)
    print str(media_link) + " - " + text + " - " + r.text



def post_delete(post_id):
    '''
    Deletes the post with post_id = post_id
    '''
    url = "http://plague.io/api/posts/" + str(post_id) + "/?token=" + token + "&uid=" + u_id
    r = requests.delete(url, headers=headers)
    print "deleted " + str(post_id) + " - " + r.text

#comment(89957,"Coooool")
#send_text('Hi From Northpole!')
#post_link("http://funnypictures.me/wp-content/uploads/2012/12/funny-pictures-new-record-lab-plague.jpg","http://funnypictures.me/wp-content/uploads/2012/12/funny-pictures-new-record-lab-plague.jpg","Plague... Eh?")
#post_link("http://google.com","http://google.com","http://google.com")
#post_delete("82871")


#photo_post("./plague.jpg","I told you, Plague is contagious!")
