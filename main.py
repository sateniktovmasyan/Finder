import json


def loadScientistList():
    with open('names.json') as data_file:
        list = json.load(data_file)
        data = list["name_setup"]
    return data


def inputSearchOptions(scientists):
    keywords = ["firstname", "lastname", "degree", "jobtitle", "organization", "subject"]
    keyword_values = {}
    print ("here are the keywords: " + str(keywords))
    for item in keywords:
        user_answer = raw_input("Please insert value for " + item)
        if user_answer != "":
            keyword_values[item] = user_answer.lower()
    return keyword_values


def findMatches(scientists, keyword_values):
    matches = []
    for item in scientists:
        matchedKeys = 0
        for key in keyword_values:
            if item[key] == keyword_values[key]:
                matchedKeys += 1
            else:
                break
        if matchedKeys == len(keyword_values):
            matches.append(item)
    return matches

def printing(matches):
    for i in range(len(matches)):
        for key in matches[i]:
            print key + ' : ' + matches[i][key]


def main():
    scientists = loadScientistList()
    keyword_values = inputSearchOptions(scientists)
    matches = findMatches(scientists, keyword_values)
    printing(matches)


main()

