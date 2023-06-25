from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
import requests
from bs4 import BeautifulSoup as BSoup
from mynewsapp.models import HeadLine
# Create your views here.
def Home(request):
    template = loader.get_template('mynewsapp/index.html')
    return HttpResponse(template.render())
def Detail(request):
    temp = loader.get_template('mynewsapp/details.html')
    return HttpResponse(temp.render())
def Scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://indianexpress.com/"
    content = session.get(url,verify=False).content
    soup = BSoup(content,"html.parser")
    News = soup.find_all('div',{"class":"other-article"})
    for article in News:
        main = article.find_all('a')[0]
        link = main['href']
        img = article.find('img')
        image_src =img['src']
        title = article.find('h3').text 
        hd = HeadLine()
        hd.title=title
        hd.url = link
        hd.image=image_src
        hd.save()
    return redirect("../")

def news_list(request):
    headlines = HeadLine.objects.all()[::-1]
    context={
        'object_list':headlines,
    }
    # template = loader.get_template('mynewsapp/home.html')
    # return HttpResponse(template.render())
    return render(request,"mynewsapp/home.html",context)
