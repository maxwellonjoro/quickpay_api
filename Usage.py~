# Import the QuickPayAPI class
from QuickPayAPI import QuickPayAPI, QuickPayAPIException
from datetime import datetime
import cgi
import time

class Usage:
    def POST(self):	
	#Set the QuickPayAPI credentials
	username = "QuickPayAPIUsername"
	apikey   = "QuickPayAPIKey"

	api = QuickPayAPI(username, apikey)

	try:

            form = web.input()	
	    #form = cgi.FieldStorage()
	    #token = form["Token"]
	
	    date = time.strftime("%Y-%m-%d %X") #datetime.now()
	
	    print 'Date: ', date
	    referenceNo = date
	    orderInfo = date
	    amount = '1225'
	    card = form["Card Number"]
	    currency = 'KES'
	
	    #print 'date: %s, referenceNo: %s, orderInfo: %s, amount: %s, card: %s, currency: %s' % (date, referenceNo, orderInfo, amount, card, currency)
	
	    results = api.sendRequest(referenceNo, orderInfo, amount, card, currency)
	
	    print 'responseCode: %s, authId: %s, receiptNo: %s' % (results['responseCode'], results['authId'], results['receiptNo'])
		
	except QuickPayAPIException, e:
	    print 'Encountered an error while sending: %s' % str(e)
