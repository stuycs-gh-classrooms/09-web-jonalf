#!/usr/bin/python
print('Content-type: text/html\n')

from random import random

def make_head(title):
    head = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>
    """
    head+= title + '</title></head>'
    return head

def make_body(s):
    body = '<body>' + s + '</body></html>'
    return body

page = make_head("Lucky Number")
body = "Your lucky number is: "
body+= str(int(random()*100))
page+= make_body(body)
print(page)
