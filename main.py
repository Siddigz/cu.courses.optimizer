class Course:
    def __init__(self, name, code, section, days, time, prof, online, tutorial):
        self.name = name # "COMP"
        self.code = code # "1405"
        self.section = section # "C"   
        self.days = days # "Tue Thu"
        self.time = time # "11:35 - 12:55"
        self.prof = prof # "Yanan Mao"
        self.online = online # False
        self.tutorial = tutorial # False     


def main():
    parseText()




def parseText():
    course_names = ["AERO","AFRI","ASLA","ANTH","ALDS","ARAB","ARCY","ACSE","ARCH","ARCC","ARCU","ARCN","ARCS","ARTH","BIOC","BIOL","BUSI","CDNS","CIED","CHEM","CHST","CHIN","CIVE","CLCV","COOP","CGSC","COMS","CCDP","COMP","CRCJ","CRST","DIGH","DBST","ERTH","ECON","ELEC","ECOR","ENGL","ESLA","EACH","ENVE","ENSC","ENST","EURR","FILM","FYSM","FOOD","FREN","FINS","GEOG","GEOM","GERM","GINS","GPOL","GREK","HLTH","HIST","HRSJ","HUMS","INDG","IDES","ITEC","INSC","IPAF","ISCI","ISAP","DIST","INAF","ITAL","JAPA","JOUR","KORE","LANG","LATN","LACS","LAWS","LING","MATH","MECH","MAAE","MPAD","MEMS","MGDS","MUSI","NSCI","NEUR","PHIL","PHYS","POLM","PSCI","PORT","PSYC","PAPM","PADM","RELI","RUSS","SXST","SOWK","SOCI","SPAN","STAT","SREE","SYSC","TSES","WGST"]
    text = open("input.txt","r").read()
    lines = text.split("\n")
    for line in lines:
        i = -1
        words = line.split(" ")
        for word in words:
            i+=1
            if (word[1:5] in course_names) and (words[i+2][1:].isupper()):
                    name = word[1:5]
                    code = words[i+1]
                    section = words[i+2][1:]
                    #days
                    days = ""
                    #time
                    time = ""
                    #prof
                    if code == "4701":
                         print("test")
                    test = words[-3]
                    if(words[-3] == "\tYes") or (words[-3] == "\tNo"):
                        prof = words[-2] + " " +words[-1]
                    else:
                        prof = words[-3] + " " + words[-2] + " " +words[-1]
                    prof = prof[1:]
                    #online
                    online = ""
                    #tutorial
                    if len(section) == 2:
                         tutorial = True
                    else:
                         tutorial = False

                    print(name, code, section, days, time, prof, online, tutorial)
#name, code, section, days, time, prof, online, tutorial

if __name__ == "__main__":
    main()