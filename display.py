from tkinter import *
root=Tk()
root.geometry("300x250")
image=Button(root,text="Image",bd='5',height="5",width="10")
image.pack(side="left")
video=Button(root,text="Video",bd='5',height="5",width="10")
video.pack(side="left")
live=Button(root,text="live stream",bd='5',height="5",width="10")
live.pack(side="left")
root.mainloop()
