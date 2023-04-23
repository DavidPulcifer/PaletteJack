
# Palette Jack

![Screen Shot](README_assets/screenshot.png)

Palette Jack generates colors based on text descriptions using GPT 3. 

This is a Flask app based on the Palette Generator project from Colt Steele's OpenAI course on Udemy. Type in a description of a mood, idea, place or anything and this app will generates 2 to 8 colors that fit your description.

## Usage

Type in a descripiton of a mood, idea, place or anything and this app will generates 2 to 8 colors that fit your description.

Click a color to copy the Hex Code to your clipboard.

By default Palette Jack adds to the existing palette when you click Submit. To start fresh, check the 'Replace' checkbox and submit a new prompt and all the colors will be cleared before rendering new colors.

Right click a color to delete it from the palette.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/DavidPulcifer/PaletteJack.git
cd PaletteJack
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory of the project:

```bash
touch .env
```

2. Add your OpenAI API key to the `.env` file:

```ini
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

To run the Flask app, execute the following command:

```bash
python app.py
```

The app should now be running on `http://127.0.0.1:5000/`. Open your browser and navigate to the URL to use Palette Jack.

## Contributing

To contribute to this project, please submit an issue or create a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://www.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Colt Steele's Open AI Course](https://www.udemy.com/course/mastering-openai/)
```

