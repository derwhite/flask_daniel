import base64
from flask import Flask, request, json
from waitress import serve

app = Flask(__name__)

list_decode = lambda inp: [x for x in base64.b64decode(inp).decode().split("#")]


@app.route("/get/<id>", methods=["GET"])
def get(id):
    try:
        out = list_decode(id)
    except:
        return "error", 400
    with open("flask_server/default.html", "r") as f:
        html_raw = f.read()
    ans = ""
    for i, v in enumerate(out, 1):
        if not "[" in v:
            ans += f"{i}.&nbsp;&nbsp;{v}<br>"
        elif "[" in v:
            tmp = [x.strip() for x in v.strip()[1:-1].split(",")]
            ans += f"{i}. <br>"
            for j, w in enumerate(tmp, 0):
                ans += f"&nbsp;&nbsp;{chr(j+ord('a'))})&nbsp;&nbsp;{w}<br>"

    html_raw = html_raw.replace("{%loesung%}", ans)
    return html_raw, 200


if __name__ == "__main__":
    app.run(debug=True)
    # serve(app, host="127.0.0.1", port=5000)
