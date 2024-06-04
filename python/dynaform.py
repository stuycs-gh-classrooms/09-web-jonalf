#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html

def make_form(radio_options):
    html = """
    <form action="dynaform.py" method="GET">
    Who are you? <input type="text" name="name" value="Bob">
    <br>
    """
    radio = ''
  
    for option in radio_options:
        iput = '<div>'
        iput+= '<input type="radio" name="bgcolor" value="' + option + '">'
        iput+= option + '</div>'
        radio+= iput
    
    html+= radio
    html+= '<input type="submit" value="Submit!">'
    return html



data = cgi.FieldStorage()
#check if any form data present
if (len(data) != 0):
    name = 'batman'
    if ('name' in data):
        name = data['name'].value
    bgcolor = 'DarkSeaGreen'
    if ('bgcolor' in data):
        bgcolor = data['bgcolor'].value
    body = '<body style="background-color: '
    body+= bgcolor + ';">'
    body+= '<h1>Hello ' + name + '</h1>'
    body+= '<br><a href="dynaform.py">Try Again</a>'
    html = make_html('Form Result', body)
    print(html)
#if no form data, return the form html instead of result
else:
    body = '<h1>Form Test</h1>'
    body+= make_form(['LightPink', 'LightSkyBlue'])
    html = make_html('Form Results', body)
    print(html)
