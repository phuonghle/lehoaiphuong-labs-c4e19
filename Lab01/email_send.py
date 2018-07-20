from random import choice
from gmail import GMail, Message
import datetime

html_content ="""
<p>Dear thầy gi&aacute;o,</p>
<p>{{sickness}} Hnay c xin nghỉ nhe!&nbsp;<img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
<p><strong>C Phg</strong></p>
"""

excuses = ["Chị bị ốm.", "Chị ngủ quên.", "Chị mệt.", "Chị đi chơi.", "Chị đi công tác."]

html_to_send = html_content.replace("{{sickness}}", choice(excuses))



gmail = GMail("camelliachan092@gmail.com", "passs")
msg = Message("Xin nghỉ học", to="hoaiphuonglpk@gmail.com", html=html_to_send)


# 20130075@student.hust.edu.vn


looping = True
while looping:
    now = datetime.datetime.now()
    if now.hour == 7:
        gmail.send(msg)
        break





