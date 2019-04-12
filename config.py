import os


class Config:
    # app
    APP_NAME = 'PUSH TO KINDLE!'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    ACCEPTED_FILE_TYPES = ['.jpeg', '.jpg', '.gif', '.png', '.doc', '.docx', '.html', '.htm', '.rtf', '.mobi', '.azw', '.bmp', '.pdf', '.txt']
    # mailgun
    MG_DOMAIN_NAME = 'push.tokindle.top'
    MG_API_KEY = os.environ.get('MG_API_KEY')
    MG_EMAIL_FROM = 'please@%s' % MG_DOMAIN_NAME
    MG_EMAIL_FROM_USER = '%s <%s>' % (APP_NAME, MG_EMAIL_FROM)
    MG_EMAIL_SUBJECT = 'convert'
    MG_EMAIL_TEXT = 'Documents have been pushed to your kindle.'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'http://127.0.0.1:5000'
    MG_EMAIL_TO = os.environ.get('MG_EMAIL_TO_FOR_TEST')


class ProductionConfig(Config):
    DEBUG = False
    HOST = os.environ.get('PRODUCTION_HOST')
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}