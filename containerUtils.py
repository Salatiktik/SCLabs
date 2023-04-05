import re
import json

class Container:
    containersFile = "containers.json"
    loadedContainers = {}
    currentContainer = set()
    username = ""

    def add(self, object):
        self.currentContainer.add(object)

    def add_list(self, list):
        self.currentContainer.update(list)

    def remove(self, object):
        if object in self.currentContainer:
            self.currentContainer.remove(object)
        else:
            raise Exception("Element is not found")

    def find(self, object):
        if object in self.currentContainer:
            return f"\"{object}\" is in container\n"
        else:
            return f"No such element as \"{object}\"\n"

    def find_list(self, list):
        existList = []
        for object in list:
            existList.append(self.find(object))
        
        return existList

    def grep(self, reString):
        resultList = []

        for object in self.currentContainer:
            if re.search(reString,object):
                resultList.append(object)

        if(len(resultList)==0):
            return "No matches"
        
        return resultList

    def save(self, direction):
        self.loadedContainers[self.username] = list(self.currentContainer)
        try:
            with open(direction,"w") as file:
                json.dump(self.loadedContainers,file)
        except Exception as e:
            raise e

    def propose_to_save(self):
        option = input("\tWhould you like to save current container before switching users?\n\tY/N:")
        if(option=='Y'):
            print("\tFile was saved")
            self.loadedContainers[self.username]=list(self.currentContainer)
            self.save(self.containersFile)

    def load(self, direction):
        try:
            with open(direction,"r") as file:
                self.loadedContainers = json.load(file)
        except:
            raise Exception("Wrong direction or file format")
        else:
            return True
    
    def switch(self, user):
        if(user in self.loadedContainers.keys()):
            self.currentContainer = set(self.loadedContainers[user])
        else:
            self.loadedContainers[user] = []
            self.currentContainer = set()