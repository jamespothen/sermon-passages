import urllib.request
import http.cookiejar # deal with cookies

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

webprefix = "https://en.wikipedia.org/wiki/"

person = input("Please give me a name (First Last): ")
websuffix = person.replace(" ", "_")

webURL = webprefix + websuffix

infile = opener.open(webURL, timeout = 15)

newpage = infile.read().decode("utf-8")

target = '"bday">'
targetindex = newpage.find(target)

if targetindex > -1:
    print("The person's birthday is", newpage[targetindex+len(target):targetindex+len(target)+10])
else:
    print("No birthday found 😢")


bdaylist = newpage.split(target) # only splits if target is found
if len(bdaylist) > 1:
    afterstring = bdaylist[1]
    bdaystring = afterstring[:10]
    print(bdaystring)
else:
    print("No bday found 😢")

infile.close()
