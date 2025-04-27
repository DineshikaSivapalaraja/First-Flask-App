#Send form data
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student_form():
    return render_template('student.html')

# @app.route('/enroll', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template('enroll.html', enroll = result)

students = [] #global list to store the student data

@app.route('/enroll', methods=['POST'])
def student_info():
    if request.method == "POST":
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        course = request.form['course']
        
        # save the student data into the list
        students.append({
            'student_name': student_name,
            'student_id': student_id,
            'course': course
        })
        
        return render_template('enroll.html', students=students)
        
        # to store one data
        #return render_template('enroll.html', student_name = student_name, student_id = student_id, course = course)
    
if __name__ == "__main__":
    app.run(debug=True)
    
