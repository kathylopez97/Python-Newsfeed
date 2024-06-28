# this functions showcase current datetime 
from datetime import datetime
#filters are simliar to helpers in a node.js
#focus formatting date month date and year
def format_date(date):
  return date.strftime('%m/%d/%y')

print(format_date(datetime.now()))
# URL formatting 
# removed all info from string
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]
# similar to consolelog 
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))
# filters
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word
print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))