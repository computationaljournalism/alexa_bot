# -*- coding: utf-8 -*-
''' Simple wrapper library for Flask Ask to simplify the setup (mostly decorators)
'''
from flask import Flask
from flask_ask import Ask

class AlexaBot(object):
    ''' Simple class which moves the Flask Ask decorators to simple config
    '''

    def __init__(self, config):
        # set up the Flask app
        self.app = Flask(__name__)
        self.ask = Ask(self.app, '/')

        # load config
        # the config is a list of lists (keeping w/ what the students know from Eliza):
        # 0: intent name
        # 1: intent method to call
        for intent_config in config:
            intent_name = intent_config[0]
            func = intent_config[1]

            if intent_name == 'launch':
                # special case the 'launch' method
                func = self.ask.launch(func)
            elif intent_name.lower().startswith('on_playback'):
                # special case 'on_playback'
                # get the method name from the string
                method = getattr(self.ask, intent_name)
                func = method(func)
            else:
                func = self.ask.intent(intent_name)(func)

    def start(self, debug=False):
        ''' start it up
            Note: debug=True does not play well with jupyter notebook
        '''
        # start it up
        self.app.run(debug=debug)
