#多层框架iframe switch_to.frame(iframe的id)
from lib2to3.pgen2 import driver
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://mail.qq.com")            
browser.switch_to.frame('login_frame')         #id属性为btlogin，定位到其所在iframe框架
browser.switch_to.default_content()      #切回主文档
#browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))
#iframe里没有id或者name  两种方法
#browser.switch_to_frame(browser.find_element_by_xpath("//iframe[contains(@src,'//accounts.douban.com/passport/login_popup?login_source=anony')]"))


#定位元素8种方式：
driver=webdriver.Chrome()
driver.find_element_by_id("loginName").send_keys('wenyu')  #id定位  id属性
driver.find_element_by_name("name")[0].click()  #name定位 元素的名称
driver.find_element_by_class_name("u-btn")[0].click()  #元素的类名,class值
driver.find_element_by_tag_name("input")  # tag定位，少用，html文档下各种标签，一类功能
driver.find_element_by_link_text(u"退出").click()  #页面右上方的一些个人操作
driver.find_element_by_xpath("//*[@id='Title']/input[4]").click()  # *是标签名，不指定时用*
driver.find_element_by_xpath("html/body/div/div[3]/a[1]").click()  #完整xpath路径
driver.find_element_by_css_selector("#loginName") #css属性定位.  id定位属性#  属性定位[type=submit]