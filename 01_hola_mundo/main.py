import os
import urllib
import webapp2

class MainPage(webapp2.RequestHandler):

  def get(self):
    """Return a friendly HTTP greeting"""

    self.response.headers['Content-type'] = 'text/plain'
    self.response.write('Hola Mundo!')

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
