from flask import Flask, render_template

app = Flask(__name__)

#Criar a Pagina 1

#route --> spamtong.org/

#função --> Oque exibir na pagina

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/spamton")
def secret():
    return "[[Holy Cow]] you found this secret!"
    
@app.route("/user/<uoi>")
#ioa = info or account
#uoi = user or info

def info(uoi):
    if uoi == "mike":
        return render_template("uoi.html",name="..mike..", des="Someon, please... help me..", img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxuqznLUJ0wUa8R1E_2MdU_aJt6JWFlYymGw&usqp=CAU", tamanho="200")
    if uoi == "spamton":
        return "You know me?"
    else:
         return "<p><h1>Error 404</h1></p> <p>Page not found</p>"
         
    

#colocar site no ar
if __name__=="__main__":
    app.run(debug=True)