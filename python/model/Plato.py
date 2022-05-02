
import os 
import json

class Plato:
    def __init__(self):
        print('plato')
        self.current_user = ""

    def load_user(self):
        self.current_user = os.getenv("USERNAME")
        print (self.current_user)

    def get_user(self):
        self.load_user()
        return self.current_user

    def get_work_files(self):
        self.load_user()
        data = self.load_data()
        return data.get('work_files')

    def load_data(self):
        path= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/data/user.json"
        if os.path.exists(path):
            with open(path, "r") as jsonFile:
                data = json.load(jsonFile)
                return data
        else:
            print("user file not found at "+path)
            return False


class WorkFile:
    def __init__(self,_path):
        print('workfile')
        self.path = _path 
        self.user = None
        self.sg_context = {}


class ShotgunContext:
    def __init__(self,_dict):
        self.data = _dict
        

class Xstage(WorkFile):
    def __init__(self):
        super().__init__()


