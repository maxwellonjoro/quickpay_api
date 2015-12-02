
import urllib
import urllib2
import json
import requests

class QuickPayAPIException(Exception):
    pass

class QuickPayAPI:
	def __init__(self, username_, apiKey_):
		if len(username_) == 0 or len(apiKey_) == 0:
			raise QuickPayAPIException("Please provide both username_ and apiKey_ parameters")
			
		self.username = username_
		self.apiKey   = apiKey_
	
		#self.QuickPayURL			= "http://localhost:8888"
		self.QuickPayURL           = "http://api.quickpay.co.ke/api/mcpay"
		
		self.headers                = {'Content-Type':'application/json','SecureHash':apiKey_,'merchantId':username_}
		
		self.HTTP_RESPONSE_OK       = 200
		self.HTTP_RESPONSE_CREATED  = 201

		# Turn this on if you run into problems. It will print the raw HTTP response from our server
		self.Debug                  = True
		
	# HTTP method
	def sendRequest(self, referenceNo_, orderInfo_, amount_, card_, currency_):		
		if len(referenceNo_) == 0 or len(orderInfo_) == 0 or len(amount_) == 0 or len(card_) == 0 or len(currency_) == 0:
			raise QuickPayAPIException("Please provide all the parameters")

		parameters = {'username' : self.username,
			'reference': referenceNo_,
			'orderInfo': orderInfo_,
			'amount': amount_,
			'card': card_,
			'currency':currency_
		}
		
		response = self.executeRequest(self.QuickPayURL, parameters, self.headers)

		if self.responseCode == self.HTTP_RESPONSE_OK:
			decoded = json.loads(response)
			return decoded
			
		raise QuickPayAPIException(response)
		
	# HTTP send method
	def executeRequest(self, urlString, data_ = None, headers_ = None):
		print 'Data: ',data_
		try:
			if data_ is not None:
				response = requests.post(urlString, data=json.dumps(data_), headers=headers_)
			else:
				response = requests.get(urlString)
			
		except Exception as e:
			raise QuickPayAPIException(str(e))
		else:
			self.responseCode = response.status_code
			response = response.text
			if self.Debug:
				print self.responseCode
				#print response
			return response
			