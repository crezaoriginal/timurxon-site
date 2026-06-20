from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():

    avatar = "https://i.imgur.com/8Km9tLL.png"
    name = "Тимурхон"
    username = "timurxon"

    return render_template_string(f"""
<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>
</head>
<body style="background:black;color:white;display:flex;justify-content:center;align-items:center;height:100vh;">

<div style="text-align:center">
    <img src="{avatar}" style="width:100px;height:100px;border-radius:50%;">
    <h2>{name}</h2>
    <p>@{username}</p>

    <button onclick="go()" style="padding:15px 25px;border:none;border-radius:10px;background:#0a84ff;color:white;">
        Telegram
    </button>
</div>

<script>
function go(){{
    window.location.href = "https://t.me/{username}";
}}
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
