import requests
import html5lib
import re
from bs4 import BeautifulSoup

s = requests.Session()
url_login = 'https://accounts.douban.com/login'
url_contacts = 'https://ww.douban.com/people/***/contacts'
'''
source: None
redir: https://www.douban.com
form_email: fxyfdf_test@126.com
form_password: 126fxyfdf_test
captcha-solution: window
captcha-id: QnfplsXMAyPAueTDpeuU9ONz:en
login: 登录
'''
#https://accounts.douban.com/login?alias=zhanghao&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1027
formdata = {
    'redir':'https://www.douban.com',
    'form_email':'fxyfdf_test@126.com',
    'form_password':'126fxyfdf_test',
    'login':u'登录'
}
# 模拟一个 浏览器头信息
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
r = s.post(url_login,data = formdata, headers = headers )
content = r.text
#print (content)
# 解析验证码
soup = BeautifulSoup(content,'html5lib')
# 如果有图片就有验证码
captcha = soup.find('img', id = 'captcha_image')
#如果有验证码处理验证码信息
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    '''
    formdata = {
        'redir': 'https://www.douban.com',
        'form_email': 'fxyfdf_test@126.com',
        'form_password': '126fxyfdf_test',
        'login': u'登录'
    }
    '''
    r = s.post(url_login, data = formdata, headers = headers)
    print (r)
    #print (r.text)
with open('douban_login.html','w+',encoding='utf-8') as f:
    f.write(r.text)


