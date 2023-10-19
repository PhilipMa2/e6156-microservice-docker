from flask import Flask

app = Flask(__name__)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Awesome cloud developer dff9 says hello {name}"}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8012)
