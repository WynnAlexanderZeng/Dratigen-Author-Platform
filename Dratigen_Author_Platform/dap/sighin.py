from tkinter import*
from tkinter import messagebox
import zmail
import random
import time
zt=('楷体',18)
sighintrue=False
def sendyzm():
    global yzm

    try:
        yzm=random.randint(100000,999999)
        server = zmail.server('Dratigen@163.com', 'AHUTQWYOJDICNPNE')
        server.send_mail(mail.get(),{'subject':'Your Verify Code is','content_text':'【Dratigen】你的验证码是:'+str(yzm)})
        messagebox.showinfo('验证码发送成功！','已发送至您的邮箱：'+mail.get())
        for i in range(15,0,-1):
            abrrd=Label(root,text='   已发送'+str(i)+'s   ',font=('楷体',30)).grid(row=1,column=2)
            root.update()
            time.sleep(1)
        Button(root,text='重新发送验证码',font=zt,command=sendyzm).grid(row=1,column=2)
        root.update()

    except:
        if mail.get() == '':
            messagebox.showerror('错误','邮箱不能为空！')
        elif '@' not in mail.get():
            messagebox.showerror('错误','您输入的邮箱格式不对')
        else:
            messagebox.showerror('错误','没有查询到邮箱')
def sighin():
    if yzms.get() == str(yzm):
        messagebox.showinfo('登录成功','登录成功！')
        sighintrue=True
    else:
        messagebox.showwarning('错误','验证码错误')
def main():
    global mail
    global root
    global yzms

    root=Tk()
    root.title('登录')
    Label(root,text='请登录',font=zt).grid(row=0,column=0)
    Label(root,text='邮箱：　',font=zt).grid(row=1,column=0)
    mail=StringVar()
    Entry(root,textvariable=mail,font=zt).grid(row=1,column=1)
    abrrc=Button(root,text='发送验证码',font=zt,command=sendyzm).grid(row=1,column=2)
    Label(root,text='验证码：',font=zt).grid(row=2,column=0)
    yzms=StringVar()
    Entry(root,textvariable=yzms,font=zt).grid(row=2,column=1)
    Button(root,text='登录',command=sighin,font=zt).grid(row=3,column=3)
    root.mainloop()

if __name__ == '__main__':
    main()