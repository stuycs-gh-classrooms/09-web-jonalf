#!/usr/bin/python
print('content-type: text/html\n)'

import cgitb
cgitb.enable()

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
<body>
"""

HTML_FOOTER = """
</body>
</html>
"""


data = cgi.FieldStorage()
name = 'batman'
if ('name' in data):
    name = data['name'].value

print(HTML_HEADER)
print('<h1>Hello ' + name + '</h1>')
print(HTML_FOOTER)
