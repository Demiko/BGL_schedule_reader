import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from datetime import datetime, date
from GameDay import GameDay

class ScheduleBot:
    """A Telegram BGL schedule bot."""
    def __init__(self, token):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.updater = Updater(token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler('start', self._start))
        dp.add_handler(CommandHandler('today', self._today))
        dp.add_handler(CommandHandler('tomorrow', self._tomorrow))
        dp.add_handler(CommandHandler('week', self._week))
        dp.add_handler(InlineQueryHandler(self._inline))
        pass

    def Start(self):
        '''Start the bot. Will block until stopped!'''
        self.updater.start_polling()
        self.logger.info("Started at %s", datetime.now().isoformat())
        self.updater.idle()
        self.logger.info("Stopped at %s", datetime.now().isoformat())

    def _start(self, update: Update, context: CallbackContext):
        '''Message when /start is used.'''
        update.message.reply_text("Привет. Я могу подсказать тебе расписание Лиги Настольных Игр.")
        pass

    def _inline(self, update: Update, context: CallbackContext):
        '''Handler for inline queries'''
        self.logger.exception('inline handler is not implemented.')
        pass

    def _today(self, update: Update, context: CallbackContext):
        '''Handler for /today command'''
        d = date.today()
        self.send_day(GameDay(d), update, context)
        pass

    def _tomorrow(self, update: Update, context: CallbackContext):
        '''Handler for /tomorrow command'''
        d = date.today()
        d = d.replace(day=d.day+1)
        self.send_day(GameDay(d), update, context)
        pass

    def _week(self, update: Update, context: CallbackContext):
        '''Handler for /week query'''
        self.logger.exception('week handler is not implemented.')
        pass

    def send_day(self, gameDay: GameDay, update: Update, context: CallbackContext):
        reply:str = 'День: %s\n' % gameDay.date.strftime('%A %d.%m')
        if not gameDay.events:
            reply+='\n'
            reply+='Запланированных игр нет.'
        for event in gameDay.events:
            reply += '\n'
            reply += '**[%s](%s)** (%s)\n' % (event.title, event.link, event.type)
            reply += '🕐: %s\n' % (event.time)
            reply += 'Свободных мест: %s\n' % (event.seats)
        reply = reply.strip('\n')
        print(reply)
        update.message.reply_markdown(reply, disable_web_page_preview=True)
        pass
    pass
