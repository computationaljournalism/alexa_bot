# -*- coding: utf-8 -*-
''' example of how to use our AlexaBot wrapper class for Flask Ask
'''
from alexa_bot import AlexaBot
from flask_ask import statement, question, session

def launch():
    ''' launch intent
    '''
    return question('Welcome to our bot! What would you like to do?')

def no():
    ''' no intent
    '''
    return statement("no? really?")

def yes():
    ''' yes intent
    '''
    return question("ok, great! no what would you like to do next?")

def quit():
    ''' quit intent
    '''
    return statement("good bye. Sorry to see you go")

def person(person):
    ''' person intent - will pass in the person's name
    '''
    print("person: '%s'" % person)
    if person:
        return statement("%s did not done." % person)
    else:
        return question("i didn't catch that name. can you please try that again?")

def main():
    ''' set up config and start the bot
    '''
    config = {
        ('launch', launch),
        ('AMAZON.StopIntent', quit),
        ('AMAZON.NoIntent', no),
        ('AMAZON.YesIntent', yes),
        ('PersonIntent', person),
    }
    bot = AlexaBot(config)
    bot.start()

if __name__ == '__main__':
    main()
