# -*- coding: utf-8 -*-
"""all functions related to INDIA"""
from urllib2 import urlopen
from flask import Blueprint, render_template
from bs4 import BeautifulSoup

INDIA = Blueprint('INDIA', __name__)


def extract_image(old_list):
    """slicing of characters to obtain correct image url"""
    new_list = []
    for member in old_list:
        member = member.replace("ALTERNATES", "alternates")
        member = member.replace("100", "300")
        member = member.replace("215", "300")
        new_list.append(member)
    return new_list


def mega_replace(old_list):
    """replacing \xecode characters"""
    for i in range(len(old_list)):
        old_list[i] = old_list[i].replace("\xe2\x80\x90", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x91", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x92", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x93", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x94", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x95", "-")
        old_list[i] = old_list[i].replace("\xe2\x80\x98", "'")
        old_list[i] = old_list[i].replace("\xe2\x80\x99", "'")
        old_list[i] = old_list[i].replace("\xe2\x80\x9d", "</strong>")
        old_list[i] = old_list[i].replace("\xe2\x80\x9c", "<strong>")
    return old_list


def data_parse(link_address):
    """return basic lists"""
    url = urlopen(link_address)
    reader = url.read()
    soup = BeautifulSoup(reader, 'lxml')
    image_list, headline, desc, main_description = [], [], [], []
    for a_tag in soup.find_all('div', attrs={"class": "story-card-33"}):
        story_card_news = a_tag.find('div',
                                     attrs={"class": "story-card-33-news"})
        link_name = story_card_news.find('a')
        if link_name['href'] == \
                "http://www.thehindu.com/opinion/interview/":
            continue
        else:
            for link in a_tag.find_all('a',
                                       attrs={
                                           "class": "story-card-33-img" +
                                                    " focuspoint"}):
                main_description.append(link['href'])
                if link.find('img'):
                    image_location = link.find('img')
                    image_list.append(image_location['data-proxy-image'])
                else:
                    image_list.append('/static/news.png')
                para = a_tag.find('p', attrs={
                    "class": "story-card-33-heading"})
                para_text = para.find('a')
                para_text = str(para_text)
                if para_text.find("span") != -1:
                    start = para_text.find("</span>") + 8
                    end = para_text.find("</a>")
                    para_text = para_text[start:end]
                    headline.append(para_text)
                    span_text = a_tag.find(
                        'span', attrs={
                            "class": "light-gray-color story-card-33-text"
                                     + " hidden-xs"})
                    span_text = span_text.text.encode('utf-8')
                    desc.append(span_text)
                else:
                    para_text = para.find('a')
                    para_text = para_text.text
                    desc.append(para_text.encode('utf-8'))
    return image_list, headline, desc, main_description


@INDIA.route('/top-3/india')
def india():
    """top 3 news for india"""
    image_list, headline, desc, main_description = \
        data_parse("http://www.thehindu.com/tag/81/india/")
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template(
        "India.html",
        N=len(image_list),
        news=image_list,
        head=headline,
        des=desc,
        main_news=main_description)


@INDIA.route('/Politics/india')
def politicsindia():
    """top politics news for india"""
    url_list = [
        "http://www.thehindu.com/tag/1422-1420-1349/political-development/",
        "http://www.thehindu.com/tag/1420-1349/politics-general/",
        "http://www.thehindu.com/tag/1349/politics/"]
    image_list, headline, desc, main_description = [], [], [], []
    for temp in url_list:
        one, two, three, four = data_parse(temp)
        image_list = image_list + one
        headline = headline + two
        desc = desc + three
        main_description = main_description + four
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template(
        "India.html",
        N=len(image_list),
        news=image_list,
        head=headline,
        des=desc,
        main_news=main_description)


@INDIA.route('/Sports/india')
def sportsindia():
    """top sports news for india"""
    url_list = [
        "http://www.thehindu.com/tag/1683-1569/cricket/",
        "http://www.thehindu.com/tag/1802-1569/soccer/",
        "http://www.thehindu.com/tag/1570-1569/hockey/",
        "http://www.thehindu.com/tag/1892-1569/tennis/",
        "http://www.thehindu.com/tag/1737-1569/marathon/",
        "http://www.thehindu.com/tag/1689-1683-1569/test-cricket/"]
    image_list, headline, desc, main_description = [], [], [], []
    for temp in url_list:
        one, two, three, four = data_parse(temp)
        image_list = image_list + one
        headline = headline + two
        desc = desc + three
        main_description = main_description + four
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template(
        "India.html",
        N=len(image_list),
        news=image_list,
        head=headline,
        des=desc,
        main_news=main_description)


@INDIA.route('/economy/india')
def economyindia():
    """top economy news for India"""
    image_list, headline, desc, main_description = \
        data_parse("http://www.thehindu.com/tag/791-684/economy-general/")
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template(
        "India.html",
        N=len(image_list),
        news=image_list,
        head=headline,
        des=desc,
        main_news=main_description)


@INDIA.route('/Technology/india')
def technologyindia():
    """top technology news in India"""
    url_list = [
        "http://www.thehindu.com/tag/1506-1461/technology-general/",
        "http://www.thehindu.com/tag/1461/science-and-technology/"]
    image_list, headline, desc, main_description = [], [], [], []
    for temp in url_list:
        one, two, three, four = data_parse(temp)
        image_list = image_list + one
        headline = headline + two
        desc = desc + three
        main_description = main_description + four
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template(
        "India.html",
        N=len(image_list),
        news=image_list,
        head=headline,
        des=desc,
        main_news=main_description)


@INDIA.route('/Entertainment/india')
def entertainmentindia():
    """top entertainment news for India"""
    url_list = [
        "http://www.thehindu.com/tag/524-428/entertainment-general/",
        "http://www.thehindu.com/tag/487-483-428/english-cinema/"]
    image_list, headline, desc, main_des = [], [], [], []
    for link_name in url_list:
        url = urlopen(link_name)
        read = url.read()
        soup = BeautifulSoup(read, 'lxml')
        for a_tag in soup.find_all('div',
                                   attrs={"class": "story-card-33"}):
            for link in a_tag.find_all('a', attrs={
                    "class": "story-card-33-img focuspoint"}):
                if link.find('img'):
                    image_link = link.find('img')
                    image_list.append(image_link['data-proxy-image'])
                else:
                    image_list.append('/static/news.png')
                main_des.append(link['href'])
            para = a_tag.find('p',
                              attrs={"class": "story-card-33-heading"})
            para_text = para.find('a')
            para_text = str(para_text)
            if para_text.find("span") != -1:
                start = para_text.find("</span>") + 8
                end = para_text.find("</a>")
                para_text = para_text[start:end]
                headline.append(para_text)
                text = a_tag.find('span', attrs={"class": "light-gray-" +
                                                          "color story-" +
                                                          "card-33-text " +
                                                          "hidden-xs"})
                text = text.text.encode('utf-8')
                desc.append(text)
            else:
                para_text = para.find('a')
                para_text = para_text.text
                desc.append(para_text.encode('utf-8'))
    image_list = extract_image(image_list)
    headline = mega_replace(headline)
    desc = mega_replace(desc)
    return render_template("India.html", N=len(image_list),
                           news=image_list, head=headline, des=desc,
                           main_news=main_des)
