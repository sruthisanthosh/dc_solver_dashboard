# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>DC Dashboard</title>
</head>
<body>
<h2>Welcome To DC Dashboard</h2>

<p>Current Results</p>

</body>
</html>

"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()