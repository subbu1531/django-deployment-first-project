from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):   # view-function (/welcome/)
    print("welcome/ url is request & display() is Excueted");
    ss="<h2 style='color:green;'><center>Hello Subbu! Welcome to First Django Project First-App</h2><hr color='red' width='80%' size='5'/></center>";
    return HttpResponse(ss) ;
    

def show(request):  #/welcome2/
    ss ='''<center>
			<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color="brown" width="45%"/>
		</center>''';
    return HttpResponse(ss);
    
    
#*** Working with other applications***    
def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
				}
				h2{
					color:Green;
				}
				h3{
					color:Red;
				}
				h1,h2,h3{
					background-color:plum;
					width:60%;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='80%'/>
				<h3>Have a nice day...</h3>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
#-------------------------------------------
#*** Another application***    
import time;
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
				}
				h2{
					color:Green;
				}
				h3{
					color:Red;
				}
				h1,h2,h3{
					background-color:plum;
					width:60%;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='80%'/>
				<h3>''',ct,'''</h3>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
    
#   *** Multiple URLs for same views function *** 
  
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);


#-------------------
#   ***default-url-request-view-func***
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
