import requests
import json
from markdownify import markdownify as md

r = requests.get("https://arts.nthu.edu.tw/api/exhibitions?typeOfArt=visual_art")
"""
---
registration_link: null
draft: false
title: Juanjo Novella公共藝術個展
cover: https://i.imgur.com/GpcVKk0h.jpg
date: 2020-05-20T08:49:47.832Z
categories:
  - public_art
host: 清大藝術中心
performer: Juanjo Novella
location: 藝術中心展覽廳
start_date: "2018-05-08"
end_date: "2018-06-07"
daily_start_time: "22:00"
daily_end_time: "18:00"
ticket_info: null
subtitle: null
---
"""
if r.status_code != 200:
    print("Error")
else:
    exhibitions = r.json()
    

    #print(exhibitions)
    print(len(exhibitions))

    for e in exhibitions:
        output_str = ""
        output_str += "---\n"
        output_str += "title: " + e["title"] + '\n'
        output_str += "categories:\n  - " + e["type"] + '\n'
        output_str += "start_date: \"\" + e["start_date"] + "\'\"\n"
        output_str += "end_date: \"\" + e["end_date"] + "\'\"\n"
        output_str += "draft: false\n"
        output_str += "date: 2020-05-20T08:49:47.832Z\n"
        if(e["subtitle"]):
            output_str += "subtitle: " + e["subtitle"] + '\n'
        if(e["host"]):
            output_str += "host: " + e["host"] + '\n'
        if(e["performer"]):
            output_str += "performer: " + e["performer"] + '\n'
        if(e["location"]):
            output_str += "location: " + e["location"] + '\n'
        if(e["daily_start_time"]):
            output_str += "daily_start_time: \"\" + e["daily_start_time"] + "\'\"\n"
        if(e["daily_end_time"]):
            output_str += "daily_end_time: \"\" + e["daily_end_time"] + "\'\"\n"
        if(e["registration_link"]):
            output_str += "registration_link: " + e["registration_link"] + "\n"
        if(e["ticket_info"]):
            output_str += "ticket_info: " + e["ticket_info"] + "\n"
        
        output_str += "---\n\n"
        
        output_str += md(e["description"])
        print(output_str)
        with open("output/" + e["start_date"] + "-" + e["title"] + ".md", "w", encoding="utf-8") as fp:
            fp.write(output_str)
        