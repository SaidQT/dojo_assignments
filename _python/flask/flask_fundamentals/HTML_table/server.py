from flask import Flask, render_template
app = Flask(__name__)
@app.route('/lists')
def renderlists():
    users = [
        {'firstname' : 'Michael', 'lastname' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template("index.html", users=users)

if __name__=="__main__":
    app.run(debug=True)