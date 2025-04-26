from flask import Flask, redirect, url_for
app = Flask(__name__)  #Flask constructor or  creates the Flask app

# #decorator used to tell which URL is associated with function
@app.route('/') #defines home route(/) or can use like ('/home')
def hello(): #creates a function that is bound with ‘/‘ route and returns “HELLO” when the root page is accessed
    return 'Hello!'

#decorator used to tell which URL is associated with function
#define string fun
@app.route('/home/<name>') #defines home route(/)
def hello_name(name): #creates a function that is bound with ‘/‘ route and returns “HELLO” when the root page is accessed
    return 'Hello %s!' %  name

#define int function
@app.route('/num/<int:age>')
def num(age):
    return "I am %d years old" % age

#define float function
@app.route('/part/<float:secNo>')
def section(secNo):
    return "Section number is %f" % secNo

#Build a URL in Flask
@app.route('/user/<role>')
def hello_user(role):
    if role == "admin":
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('hello_name', name = role))

if __name__ == "__main__":
    app.run(debug=True) #runs the app in debug mode. It ensure that app is not need to restart manually if any changes are made in code
    
