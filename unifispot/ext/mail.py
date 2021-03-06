# coding: utf-8
from flask_mail import Mail 

from unifispot.utils.options import get_option_value



mail = Mail()



def configure(app):
    #load options from DB
    with app.app_context():
        #need to be ran on app context
        app.config['MAIL_SERVER']   = get_option_value('MAIL_SERVER','localhost')
        app.config['MAIL_PORT']     = str(get_option_value('MAIL_PORT',25))  
        app.config['MAIL_DEFAULT_SENDER'] = get_option_value('MAIL_DEFAULT_SENDER',
                                    'no-reply@spotipo.local')  
    
    mail.init_app(app)
