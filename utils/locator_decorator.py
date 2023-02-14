from playwright.sync_api import Locator
from utils.logger import logger


class LocatorDecorator:

    @classmethod
    def decorate_locator_methods(self):
        original_click = Locator.click
        original_fill = Locator.fill

        def click(self):
            logger.info("clicked " + self._impl_obj._selector)
            try:
                original_click(self)
            except Exception as err:
                logger.info(err)
            logger.info("after " + self._impl_obj._selector)

        def fill(self, value):
            logger.info("filled " + self._impl_obj._selector + " with: " + value)
            try:
                original_fill(self, value)
            except Exception as err:
                logger.info(err)
            logger.info("filled " + self._impl_obj._selector + " with: " + value)

        Locator.click = click
        Locator.fill = fill
