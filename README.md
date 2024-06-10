# Simple python job in Heroku

---
## What is Heroku?
+ An application platform
+ Push the code. They take care of the rest.
+ No servers, no instances, not –a lot– of configurations.
+ Front-End and Back-end

---
## Requirements

1) You must open a [Heroku account](https://www.heroku.com/)
2) Install Heroku in the command line
```
brew tap heroku/brew && brew install heroku
```
3) Log in
```
heroku login
```

---
## Structure of the code

+ Minimum files:
    1. ```app.py``` (you can use other names)
    2. ```requirements.txt``` >> python packages you need

+ Sometimes, you need two more files:
    1. ```runtime.txt``` >> specify that you're using python
    2. ```Procfile``` >> simple text file without extension

+ Note: You must not modify the names of the files
---
## Code in the repo
| File        | Content           |
| ------------- |:-------------:|
| .gitignore      | avoid pushing files you do not need in the cloud|
| app.json      | installs vim in Heroku |   
| app.py | main code|
|requirements.txt | python packages to install|

---
## Run the app
1. Create a virtual environment
```bash
virtualenv vsp
```
Hint: vsp is the name of the virtual environment, you may want to modify it

2. Install the packages you need
```
pip install NameOfPackage1
pip install NameOfPackage2
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
## Notes
+ Use ```heroku run bash``` to see a terminal running in a dyno (heroku 'server')
+ Basically, use ```heroku run``` as a prefix and do whatever you want
