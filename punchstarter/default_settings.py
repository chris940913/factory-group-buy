import os
import cloudinary

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"

SECURITY_REGISTERABLE=False
SECURITY_SEND_REGISTER_EMAIL=False
SECURITY_EMAIL_SENDER="Punchstarter"

cloudinary.config( 
  cloud_name = "dv4lxe8mc", 
  api_key = "885263157388338", 
  api_secret = "qhuRowVVn0yh3llAd7r4i24iPB0" 
)