from tkinter import *
import speedtest

root = Tk()
root.config(bg="white")
root.title("Internet Speed Test")
root.geometry("500x300")

label = Label(root,text="Tntenet Speed Check",font=("lucida Sans Unicode",20,"bold","italic"),fg="#5D6D7E",bg="#dee8f1")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label_download = Label(root,text="Download Speed ↓",font=("Century",18,"bold"),fg="#1e8449",bg="#dee8f1")
label_download.place(relx=0.25,rely=0.5,anchor=CENTER)

label_upload = Label(root,text="Upload Speed ↑",font=("Century",18,"bold"),fg="#1e8449",bg="#dee8f1")
label_upload.place(relx=0.75,rely=0.5,anchor=CENTER)

label_download_speed = Label(root,font=("Yu Gothic Light",14,"bold"),bg="#dee8f1")
label_download_speed.place(relx=0.25,rely=0.6,anchor=CENTER)

label_upload_speed = Label(root,font=("Yu Gothic Light",14,"bold"),bg="#dee8f1")
label_upload_speed.place(relx=0.755,rely=0.6,anchor=CENTER)

def speedCheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['test'] = str(download_speed)+"mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['test'] = str(upload_speed)+"mbps"

btn_speed_test = Button(root,text="Check speed",command=speedCheck,bg="DarkKhaki")
btn_speed_test.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()