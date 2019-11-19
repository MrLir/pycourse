#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#设置发送邮件的邮箱属性
mail_host = 'smtp.chinaunicom.cn'#服务器
mail_port = 25#端口
mail_user = 'lir35@chinaunicom.cn'#用户名
mail_pass = '******'#口令

#发送邮件
sender = 'lir35@chinaunicom.cn'
message = MIMEText('你好，李瑞的Python作业 ', 'plain', 'utf-8')
message['From'] = Header("lir35@chinaunicom.cn", 'utf-8')
subject = 'lir35的Python作业'
message['Subject'] = Header(subject, 'utf-8')


#开始连接服务器，并根据csv文件完成发送
try:
    #连接SMTP邮箱服务器
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)

    #读取csv文件，循环发送邮件
    with open("recvMailList.csv","rb") as recv_emails_file:
        lines = csv.reader(recv_emails_file)
        for line in lines:
            recv = line[1]
            message['To'] = Header(line[0], 'utf-8')
            smtpObj.sendmail(sender, recv, message.as_string())#发送邮件
            print("邮件发送成功")
    smtpObj.quit() #断开连接
except smtplib.SMTPException:
    print("Error: 无法发送邮件" + smtplib.SMTPException.message)