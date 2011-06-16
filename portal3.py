import cgi
from google.appengine.ext import db
import os
import urllib
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class registeredUser(db.Model):
	name = db.StringProperty(); 
	age =  db.StringProperty();
	description =  db.StringProperty();
	address =  db.StringProperty();
	sex = db.StringProperty();


class itemData (db.Model):
	itemName = db.StringProperty(); 
	itemType = db.StringProperty(); 
	screenShoot = db.StringProperty(); 
	age = db.StringProperty(); 
	description = db.StringProperty(); 
	owner = db.ReferenceProperty(registeredUser);
	owner_name = db.StringProperty();

class requestData(db.Model):
	reqName = db.StringProperty(); 
	reqType = db.StringProperty(); 
	#screenShoot = db.StringProperty(); 
	requestor = db.ReferenceProperty(registeredUser);
	requestor_name = db.StringProperty();
	description = db.StringProperty(); 


class NewUser(webapp.RequestHandler):
    def get(self):
	    template_values = {
		'name':cgi.escape(self.request.get('name')) ,
            }

	    path = os.path.join(os.path.dirname(__file__), 'html/createNew.html')
	    self.response.out.write(template.render(path, template_values))
	    
class  NewItem(webapp.RequestHandler):
	def get(self):
	    template_values = {
		'name':cgi.escape(self.request.get('name')) ,
            }
	    path = os.path.join(os.path.dirname(__file__), 'html/new_item.html')
	    self.response.out.write(template.render(path, template_values))

class createItem(webapp.RequestHandler):
	def post(self):
		print "hello world"
		print cgi.escape(self.request.get('name'))
		NewItem = itemData();
		NewItem.itemName = cgi.escape(self.request.get('itemName'))
		NewItem.owner_name = cgi.escape(self.request.get('name'))
		NewItem.itemType= cgi.escape(self.request.get('itemType'))
		NewItem.age= cgi.escape(self.request.get('age'))
		NewItem.description = cgi.escape(self.request.get('description'))
		NewItem.put()
	        string1 = "/index?name="+cgi.escape(self.request.get('name'));
	       # self.redirect(string1)
		print NewItem.owner_name
		print NewItem.itemName

		
class  NewRequest(webapp.RequestHandler):
	def get(self):
	    template_values = {
		'name':cgi.escape(self.request.get('name')) ,
            }
	    path = os.path.join(os.path.dirname(__file__), 'html/new_req.html')
	    self.response.out.write(template.render(path, template_values))

class createRequest(webapp.RequestHandler):
	def post(self):
		print "hello world"
		print cgi.escape(self.request.get('name'))
		reqItem = requestData();
		reqItem.reqName = cgi.escape(self.request.get('reqName'))
		reqItem.requestor_name = cgi.escape(self.request.get('name'))
		reqItem.reqType= cgi.escape(self.request.get('reqType'))
		reqItem.description = cgi.escape(self.request.get('description'))
		reqItem.put()
		print reqItem.reqName;
	        string1 = "/index?name="+cgi.escape(self.request.get('name'));
	       # self.redirect(string1)

class MainPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""
		  <html>
	   	 <body>
	    	<p>Hi 
	      	<form action="/index" method="post">
		<p>NAME :::	<div><textarea name="name" rows="1" cols="60"></textarea></div></p>
			<div><input type="submit" value="Sign Guestbook"></div>
	      	</form>
	    	</body>
	  	</html>""")

class Index(webapp.RequestHandler):
    def post(self):
	    self.response.out.write(cgi.escape(self.request.get('name')))
	    userQ =db.GqlQuery("SELECT * FROM registeredUser WHERE name = :1",cgi.escape(self.request.get('name')))
	    if  userQ.count()>0 :
		    user= userQ.fetch(1)[0]
	#    self.response.out.write( user.name )
	    string1 = "/newUser?name="+cgi.escape(self.request.get('name'))
	    if  userQ.count() >0 :
		    itemQ =db.GqlQuery("SELECT * FROM itemData WHERE owner_name = :1",cgi.escape(self.request.get('name')))
		    items=itemQ.fetch(10)
		    reqQ =db.GqlQuery("SELECT * FROM requestData WHERE requestor_name = :1",cgi.escape(self.request.get('name')))
		    reqs=reqQ.fetch(10)
	    	    template_values = {
				     'name':cgi.escape(self.request.get('name')) ,
				     'items':items,
				     'reqs':reqs,

				     }

		    path = os.path.join(os.path.dirname(__file__), 'html/index.html');
	    	    self.response.out.write(template.render(path, template_values))
	    else :
		    self.response.out.write("not got it " )
		    self.redirect(string1)

       


			

class createNew(webapp.RequestHandler):
    def post(self):
	    new_u = registeredUser()
	    new_u.name = cgi.escape(self.request.get('name'));
	    new_u.age = cgi.escape(self.request.get('age'));
	    new_u.description = cgi.escape(self.request.get('description'));
	    new_u.address= cgi.escape(self.request.get('address'));
	    self.response.out.write('<html><body>')
            self.response.out.write(cgi.escape(self.request.get('name')))
            self.response.out.write('You wrote:<pre>')
            self.response.out.write(cgi.escape(self.request.get('description')))
            self.response.out.write('</pre></body></html>')
	    new_u.put();

	    string1 = "/index?name="+cgi.escape(self.request.get('name'));
	    #self.redirect(string1)
	    self.redirect("/showall")

class showall(webapp.RequestHandler):
	def get(self):
		for user in registeredUser.all():
			print user.name
			print user.age
			print user.description
			print "-========================================"

class showallItem(webapp.RequestHandler):
	def get(self):
		for it in itemData.all():
			print it.owner_name
			print it.itemName
			print it.description
			print "-========================================"

class showallReq(webapp.RequestHandler):
	def get(self):
		for it in requestData.all():
			print it.requestor_name
			print it.reqName
			print it.description
			print "-========================================"

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/index', Index),
                                      ('/createNew', createNew),
				      ('/newUser',NewUser),
				      ('/new_item',NewItem),
				      ('/createItem',createItem),
				      ('/new_req',NewRequest),
				      ('/createRequest',createRequest),
				      ('/showallItem',showallItem),
				      ('/showallReq',showallReq),
				      ('/showall',showall)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

