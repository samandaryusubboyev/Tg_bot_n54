import asyncio
import logging
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "A bot resumes complaints"

    async def main(self):
        from tg_bot import config
        logging.basicConfig(level=logging.INFO)
        try:
            # Start polling for the bot
            await config.dispatcher.start_polling(config.bot)
        except asyncio.CancelledError:
            logging.info("Polling canceled.")
        finally:
            logging.info("Bot shutdown cleanly.")

    def handle(self, *args, **options):
        try:
            asyncio.run(self.main())
        except KeyboardInterrupt:
            logging.info("Bot interrupted by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
