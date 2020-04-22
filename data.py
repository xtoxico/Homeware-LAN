import json
import random
from cryptography.fernet import Fernet
<<<<<<< HEAD
import redis
from redisworks import Root
=======
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645


class Data:

<<<<<<< HEAD
    version = 'v0.6'
=======
    version = 'v0.5.2'
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
    homewareData = {}
    homewareFile = 'homeware.json'
    secureData = {}
    secureFile = 'secure.json'


    def __init__(self):
<<<<<<< HEAD
        self.redis = redis.Redis("localhost")
        self.ddbb = Root()

        self.ddbb.transfer = False

        if not self.ddbb.transfer == True:
            print('Must create the database')
            with open(self.homewareFile, 'r') as f:
                self.ddbb.homewareData = json.load(f)
            with open(self.secureFile, 'r') as f:
                self.ddbb.secureData = json.load(f)
            self.ddbb.transfer = True

        else:
            print('DDBB up and running')

=======
        try:
            with open(self.homewareFile, 'r') as f:
                self.homewareData = json.load(f)
            #Create the secure file if doesn't exists: v0.3 to v0.4
            try:
                with open(self.secureFile, 'r') as f:
                    self.secureData = json.load(f)
            except:
                with open('config.json', 'r') as f:
                    self.secureData = json.load(f)
                with open('token.json', 'r') as f:
                    self.secureData['token']['google'] = json.load(f)['google']
                with open(self.secureFile, 'w') as f:
                    json.dump(self.secureData, f)
            #Create DDNS content v0.3 to v0.4
            try:
                ddns = self.secureData['ddns']
            except:
                self.secureData['ddns'] = {
                    'enabled': False,
                    'status': 'Disabled',
                    'code': 'unknown',
                    'last': 'unknown',
                    'ip': 'unknown',
                    'provider': 'ddns',
                    'hostname': self.secureData['domain'],
                    'username': '',
                    'password': ''
                }
                self.save()
            #Create apikey content v0.3 to v0.4
            try:
                ddns = self.secureData['token']['apikey']
            except:
                self.secureData['token']['apikey'] = ''
                self.save()
        except:
            print('Hi')
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

    def getVersion(self):
        return {'version': self.version}

<<<<<<< HEAD
    def redisStatus(self):
        status = {}
        try:
            response = self.redis.client_list()
            status =  {
                'enable': True,
                'status': 'Running'
            }
        except redis.ConnectionError:
            status = {
                'enable': True,
                'status': 'Stoped'
            }
        return status

    def firstRun(self):
        return False

    def getGlobal(self):
        data = {
            'devices': self.ddbb.homewareData['devices'],
            'status': self.ddbb.homewareData['status']
        }
        return data
=======
# FILES

    def firstRun(self):
        try:
            with open(self.homewareFile, 'r') as f:
                self.homewareData = json.load(f)
            with open(self.secureFile, 'r') as f:
                self.secureData = json.load(f)
            return False
        except:
            return True

    def save(self):
        with open(self.homewareFile, 'w') as f:
            json.dump(self.homewareData, f)
        with open(self.secureFile, 'w') as f:
            json.dump(self.secureData, f)

    def refresh(self):
        with open(self.homewareFile, 'r') as f:
            self.homewareData = json.load(f)
        with open(self.secureFile, 'r') as f:
            self.secureData = json.load(f)
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

# DEVICES

    def getDevices(self):
<<<<<<< HEAD
        # with open(self.homewareFile, 'w') as f:
        #     json.dump(self.homewareData, f)
        return self.ddbb.homewareData['devices']
=======
        with open(self.homewareFile, 'w') as f:
            json.dump(self.homewareData, f)
        return self.homewareData['devices']
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

    def updateDevice(self, incommingData):
        deviceID = incommingData['devices']['id']
        temp_devices = [];
<<<<<<< HEAD
        for device in self.ddbb.homewareData['devices']:
=======
        for device in self.homewareData['devices']:
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            if device['id'] == deviceID:
                temp_devices.append(incommingData['devices'])
            else:
                temp_devices.append(device)
<<<<<<< HEAD
        self.ddbb.homewareData['devices'] = temp_devices
        # self.save()

    def createDevice(self, incommingData):
        deviceID = incommingData['devices']['id']
        self.ddbb.homewareData['devices'].append(incommingData['devices'])
        self.ddbb.homewareData['status'][deviceID] = {}
        self.ddbb.homewareData['status'][deviceID] = incommingData['status']
        # self.save()

    def deleteDevice(self, value):
        temp_devices = [];
        for device in self.ddbb.homewareData['devices']:
            if device['id'] != value:
                temp_devices.append(device)
        self.ddbb.homewareData['devices'] = temp_devices
        # Delete status
        status = self.ddbb.homewareData['status']
        del status[value]
        self.ddbb.homewareData['status'] = status
        # self.save()
