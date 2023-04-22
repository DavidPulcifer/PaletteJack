import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

config = dotenv_values('.env')
openai.api_key = config['OPENAI_API_KEY']

app = Flask(
    __name__,
    template_folder='templates',
    static_url_path='',
    static_folder='static'
)

def generate_palette(palette_description):
    prompt = f"""
    You are a color palette generating assistant that generates color palettes from text prompts.

    Generate color palettes that fit the theme, mood, or instructions in the prompt. Generate between 2 and 8 colors.

    Desired Format: a JSON array of hexidecimal color codes

    Q: Convert the following description into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following description into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]    

    Q: Convert the following description into a list of colors: {palette_description}
    A: 
    """

    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=100,    
    )

    colors = json.loads(response['choices'][0]['text'])
    return colors
    

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get('query')
    colors = generate_palette(query)
    return {"colors": colors}


@app.route("/")
def index():    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)