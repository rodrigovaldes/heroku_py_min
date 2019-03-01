# Simple python job in Heroku

---
# What is Heroku?
+ An application platform
+ Push the code. They take care of the rest.
+ No servers, no instances, not –a lot– of configurations.
+ Front-End and Back-end

---
# Requirements

1) You must open a Heroku account
2) Install Heroku in the command line
```
brew install heroku/brew/heroku
```
3) Log in
```
heroku login
```

---
# Structure of the code

+ You must have a file named ```requirements.txt```
... requirements.txt >> python modules you need

+ Sometimes, you may need two more files:
... ```runtime.txt``` >> specify that you're using python
... ```Procfile``` >> simple text file without extension

---
# Code in the repo
| File        | Content           |
| ------------- |:-------------:|
| .gitignore      | avoid pushing files you do not need in the cloud|
| app.json      | installs vim in Heroku |   
| app.py | main code|
|requirements.txt | python packages to install|

---
# Run the app
1. Create a virtual environment
```bash
virtualenv vsp
```
Hint: vsp is the name of the virtual environment, you may want to modify that
2. Install the packages you need
```
pip install math
```
3. Create ```requirements.txt```
```bash
pip freeze > requirements.txt
```
4. Run the code
```bash
heroku run python app.py
```
You should see a message: **Yes, you did it! This is running!**

---
# Notes
+ Use ```heroku run bash``` to see a terminal running in a dyno (heroku 'server')
+ Basically, use ```heroku run``` as a prefix and do whatever you want
