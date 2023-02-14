"""
This module contains shared fixtures.
"""

import pytest

from pages.home_page import DemoblazeHomePage
from playwright.sync_api import Page


@pytest.fixture
def home_page(page: Page) -> DemoblazeHomePage:
    return DemoblazeHomePage(page)

