from flask import Flask, render_template

app = Flask(__name__)

#RUTA PARA EL HOME PAGE
@app.route("/")
def home():
    return render_template('home.html')
#RUTA PARA EL ABOUT PAGE
@app.route("/login")
def about():
    return render_template('login.html') 

if __name__ == "__main__":
#ESTABLECEMOS EL SERVIDOR DE PRUEBA (SE REFRESCA SOLO).
    app.run(debug= True)