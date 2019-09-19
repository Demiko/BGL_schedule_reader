import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

class ScheduleBot:
    """A Telegram BGL schedule bot."""
    def __init__(self, token):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.updater = Updater(token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler('start', self._start))
        dp.add_handler(InlineQueryHandler(self._inline))
        pass

    def Start(self):
        '''Start the bot. Will block until stopped!'''
        self.updater.start_polling()
        self.updater.idle()

    def _start(self, update, context):
        '''Message when /start is used.'''
        self.logger.debug('')
        update.message.reply_text("Привет. Я могу подсказать тебе расписание Лиги Настольных Игр.")
        pass

    def _inline(self, update, context):
        '''Handler for inline queries'''
        self.logger.exception('inline handler is not implemented.')
        pass

    def _today(self, update, context):
        '''Handler for /today command'''
        self.logger.exception('today handler is not implemented.')
        pass

    def _tomorrow(self, update, context):
        '''Handler for /tomorrow command'''
        self.logger.exception('tomorrow handler is not implemented.')
        pass

    def _week(self, update, context):
        '''Handler for /week query'''
        self.logger.exception('week handler is not implemented.')
        pass

    pass
