import web
from web import form
# Import the QuickPayAPI class
from QuickPayAPI import QuickPayAPI, QuickPayAPIException
from datetime import datetime
import cgi
import time

render = web.template.render('templates/')

urls = ('/', 'index',
        '/Usage', 'Usage')

app = web.application(urls, globals())

myform = form.Form( 
	form.Textbox("Street"), 
	form.Textbox("City"), 
	form.Textbox("State"), 
	form.Textbox("Postal Code"), 
	form.Dropdown('Country', ['Kenya', 'Uganda', 'Tanzania']), 
	form.Textbox("Email"), 
	form.Textbox("Cardholder's Name",form.notnull),
	form.Textbox("Card Number",form.notnull,form.regexp('\d+', 'Must be a digit'),form.Validator('Must be 16 to 19', lambda x:20>len(x)>=16 ))
	#,
)

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

class index: 
    def GET(self): 
	#print 'Form: ', myform()
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
	    #print "Form.d: ", form.d
            raise web.seeother('/Usage')

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
