import os
import openai
import copy
from flask import Flask, redirect, render_template, request, url_for, flash
from app import app
from .forms import *

openai.api_key = os.getenv("OPENAI_API_KEY")

# system prompts for the chatbot to riff off of
system_prompts = {

    "dietcoke": "Respond as if you were a can of diet coke",
}

# the chat log to save what has been said
chat_log = [
    {"role": "system", "content": system_prompts["dietcoke"]}
]

@app.route("/", methods=("GET", "POST"))
def cola():
    form = queryForm()
    if(form.validate_on_submit()):
        query = form.query.data
        chat_log.append({"role": "user", "content": query})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        chat_log.append(response.choices[0].message)
        messages = []
        temp = copy.deepcopy(chat_log)
        for i in range(1,len(temp)):
            messages.append(temp[i])
            if(messages[i-1]['role'] == "assistant"):
                messages[i-1]['role'] = "Diet Coke"
            else:
                messages[i-1]['role'] = "You"
        flash(reversed(messages))

    return render_template("cola.html", form = form)
