import os

class Spec(object):
    name = str(input("Nama :"))
    def check(self):
        if self.name:
            data = {
                    "Username :" : "USERNAME",
                    "Computer Name :" : "COMPUTERNAME",
                    "Operating System :" : "OS",
                    "Processor revision :":"PROCESSOR_REVISION",
                    "Processor Level :" : "PROCESSOR_LEVEL",
                    "Processor Architecture :" : "PROCESSOR_ARCHITECTURE",
                    "Number of Processors :" :"NUMBER_OF_PROCESSORS"
                }
            for x, y in data.items():
                return x,os.environ.get(y)
    
Spec().check()