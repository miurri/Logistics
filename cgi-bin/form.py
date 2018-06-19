from jinja2 import Template
import cgi
import html
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

form = cgi.FieldStorage()
text1 = form.getfirst("Starting point:", "Undefined")
text2 = form.getfirst("Destination point:", "Undefined")
text1 = html.escape(text1)
text2 = html.escape(text2)
temp = Template('''<iframe
                    width="1150"
                     height="700"
                src ="https://www.google.com/maps/embed/v1/directions?key=AIzaSyDkYAEwn9PMqFnBNcb8YpfB0HR__NVpATA&origin={{ t1 }}&destination={{ t2 }}&avoid=tolls|highways" allowfullscreen>
                </iframe>''')
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Estimated Route</title>
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../../assets/js/html5shiv.js"></script>
      <script src="../../assets/js/respond.min.js"></script>
    <![endif]-->
</head>
<style>
    body {
        padding-top: 0px;
        background: url(http://subtlepatterns.com/patterns/lightpaperfibers.png) repeat 0 0;
        }
    .jumbotron {
      margin: 0px 0;
      text-align: center;
      background-color:white;
    }
    .jumbotron h1 {
      font-size: 52px;
      line-height: 1;
      font-weight: bold;
    }
</style>
        <body>
        <div class="jumbotron" style="background-color: #EFEFEF;">
        <h1>Computing your route</h1>
        <p class="lead">Below is the most convenient route for your points.</p>
    </div>

    <hr>

    <div class="container">
        <div class="row output">

            <div class="col-xs-6">""")
print("<h3>Starting point: {}</h3>".format(text1))
print("""</div>
<div class="col-xs-6">""")
print("<h3>Destination point: {}</h3>".format(text2))
print("""</div>
 </div>""")
t = temp.render(t1=text1, t2=text2)
print("""<div class="row-fluid"
<div class="span12">""")
print(t)
print("""</div>
</div>
    </div>
    <script src="js/jquery.js"></script>
  	<script src="js/bootstrap.min.js"></script>
</body>
</html>""")
