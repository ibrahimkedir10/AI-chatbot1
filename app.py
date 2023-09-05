# app.py

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Motivational quotes based on different issues
motivational_quotes = {
    "work": [
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Believe you can, and you're halfway there.",
    ],
    "life": [
        "Life is 10% what happens to us and 90% how we react to it.",
        "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.",
        "Your time is limited, so don't waste it living someone else's life.",
    ],
    "personal": [
        "You are never too old to set another goal or to dream a new dream.",
        "Success is walking from failure to failure with no loss of enthusiasm.",
        "Don't watch the clock; do what it does. Keep going.",
    ],
}

# Default personality (issue)
current_issue = "work"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/change_issue/<issue>")
def change_issue(issue):
    global current_issue
    current_issue = issue
    return jsonify({"message": f"Issue set to '{issue}'"})

@app.route("/get_quote")
def get_quote():
    global current_issue
    issue_quotes = motivational_quotes.get(current_issue, [])
    if issue_quotes:
        quote = random.choice(issue_quotes)
    else:
        quote = "Sorry, I couldn't find any quotes for that issue."
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(debug=True)
