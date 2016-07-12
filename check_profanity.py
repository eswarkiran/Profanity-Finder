import urllib
def read():
    quo = open(r"C:\Users\Kiran\Desktop\readfile.txt")
    content=quo.read()
    print(content)
    quo.close()
    check(content)
    
def check(content):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+content)
    output = connection.read()
    if "false" in output:
        print("NO profanity")
    elif "true" in output:
        for x in range(0,3):
            print("Profanity Alert!!!")
    else:
        print("check the read file")
    connection.close()


read()
