# Abstraction
# reduce complexicity by hiding unnecessary details.

class EmailServices:
    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")
    def send_email(self,msg):
         self._connect()
         self._authenticate()
         print("Sending email....")
         print(f"Send:{msg}")
         self._diconnect()
        
    def _diconnect(self):
        print("Disconnecting from email server")
    
email=EmailServices()
email.send_email("hello")