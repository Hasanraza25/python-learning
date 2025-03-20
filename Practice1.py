import pyjokes
import pyttsx3
poem = '''twinkle twinkle little star,
How I wonder what you're,
Up above the world so high,
like a diamond in the sky
'''

joke = pyjokes.get_joke()
print(joke)

engine = pyttsx3.init()
engine.say(poem)
engine.runAndWait()