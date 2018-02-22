# -*- coding: utf-8 -*-
''' Simple wrapper library for Flask Ask to simplify the setup (mostly decorators)
'''
from flask import Flask
from flask_ask import Ask

class AlexaBot(object):
    ''' Simple class which moves the Flask Ask decorators to simple config
    '''

    def __init__(self, config):
        # set up the app
        self.app = Flask(__name__)
        self.ask = Ask(self.app, '/')

        # load config
        for intent_name, func in config:
            # the config is a list of tuples with:
            # intent name
            # intent method to call 

            if intent_name == 'launch':
                # special case the 'launch' method
                func = self.ask.launch(func)
            else:
                func = self.ask.intent(intent_name)(func)

    def start(self, debug=True):
        ''' start it up
        '''
        # start it up
        self.app.run(debug=debug)
