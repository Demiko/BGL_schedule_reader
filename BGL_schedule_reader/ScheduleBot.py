import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from datetime import datetime, date

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
        #self.updater.start_polling()
        dt = datetime.now()
        self.logger.info("Started at %s", dt.isoformat())
        #self.updater.idle()
        dt = datetime.now()
        self.logger.info("Stopped at %s", dt.isoformat())

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
        self.logger.exception('today handler is not implemented.')

        pass

    def _tomorrow(self, update: Update, context: CallbackContext):
        '''Handler for /tomorrow command'''
        self.logger.exception('tomorrow handler is not implemented.')
        pass

    def _week(self, update: Update, context: CallbackContext):
        '''Handler for /week query'''
        self.logger.exception('week handler is not implemented.')
        pass

    pass
