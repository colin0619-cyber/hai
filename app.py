pip install flask

from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Valentine's Day Invitation</title>
<style>
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-family: Arial;
  text-align: center;
}

button {
  margin: 10px;
  padding: 10px 20px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.yes { background: green; }
.no { background: red; }
</style>
</head>

<body>

<img id="image" src="https://media.tenor.com/VIChDQ6ejRQAAAAj/jumping-bear-hearts-no-png.gif">
<h1 id="question">Will you be my Valentine? 💘</h1>

<button id="yesBtn" class="yes">Yes</button>
<button id="noBtn" class="no">No</button>

<script>
let noClicks = 0;

const phrases = [
"Pretty please? 🥺",
"But we'd be so cute together! 💕",
"One more chance, pookie?",
"Don't break my heart :(",
"What about a maybe?",
"Please don't do this to me, I'm fragile"
];

const yesBtn = document.getElementById("yesBtn");
const noBtn = document.getElementById("noBtn");
const img = document.getElementById("image");
const question = document.getElementById("question");

yesBtn.onclick = () => {
  img.src = "https://media.tenor.com/f1xnRxTRxLAAAAAj/bears-with-kisses-bg.gif";
  question.innerHTML = "Yay!!! 💖🎉";
  noBtn.style.display = "none";
  yesBtn.style.display = "none";
};

noBtn.onclick = () => {
  noClicks++;
  yesBtn.style.fontSize = (16 + noClicks * 20) + "px";

  if(noClicks <= phrases.length){
    noBtn.innerHTML = phrases[noClicks-1];
  }
};
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)