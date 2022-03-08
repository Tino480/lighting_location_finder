# Lighting location finder

requirements:

* Python >= 3.9
* Pip

# Configuration

### Using virtual enviroments

Open a terminal navigate to the project directory and execute the following commands to install and create a virtual environment:

- pip<3> install virtualenv
- python3 -m venv env

Then you need activate you virtual enviroment, if your operating system is based on unix(macos or linux) execute the
following in your terminal:

- source env/bin/activate

or if it's windows:

- .\env\Scripts\activate

Now you need to install everything in the requirements.txt file:

- pip install -r requirements.txt

### Running the project

Once everything is installed, you can run the project utilizing the following command:

- python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000

You can now open your browser and navigate to localhost:8000/docs
