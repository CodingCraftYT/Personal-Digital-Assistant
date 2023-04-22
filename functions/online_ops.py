import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


# Function for finding IP Address

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


# Function for WikiPedia Search

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)  # sentence => number of sentence required
    return results


# Function to Play videos on Youtube

def play_on_youtube(video):
    kit.playonyt(video)  # playonyt() accepts topics as an argument. It searches on youtube and plays the most
    # appropriate video.


# Function for search on google

def search_on_google(query):
    kit.search(query)  # It has a method that helps us search on google instantly


# Function to send WhatsApp Message Function

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)  # This method only work when you're logged in whatsapp on
    # Whatsapp for web.


# function to send email function

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['subject'] = subject
        email['FROM'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


# Function to get news headlines

NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


# Function to get weather report Function

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units"
                       f"=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


# Function to get Trending Movies Function

TMDB_API_KEY = config("TMDB_API_KEY")


def get_trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


# Function to get Random Jokes

def get_random_joke():
    headers = {
        "Accept" : "application/json"
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


# Function to get random advice

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()