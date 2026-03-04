from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def read_excel():
    df = pd.read_excel("data.xlsx")
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 