```
# Palette Jack

Palette Jack is a color palette generator Flask web app based on the Palette Generator project from Colt Steele's OPEN AI course on Udemy. Type in a description of a mood, idea, place or anything and this app will generates 2 to 8 colors that fit your description.

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