=======
        self.homewareData['devices'] = temp_devices
        self.save()

    def createDevice(self, incommingData):
        deviceID = incommingData['devices']['id']
        self.homewareData['devices'].append(incommingData['devices'])
        self.homewareData['status'][deviceID] = {}
        self.homewareData['status'][deviceID] = incommingData['status']
        self.save()

    def deleteDevice(self, value):
        temp_devices = [];
        for device in self.homewareData['devices']:
            if device['id'] != value:
                temp_devices.append(device)
        self.homewareData['devices'] = temp_devices
        # Delete status
        status = self.homewareData['status']
        del status[value]
        self.homewareData['status'] = status
        self.save()
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

# RULES

    def getRules(self):
<<<<<<< HEAD
        # with open(self.homewareFile, 'w') as f:
        #     json.dump(self.homewareData, f)
        return self.ddbb.homewareData['rules']

    def updateRule(self, incommingData):
        self.ddbb.homewareData['rules'][int(incommingData['id'])] = incommingData['rule']
        # self.save()

    def createRule(self, incommingData):
        self.ddbb.homewareData['rules'].append(incommingData['rule'])
        # self.save()

    def deleteRule(self, value):
        temp_rules = self.ddbb.homewareData['rules']
        del temp_rules[int(value)]
        self.ddbb.homewareData['rules'] = temp_rules
        # self.save()
=======
        with open(self.homewareFile, 'w') as f:
            json.dump(self.homewareData, f)
        return self.homewareData['rules']

    def updateRule(self, incommingData):
        self.homewareData['rules'][int(incommingData['id'])] = incommingData['rule']
        self.save()

    def createRule(self, incommingData):
        self.homewareData['rules'].append(incommingData['rule'])
        self.save()

    def deleteRule(self, value):
        temp_rules = self.homewareData['rules']
        del temp_rules[int(value)]
        self.homewareData['rules'] = temp_rules
        self.save()
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

# STATUS

    def getStatus(self):
<<<<<<< HEAD
        # with open(self.homewareFile, 'w') as f:
        #     json.dump(self.homewareData, f)
        return self.ddbb.homewareData['status']

    def updateParamStatus(self, device, param, value):
        self.ddbb.homewareData['status'][device][param] = value
        # self.save()
=======
        with open(self.homewareFile, 'w') as f:
            json.dump(self.homewareData, f)
        return self.homewareData['status']

    def updateParamStatus(self, device, param, value):
        self.homewareData['status'][device][param] = value
        self.save()
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645

# SECURE

    def getSecure(self):
        data = {
            "google": {
<<<<<<< HEAD
                "client_id": self.ddbb.secureData['token']["google"]["client_id"],
                "client_secret": self.ddbb.secureData['token']["google"]["client_secret"],
            },
            "ddns": self.ddbb.secureData['ddns'],
            "apikey": self.ddbb.secureData['token']['apikey']
=======
                "client_id": self.secureData['token']["google"]["client_id"],
                "client_secret": self.secureData['token']["google"]["client_secret"],
            },
            "ddns": self.secureData['ddns'],
            "apikey": self.secureData['token']['apikey']
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
        }
        return data

    def updateSecure(self, incommingData):
<<<<<<< HEAD
        self.ddbb.secureData['token']["google"]["client_id"] = incommingData['google']['client_id']
        self.ddbb.secureData['token']["google"]["client_secret"] = incommingData['google']['client_secret']
        self.ddbb.secureData['ddns']['username'] = incommingData['ddns']['username']
        self.ddbb.secureData['ddns']['password'] = incommingData['ddns']['password']
        self.ddbb.secureData['ddns']['provider'] = incommingData['ddns']['provider']
        self.ddbb.secureData['ddns']['hostname'] = incommingData['ddns']['hostname']
        self.ddbb.secureData['ddns']['enabled'] = incommingData['ddns']['enabled']
        self.save()

    def getToken(self,agent):
        return self.ddbb.secureData['token'][agent]

    def updateToken(self,agent,type,value,timestamp):
        self.ddbb.secureData['token'][agent][type]['value'] = value
        self.ddbb.secureData['token'][agent][type]['timestamp'] = timestamp
        self.save()

    def setUser(self, incommingData):
        if self.ddbb.secureData['user'] == '':
            data = {}
            key = Fernet.generate_key()
            self.ddbb.secureData['key'] = str(key)
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(str.encode(incommingData['pass']))   #required to be bytes
            self.ddbb.secureData['user'] = incommingData['user']
            self.ddbb.secureData['pass'] = str(ciphered_text)
