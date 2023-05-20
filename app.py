from flask import Flask, render_template, request, redirect
import sys
sys.path.insert(0, 'db/')
from os import system
from service.studentservice import *

app=Flask(__name__)

header:list = ["id","idno","lastname","firstname","course","level","ImageSRC","action"]
slist:list = []

upload_folder="static/images"
app.config["UPLOAD_FOLDER"]=upload_folder
imagename=""

@app.route("/upload",methods=['POST','GET'])
def upload():
    global imagename
    if request.method=="POST":
        file = request.files['webcam']
        idno = request.args.get("idno")
        imagename=upload_folder+"/"+idno+".jpg"
        file.save(imagename)
        return redirect("/")

@app.route("/deletestudent",methods=["GET"])
def delstudent():
    idno:str = request.args.get("idno")
    print("Deleting student with idno:", idno)
    deletestudent(idno=idno)
    return redirect("/")

@app.route("/savestudent",methods=["POST"])
def savestudent():
    if request.method=="POST":
        flag:int = int(request.form["flag"])
        idno:str = request.form["idno"]
        lastname:str = request.form["lastname"]
        firstname:str = request.form["firstname"]
        course:str = request.form["course"]
        level:str = request.form["level"]
        global imagename
    
    if flag == 1:
        updaterecord("student",id=id,idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=imagename)
    else:
        ok = addstudent(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=imagename)
    return redirect("/")

def displayall()->list:
    students:list = getallstudent()
    student_list = []
    for s in students:
        student_dict = s.copy()
        student_list.append(student_dict)
    return student_list

@app.route("/")
def index():
    slist = displayall()
    return render_template("index.html", title = 'Student List', list=slist, header_list=header)

if __name__=="__main__":
    app.run(debug=True)