# date:2019-9-12
# author:sc
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "32024826@qq.com"
mail_pwd = "yucrlukkkyoocaaf"

sender = '32024826@qq.com'
receiver = "shencheng_1014@aliyun.com"

message = MIMEText('python smtp 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header("QQ", 'utf-8')
message['To'] = Header("aliyun", 'utf-8')

subject = 'Python SMTP 邮箱测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 25 为 SMTP 常用端口号  QQ邮箱 需要使用ssl
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("发送失败")
