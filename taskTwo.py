import json
import re
from containerUtils import Container

def task_two():
    container = Container()

    container.username = input("Enter username:")
    option = input("Enter file option:\n\t1)Load default file\n\t2)Load you file\nOption:")
    if(option=="1"):
        print("Loading default containers file")
        container.containersFile = "containers.json"
    elif(option == "2"):
        container.containersFile = input("Enter path to your file: ")

    try:
        f = open(container.containersFile)
        container.loadedContainers = json.load(f)
        container.switch(container.username)
        
    except:
        print("File loading error. Default file was loaded")
        container.containersFile = "containers.json"
        f = open(container.containersFile)
        container.loadedContainers = json.load(f)
        container.switch(container.username)

    print("""Commands list:\n\tadd <key> [key, …] – add one or more elements to the container (if the element is already in there then don’t add);\n
        remove <key> – delete key from container;\n
        find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is;\n
        list – print all elements of container;\n
        grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is;\n
        save - save container to file;\n
        load <direction>– load container from file;\n
        switch <username>– switches to another user.
""")
    while(True):
        try:
            command = input('>>> ')

            if(re.search("^add <(.+)>$",command)):
                container.add(re.search("<(.+)>",command)[1])

            elif(re.search("^add \[(.+)\]$",command)):
                container.add_list(re.search("\[(.+)\]",command)[1].split(','))

            elif(re.search("^remove <(.+)>$",command)):
                container.remove(re.search("<(.+)>",command)[1])

            elif(re.search("^find <(.+)>$",command)):
                print(container.find(re.search("^find <(.+)>$",command)[1]))

            elif(re.search("^find \[(.+)\]$",command)):
                print(*container.find_list(re.search("\[(.+)\]",command)[1].split(',')))

            elif(re.search("^list$",command)):
                if(len(container.currentContainer)):
                    print(container.currentContainer)
                else:
                    print("Container is empty")

            elif(re.search("^grep <(.+)>$",command)):
                print(*container.grep(re.search("<(.+)>",command)[1]))

            elif(re.search("^save$",command)):
                container.save(container.containersFile)

            elif(re.search("^load <(.+)>$",command)):
                tempDirection = re.search("<(.+)>",command)[1]
                if(container.load(tempDirection)):
                    container.containersFile = tempDirection
                    if(container.loadedContainers[container.username]):
                        container.add_list(container.loadedContainers[container.username])
                    else:
                        print("There is no container with current username, data in current container wasn't updated")

            elif(re.search("^switch <(.+)>$",command)):
                container.propose_to_save()
                container.switch(re.search("<(.+)>",command)[1])

            else:
                raise Exception("Wrong command or format")
            
        except Exception as e:
            print('\033[91m'+"Exception:",'\033[37m',e)

        
        
    
    
