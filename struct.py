from google.appengine.ext import db

class registeredUser:
	fbid ;
	googleid;
	listOfDemands;
	ListofRequests;
	ListOfProposal;
	ListOfTransaction;
	Mystuff;
	defaultSpreadList = list ofStrings # initially all the friends of fb but editable . that who all will recieve a demand from me and vica versa .
	#strings
	name; 
	age; 
	sex;
	
class typeOfStuff:# contains the hierarchy of type of stuff as in books->fiction->thriller etc . it is editable by user , but a standard set is maintained and custom categories are seen by a creator or if it is in a request . 
	name  = string 
	parent typeofStuff 
	listofChildStuff = list of string 
	isBasic = bool # a top level type like a book , cd , softcopy , clothing shoes etc . 
	isCustom = bool # if not standard >>how to map with the creator user ??implementation depends on traversal . 

class item :
	name = string ; 
	type = typeOfStuff ; # the  leaf node in the hierarchy . 
	screenShoot ; 
	owner = name, string ;# or may be RegisteredUser Type . Whatever basically who owns it . 
	#visibility criteria 
	degreeOfSeperation ; 
	geographical Spread
	fb based types like school college , age group , male female etc . 


class  itemBasket : # list of item which are same !!! 
	name = string ; 
	list = list Of item;
        otheMatches = list of item ; 
  #a user migght put them in a basket , it means if i declare a possesion , i will be shown other possesions which might be same  thing , so all that is clubed to create a list of supplies . Hence this is a thing that will be "searched " and also implement algos to populate these baskets . 

class demands :  #kind of a mirror image od item . 
	name = string ; 
	type = typeOfStuff; 
	expected ScreenShot; 
#	Searchability criteria 
       --> essentially same as visibilty criteria in item 
       # there will be a browsability option and a demand will be created 

class request :# once demands meet item this is created , it is item linked not ritem basket link i.e. end to end (user to user)
	provider ;
	custumor; 
	item ; 
	demand ; 
	message ; 
	handShake ; # true or false
# a not on use model ,user X creates an item say a copy of "brief history of time" it enters a basket of all "bft:" items by all users . Now Y commes and puts a demand for " bft " so a demand object is created and since in search it will match with an itemBasket , (from where Y selects X ) a request is created , ( no need to link entire  itemBasket to demands; so now request is added to the list of user X , when X logs in it is shown these requests . and it may say yes to the request , or it can refer to the expected screenshot or say a message text with item , or demand and decline the offer .  It becomes a "suspension "which will say if user X declined to share all togather or has difficulty rightnow . 

class suspended:
	request; 
	Message texts ; # it may be a forum module , to be done later;
	decline = bool ; 
	waitmode = bool ; 

class proposal : 
	request 
	waitForinLeuof = bool ; # for a mirror image proposal 
	proposalList = list # a proposal list between users . other than this one . 
	appointement  ; # to be set by demander and another date in requestor class .We assume for time being that exchange will happen only in acquainted circles . or in same locality . 
	