=======
        self.secureData['token']["google"]["client_id"] = incommingData['google']['client_id']
        self.secureData['token']["google"]["client_secret"] = incommingData['google']['client_secret']
        self.secureData['ddns']['username'] = incommingData['ddns']['username']
        self.secureData['ddns']['password'] = incommingData['ddns']['password']
        self.secureData['ddns']['provider'] = incommingData['ddns']['provider']
        self.secureData['ddns']['hostname'] = incommingData['ddns']['hostname']
        self.secureData['ddns']['enabled'] = incommingData['ddns']['enabled']
        self.save()

    def getToken(self,agent):
        return self.secureData['token'][agent]

    def updateToken(self,agent,type,value,timestamp):
        self.secureData['token'][agent][type]['value'] = value
        self.secureData['token'][agent][type]['timestamp'] = timestamp
        self.save()

    def setUser(self, incommingData):
        if self.secureData['user'] == '':
            data = {}
            key = Fernet.generate_key()
            self.secureData['key'] = str(key)
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(str.encode(incommingData['pass']))   #required to be bytes
            self.secureData['user'] = incommingData['user']
            self.secureData['pass'] = str(ciphered_text)
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            self.save()
            return 'Saved correctly!'
        else:
            return 'Your user has beed set in the past'

    def setDomain(self, value):
<<<<<<< HEAD
        self.ddbb.secureData['domain'] = value
        self.ddbb.secureData['ddns']['hostname'] = value
        self.save()

    def getDDNS(self):
        return self.ddbb.secureData['ddns']

    def updateDDNS(self, ip, status, code, enabled, last):
        self.ddbb.secureData['ddns']['ip'] = ip
        self.ddbb.secureData['ddns']['status'] = status
        self.ddbb.secureData['ddns']['code'] = code
        self.ddbb.secureData['ddns']['enabled'] = enabled
        self.ddbb.secureData['ddns']['last'] = last
=======
        self.secureData['domain'] = value
        self.secureData['ddns']['hostname'] = value
        self.save()

    def getDDNS(self):
        return self.secureData['ddns']

    def updateDDNS(self, ip, status, code, enabled, last):
        self.secureData['ddns']['ip'] = ip
        self.secureData['ddns']['status'] = status
        self.secureData['ddns']['code'] = code
        self.secureData['ddns']['enabled'] = enabled
        self.secureData['ddns']['last'] = last
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
        self.save()

    def generateAPIKey(self):
        chars = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        token = ''
        i = 0
        while i < 40:
            token += random.choice(chars)
            i += 1
<<<<<<< HEAD
        self.ddbb.secureData['token']['apikey'] = token
=======
        self.secureData['token']['apikey'] = token
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
        self.save()
        return token

# LOGIN

    def login(self, headers):
        user = headers['user']
        password = headers['pass']


<<<<<<< HEAD
        cipher_suite = Fernet(str.encode(self.ddbb.secureData['key'][2:len(self.ddbb.secureData['key'])]))
        plain_text = cipher_suite.decrypt(str.encode(self.ddbb.secureData['pass'][2:len(self.ddbb.secureData['pass'])]))
        responseData = {}
        if user == self.ddbb.secureData['user'] and plain_text == str.encode(password):
=======
        cipher_suite = Fernet(str.encode(self.secureData['key'][2:len(self.secureData['key'])]))
        plain_text = cipher_suite.decrypt(str.encode(self.secureData['pass'][2:len(self.secureData['pass'])]))
        responseData = {}
        if user == self.secureData['user'] and plain_text == str.encode(password):
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            #Generate the token
            chars = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            token = ''
            i = 0
            while i < 40:
                token += random.choice(chars)
                i += 1
            #Saved the new token
<<<<<<< HEAD
            self.ddbb.secureData['token']['front'] = token
=======
            self.secureData['token']['front'] = token
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            #Prepare the response
            responseData = {
                'status': 'in',
                'user': user,
                'token': token
            }
        else:
            #Prepare the response
            responseData = {
                'status': 'fail'
            }

        self.save()
        return responseData

    def validateUserToken(self, headers):
        user = headers['user']
        token = headers['token']
        responseData = {}
<<<<<<< HEAD
        if user == self.ddbb.secureData['user'] and token == self.ddbb.secureData['token']['front']:
=======
        if user == self.secureData['user'] and token == self.secureData['token']['front']:
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            responseData = {
                'status': 'in'
            }
        else:
            responseData = {
                'status': 'fail'
            }

        return responseData

    def googleSync(self, headers, responseURL):
        user = headers['user']
        password = headers['pass']

<<<<<<< HEAD
        cipher_suite = Fernet(str.encode(self.ddbb.secureData['key'][2:len(self.ddbb.secureData['key'])]))
        plain_text = cipher_suite.decrypt(str.encode(self.ddbb.secureData['pass'][2:len(self.ddbb.secureData['pass'])]))
        responseData = {}
        if user == self.ddbb.secureData['user'] and plain_text == str.encode(password):
=======
        cipher_suite = Fernet(str.encode(self.secureData['key'][2:len(self.secureData['key'])]))
        plain_text = cipher_suite.decrypt(str.encode(self.secureData['pass'][2:len(self.secureData['pass'])]))
        responseData = {}
        if user == self.secureData['user'] and plain_text == str.encode(password):
>>>>>>> 8c5b5cc1aca3e5db3f5f7ccdb1b96498afe3a645
            return responseURL
        else:
            return "fail"
