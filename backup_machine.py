#备份文件到百度网盘
import easygui
import selenium
from selenium import webdriver
import time
import os
#嗯~还是一个面向过程的写法
#Open_and_go_to_the_page_and_prepare_for_everything_needed:
user_agent={'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.\
4183.102 Safari/537.36'}
#print(user_agent)
options=webdriver.ChromeOptions()
options.add_argument('user-agent={}'.format(user_agent))
bs=webdriver.Chrome()
bs.get('https://www.weiyun.com/')
bs.switch_to_frame('qq_login_iframe')
time.sleep(3)   #加这一步是因为，之前总是找不到下面的元素，可能是因为页面还没加载出来就开始定位元素了，肯定定位不到啊
bs.find_element_by_id('switcher_plogin').click()
loginbtn=bs.find_element_by_id('login_button')
#这个函数是专门用来登记qq号和密码，接收两个字符串，供后续使用
def get_input():
    user_name_input=input('请输入你的用户名（qq号），按回车结束\n')
    password_input=input('请输入密码，按回车结束\n')
    print(user_name_input,password_input)
    return (user_name_input,password_input)
#这个函数是专门用来登录，接收两个字符串
def login(user_name,password):
    user_name_box=bs.find_element_by_class_name('inputstyle')
    user_name_box.send_keys(user_name)
    mima=bs.find_element_by_id('p')
    mima.send_keys(password)
    time.sleep(2)
    loginbtn=bs.find_element_by_id('login_button')
    loginbtn.click()
    print('已点击登录按键')

def press_upload():
    uploadbtn=bs.find_element_by_id('formFileInputCt')
    uploadbtn.click()
    print('已点击上传按键')
    filebtn=bs.find_element_by_xpath("//span[@class='txt']")
    filebtn.click()
    print('已点击文件按键')

def get_and_run_the_exe():
    #path=easygui.fileopenbox()
    os.system('Handle_upload_dialoge.exe')
    print('已调用上传程序')

def main():
    while True:
        try:
            usname,psword=get_input()
            login(usname,psword)
            time.sleep(5)
            press_upload()
            break
        except:
            bs.refresh()
            time.sleep(5)
            print('用户名密码有误，请重新输入')
            bs.switch_to_frame('qq_login_iframe')
            bs.find_element_by_id('switcher_plogin').click()
            time.sleep(5)
            user_name_box=bs.find_element_by_class_name('inputstyle')
            user_name_box.clear()
    time.sleep(3)
    get_and_run_the_exe()
    print('恭喜你，文件备份成功！给我点个赞吧？')
    time.sleep(5)
    bs.quit()

main()

