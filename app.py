from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
  { 
    'id' : 1,
    'Position' : "Data Scientist",
    'Location' : "Bengaluru, India",
    'Salary' : "Rs. 10,00000 p.a.",
      
    
  },
  {
    'id' : 2,
    'Position' : "Data Analyst",
    'Location' : "Delhi, India",
    'Salary' : "Rs. 15,00000 p.a.",
  },
  {
    'id': 3,
    'Position' : "Frontend Engineer",
    'Location' : "Remote",
    'Salary' : "Rs 12,00000 p.a",
  }

]


@app.route('/')
def hello():
  return render_template('home.html', jobs = JOBS,company_name="Jovian" ) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
