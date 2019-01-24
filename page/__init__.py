from selenium.webdriver.common.by import By
#
# # 显示
#
# display_text_show_param = (By.XPATH, "//*[contains(@text,'显示')]")
# search_param = By.ID, "com.android.settings:id/search"
# search_send_key_param = By.ID, "android:id/search_src_text"
#
# # 网络
#
#
# click_more_param = By.XPATH, "//*[contains(@text,'更多')]"
# click_mobile_network_param = By.XPATH, "//*[contains(@text,'移动网络')]"
# click_first_network_param = By.XPATH, "//*[contains(@text,'首选网络类型')]"
# click_change_2g_param = By.XPATH, "//*[contains(@text,'2G')]"
# click_change_3g_param = By.XPATH, "//*[contains(@text,'3G')]"
#
#
# # 短信
# new_sms_param = By.ID,"com.android.mms:id/action_compose_new"
# send_recive_param = By.ID,"com.android.mms:id/recipients_editor"
# send_input_param = By.ID,"com.android.mms:id/embedded_text_editor"
# send_button_param = By.ID,"com.android.mms:id/send_button_sms"
# new_sms_params = By.ID,"com.android.mms:id/text_view"
#
#
# # 开发者
# my_param = By.XPATH,"//*[contains(@text,'我的')"
# login_param = By.ID,"io.manong.developerdaily:id/login_btn"
# email_param = By.ID,"io.manong.developerdaily:id/btn_email"
# input_email_param = By.ID,"io.manong.developerdaily:id/edt_email"
# input_password_param = By.ID,"io.manong.developerdaily:id/edt_password"
# login_btn_param = By.CLASS_NAME,"android.widget.Button"
# login_info_param = By.ID,"io.manong.developerdaily:id/nav_tv_name"
# coin_info_param = By.ID,"io.manong.developerdaily:id/nav_btn_coin_total"
# nav_name_info_param = By.ID,"io.manong.developerdaily:id/nav_tv_name"
#

setting_app_package = "com.android.settings"
setting_app_activity = ".Settings"







# 搜索设置

#点击搜索
search_setting_param = By.ID,"com.android.settings:id/search"
#输入框输入
search_input_param = By.ID,"android:id/search_src_text"
# 点击返回
back_param = By.CLASS_NAME,"android.widget.ImageButton"


