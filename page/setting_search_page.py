import page
from base.base_action import BaseAction


class SettingSearch(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)


    def click_search_btn(self):
        self.click_element(page.search_setting_param)

    def send_search_input(self,content):
        self.send_keys_content(page.search_input_param,content)


    def click_back_btn(self):
        self.click_element(page.back_param)
