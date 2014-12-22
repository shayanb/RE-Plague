import requests
import json
import time
from optparse import OptionParser


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




def login(username,password):
    url = "http://plague.io/api/auth/login/?email="+str(username)+"+&password="+password
    r = requests.get(url, headers=headers)
    #print r.json()
    print "What you need"
    print "-------------"
    print "userid = " + str(r.json()["client"]["uid"])
    print "token = " + r.json()["client"]["token"]
    print ""
    print "This is your plague"
    print "-------------------"
    print "id = " + str(r.json()["user"]["id"])
    print "IP = " + str(r.json()["client"]["ipaddress"])
    print "name = " + r.json()["user"]["name"]
    print "bio = " + str(r.json()["user"]["bio"])
    print "Can infect = " + str(r.json()["user"]["can_infect"])
    print "Karma = " + str(r.json()["user"]["karma"])
    print ""
    print "is temporary = " + str(r.json()["user"]["is_temporary"])
    print "is email verified = " + str(r.json()["user"]["is_email_verified"])
    print "is verified = " + str(r.json()["user"]["is_verified"])




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


def vote_repost_range(lrange=1000,rrange=2000):
    '''
    repost all the plagues between lrange and rrange
    '''
    if lrange < rrange:
        for i in xrange(lrange,rrange):
            vote_repost(i)
    else:
        print "Left range must be smaller than Right range"


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


def comment_range(text, lrange, rrange):
    if lrange < rrange:
        for i in xrange(lrange,rrange):
            comment(str(i),text)
    else:
        print "Left range must be smaller than Right range"



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





#Opt parser - not complete
if __name__ == "__main__":
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--email",
                        dest="username",
                        help="'john@do.e' (must be used with -p)")
    parser.add_option("-p", "--password",
                        dest="password",
                        help="password")
    parser.add_option("-i", "--postid",
                        dest="postid",
                        help="Post_id")
    # parser.add_option("-m", "--medialink",
    #                     dest="media_link",
    #                     help="media link URL (must be used with -mp)")
    # parser.add_option("-n", "--mediap",
    #                     dest="media_link_preview",
    #                     help="media link preview URL")
    parser.add_option("-t", "--text",
                        dest="text",
                        help="text that you want to send")

    parser.add_option("-u", "--userid",
                        dest="userid",
                        help="Plague user_id")
    parser.add_option("-T", "--token",
                        dest="token",
                        help="Plague Token")

(options, args) = parser.parse_args()




if options.username and options.password:
        login(options.username,options.password)

if options.userid:
    u_id = options.userid
if options.token:
    token = options.token

if options.text:
    send_text(options.text)
