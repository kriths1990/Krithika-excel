from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def read_excel():

    df = pd.read_excel("data.xlsx")

    data = df.to_dict(orient="records")

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)