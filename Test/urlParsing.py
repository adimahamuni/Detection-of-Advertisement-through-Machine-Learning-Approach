import urllib
with urllib.request.urlopen('http://www.google.co.uk') as f:
    if f.read().find('text/javascript') == 0:
        print("has JS")
        
        
o = urllib.parse.urlparse("http://www.google.com")

o.geturl()









#if urllib.urlopen('http://www.google.co.uk').read().find('text/javascript') == 0:
  #  print ("It has js.")