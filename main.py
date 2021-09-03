import wikipedia
import pyttsx3

searchInp = input("Search: ")
result = wikipedia.search(searchInp)

for search in result:
    print(search)
    robo = pyttsx3.init()
    robo.say(wikipedia.page(search).summary)
    print(wikipedia.page(search).summary)
    robo.runAndWait()