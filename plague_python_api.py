# Plague (plague.io) Python API
# Shayan 2014

import requests
import json
import time
from optparse import OptionParser


# You can hard code these here
token = 'TOKEN'
u_id = 'USERID'
# change the longiture and latitude to your choosing
lon = '90.0000' #northpole
lat = '0.0000'


headers = { 'Host':'plague.io',
			'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
			'Connection':'keep-alive',
			'Proxy-Connection':'keep-alive',
			'Accept':'application/json',
			'User-Agent':'Plague/1.1.25 (iPhone; iOS 8.3; Scale/2.00)',
			'Accept-Language':'en',
			'Accept-Encoding':'gzip, deflate'}



def login(username,password):
	'''
	Login to get the UserId and Token
	'''
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


def signup(name, email, password, lat, lon):
	'''
	Create new account
	'''
	url = "http://plague.io/api/users/"
	payload = { 'name':name,
				'email':email,
				'password':password,
				'latitude':str(lat),
				'longitude':str(lon)}
	r = requests.post(url, data=payload, headers=headers)

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

def get_posts(uid, token):
	'''
	Get your own plagues
	'''
	url = "http://plague.io/api/posts/?uid="+uid+"+&token="+token
	r = requests.get(url, headers=headers)
	return r.text

def get_infections_nearby(uid, token):
	'''
	Get nearby plagues
	'''
	url = "http://plague.io/api/infections/?uid="+uid+"+&token="+token
	r = requests.get(url, headers=headers)
	print r.text


def vote_repost_range(lrange=1000,rrange=2000):
	'''
	repost all the plagues between lrange and rrange
	'''
	if lrange < rrange:
		for i in xrange(lrange,rrange):
			vote_repost(i)
			time.sleep(5)

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
	'''
	Send a text plague
	'''
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
			time.sleep(5)
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
	'''
	Post a media plague with the image/video URL
	'''
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
	usage = "usage: %prog -h to see available options"
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
	#					 dest="media_link",
	#					 help="media link URL (must be used with -mp)")
	# parser.add_option("-n", "--mediap",
	#					 dest="media_link_preview",
	#					 help="media link preview URL")
	parser.add_option("-t", "--text",
						dest="text",
						help="text that you want to send")

	parser.add_option("-u", "--userid",
						dest="userid",
						help="Plague user_id")
	parser.add_option("-T", "--token",
						dest="token",
						help="Plague Token")
	parser.add_option("-c", "--comment",
						dest="comment",
						help="comment on post_id")

	parser.add_option("-V", "--longitude",
						dest="lon",
						help="Longitude '0.0000'")
	parser.add_option("-H", "--latitude",
						dest="lat",
						help="Latitude e.g '90.0000'")

(options, args) = parser.parse_args()


if options.username and options.password:
		login(options.username,options.password)

if options.userid:
	u_id = options.userid
if options.token:
	token = options.token

if options.lon and options.lat:
	lon = options.lon
	lat = options.lat

if options.text:
	send_text(options.text)
if options.postid:
	if options.comment:
		comment(options.postid, options.comment)
	else:
		vote_repost(options.postid)
