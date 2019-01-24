import pytest

from base.init_driver import get_driver
from data.read_yaml_data import read_yaml_data

from page.setting_search_page import SettingSearch


class TestSettingSearch:
    def setup_class(self):
        app_package = "com.android.settings"
        app_activity = ".Settings"
        self.driver = get_driver(app_package, app_activity)
        self.search = SettingSearch(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("content", read_yaml_data("data2.yaml"))
    def test_search_content(self, content):
        self.search.click_search_btn()
        self.search.send_search_input(content)

    def test_back_btn(self):
        self.search.click_back_btn()
