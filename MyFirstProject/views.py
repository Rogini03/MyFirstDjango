from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def homepage(response):
#     msg="""<html>
# <head>
# <title>Homepage</title>
# </head>
# <body>
# <h1>This is  homepage</h1>
# <h2><a href="register/">Click here</a> to Register</h2>
# <h2><a href="login/">Click here</a> to Login</h2>
# <h2><a href="payment/">Click here</a> to Payment</h2>
# </body>
# </html>"""
#     return HttpResponse(msg)

def home(request):
    dic={"name":"Ram","age":"30"}
    return render(request, template_name="firstapp\\homepage.html",context=dic)
def register(response):
    msg="""<html>
<head>
<title>Register</title>
</head>
<body>
<h2>This is  Register Application</h2>
</body>
</html>"""
    return HttpResponse(msg)

def login(response):
    msg="""<html>
<head>
<title>Login</title>
</head>
<body>
<h2>This is Login Application</h2>
</body>
</html>"""
    return HttpResponse(msg)

def payment(response):
    msg="""<html>
<head>
<title>Payment</title>
</head>
<body>
<h2>This is Payment Application</h2>
</body>
</html>"""
    return HttpResponse(msg)