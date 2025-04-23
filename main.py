class Course:
    def __init__(self, name, code, section, days, time, prof, online, tutorial):
        self.name = name # "COMP"
        self.code = code # "1405"
        self.section = section # "C"   
        self.days = days # "Tue Thu"
        self.time = time # "11:35 - 12:55"
        self.prof = prof # Yanan Mao
        self.online = online # False
        self.tutorial = tutorial # False     
             

    def toString(self):
        return (self.name, self.code, self.section, self.days, self.time, self.prof, self.online, self.tutorial)


def main():
    courses = parseText()
    viewAll(courses)

def viewAll(dict):
     for name in dict.keys():
          for code in dict[name].keys():
               for section in dict[name][code].keys():
                    print(dict[name][code][section].toString())

def parseText():
    course_names = ["AERO","AFRI","ASLA","ANTH","ALDS","ARAB","ARCY","ACSE","ARCH","ARCC","ARCU","ARCN","ARCS","ARTH","BIOC","BIOL","BUSI","CDNS","CIED","CHEM","CHST","CHIN","CIVE","CLCV","COOP","CGSC","COMS","CCDP","COMP","CRCJ","CRST","DIGH","DBST","ERTH","ECON","ELEC","ECOR","ENGL","ESLA","EACH","ENVE","ENSC","ENST","EURR","FILM","FYSM","FOOD","FREN","FINS","GEOG","GEOM","GERM","GINS","GPOL","GREK","HLTH","HIST","HRSJ","HUMS","INDG","IDES","ITEC","INSC","IPAF","ISCI","ISAP","DIST","INAF","ITAL","JAPA","JOUR","KORE","LANG","LATN","LACS","LAWS","LING","MATH","MECH","MAAE","MPAD","MEMS","MGDS","MUSI","NSCI","NEUR","PHIL","PHYS","POLM","PSCI","PORT","PSYC","PAPM","PADM","RELI","RUSS","SXST","SOWK","SOCI","SPAN","STAT","SREE","SYSC","TSES","WGST"]
    text = open("input.txt","r").read()
    lines = text.split("\n")
    coursesDict = {}
    for line in lines:
        i = -1
        words = line.split(" ")
        for word in words:
            i+=1
            if (word[1:5] in course_names) and (words[i+2][1:].isupper()):
                    name = word[1:5]
                    if name not in coursesDict:
                         coursesDict[name] = {}
                    code = words[i+1]
                    if code not in coursesDict[name]:
                         coursesDict[name][code] = {}
                    section = words[i+2][1:]
                    #days
                    days = ""
                    #time
                    time = ""

                    if code == "4801" or code == "4802" or code == "4907" :
                         print("test")

                    #prof
                    prof = "null"
                    index = -1
                    placeholder = ""
                    while prof == "null":
                        if(words[index] == "\tYes") or (words[index] == "\tNo"):
                            prof = placeholder
                        else:
                            placeholder = words[index] + " " + placeholder
                            index -=1
                    prof = prof[1:-1]
                    #online
                    online = ""
                    #tutorial
                    if len(section) == 2:
                         tutorial = True
                    else:
                         tutorial = False
                    
                    if (prof == "  " or prof == " ") and tutorial:
                         prof = coursesDict[name][code][section[0:1]].prof

                    object = Course(name, code, section, days, time, prof, online, tutorial)
                    coursesDict[name][code][section] = object
    return coursesDict
#name, code, section, days, time, prof, online, tutorial

if __name__ == "__main__":
    main()