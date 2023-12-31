# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Og2xlJ1VgCBB-8raQVVJs_UPIZyJaKcQ
"""

from tkinter import*
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox
#creating a class from the fpdf module so that we can use the methods present in it
class PDFCV(FPDF):
  def header(self):
    self.image("mywebsite.png",10,8,33,title="Portfolio Site")

  def footer(self):
    pass

  def generate_cv(self,name,email,phone_number,address,skills,work_experience,education,about_me):
    self.add_page()
    self.ln(20)

    self.set_font("Arial","B",26)
    self.cell(0,10,name,new_x="LMARGIN",new_y="NEXT",align="C")

#adding contact info header
    self.set_font("Arial","B",26)
    self.cell(0,10,"Contact information",new_x="LMARGIN",new_y="NEXT",align="L")


    self.output("cv1.pdf")



def generate_cv_pdf():
    name=entry_name.get()
    email=entry_email.get()
    phone=entry_phone.get()
    address=entry_address.get()
    website= entry_website.get()
    skills=entry_skills.get("1.0",END).strip().split('\n')#no amount of skills you enter we put it on the new line and seperate it by a space
    work_experience=[]
    education=[]
    work_experience_lines=entry_experience.get("1.0",END).strip().split('\n')
    for line in work_experience_lines:
        title, description = line.split(":")
        work_experience.append({'title':title.strip(),'description':description})

    education_lines = entry_education.get("1.0",END).strip().split('\n')
    for line in education_lines:
        degree, university= line.split(":")
        education.append({'degree':degree.strip(),'university':university.strip()})

    about_me=entry_about_me.get("1.0",END)

    #CREATING A QRCODE
    qrcode=pyqrcode.create(website)
    qrcode.png("mywebsite.png,scale=6")

    if not name or not email or not phone_number or not address or not skills or not edication or not work_experience or not about_me:
      messagebox.showerror("Error","Please fill in all the details")
      return

    cv= PDFCV()
    cv.generate_cv(name,email,phone_number,address,skills,work_experience,education,about_me)


window=Tk()
window.title("CV Generator")

label_name=Label(window,text="Name: ")
label_name.pack()
entry_name=Entry(window)
entry_name.pack()

label_email=Label(window,text="Eame: ")
label_email.pack()
entry_email=Entry(window)
entry_email.pack()

label_phone=Label(window,text="Phone: ")
label_phone.pack()
entry_phone=Entry(window)
entry_phone.pack()

label_address=Label(window,text="Address: ")
label_address.pack()
entry_address=Entry(window)
entry_address.pack()

label_website=Label(window,text="Website: ")
label_website.pack()
entry_website=Entry(window)
entry_website.pack()

label_skills=Label(window,text="Skills(Enter one skill per line")
label_skills.pack()
entry_skills=Text(window,height=5)
entry_skills.pack()

label_education=Label(window,text="Education(One per line in the format 'Degree': University")
label_education.pack()
entry_education=Text(window,height=5)
entry_education.pack()

label_experience=Label(window,text="Experience(Enter one per line in format'Job title': Description of the job")
label_experience.pack()
entry_experience=Text(window,height=5)
entry_experience.pack()

label_about_me=Label(window,text="About Me")
label_about_me.pack()
entry_about_me=Text(window,height=5)
entry_about_me.pack()

button_generate=Button(window,text="Generate CV")
button_generate.pack()

window.mainloop()

!pip install fpdf