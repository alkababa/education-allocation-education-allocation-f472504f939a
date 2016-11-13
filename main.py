'''
Created on Nov 14, 2015

@author: Andrew and KEVIN
'''
import webapp2
import stripe
import os
from google.appengine.ext.webapp import template
# class SponsorsHandler(webapp2.RequestHandler):
#     def get(self):
#         template_values = {
#         }
#         path = os.path.join(os.path.dirname(__file__),'sponsors.html')
#         self.response.out.write(template.render(path,template_values))
# class DonateHandler(webapp2.RequestHandler):
#     def get(self):
#         template_values = {
#         }
#         path = os.path.join(os.path.dirname(__file__),'donate.html')
#         self.response.out.write(template.render(path,template_values))
# class ContactHandler(webapp2.RequestHandler):
#     def get(self):
#         template_values = {
#         }
#         path = os.path.join(os.path.dirname(__file__),'contact.html')
#         self.response.out.write(template.render(path,template_values))
class PayHandler(webapp2.RequestHandler):
    def post(self):
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_live_4KhJ5IGFikA7sHH9N0Au3ksS"

        # Get the credit card details submitted by the form
        token = self.request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=self.request.POST['amount'], # amount in cents, again
              currency="usd",
              source=token,
              description="Donation"
          )
        except stripe.error.CardError, e:
          # The card has been declined
          pass
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
class BlogHandler(webapp2.RequestHandler):
  def get(self):
      template_values = {
      }
      path = os.path.join(os.path.dirname(__file__), 'blog.html')
      self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    # ('/sponsors',SponsorsHandler),
    # ('/donate', DonateHandler),
    # ('/contact', ContactHandler),
    ('/pay', PayHandler),
    ('/blog',BlogHandler),
    ('/.*', MainHandler),

], debug=True)
