
with open('dc_op.txt') as file:
    dc_op = [ line for line in file ]
    print(dc_op,'\n');


f=open('GFG.html', 'w')
f.write("""<html>
<head>
<title>DC Dashboard</title>
</head>
<body>
<h2>Welcome To DC Dashboard</h2>

<p>Current Results""")

# the html code which will go in the file GFG.html
rows = [row for row in dc_op]

for i in rows:
        # writing the code into the file
        f.write(f"{i}<br>")

f.write("""</p></body>
</html>""")

# close the file
f.close()