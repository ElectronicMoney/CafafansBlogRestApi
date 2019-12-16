from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return (
        """
            <div>
                <h1 style="color:green">Welcome To Cafafans Coders!!!</h1> 
                <p>We are profesional Developers!!!</p>
            </div>
        """
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT')))