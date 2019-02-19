# Simple python job in Heroku

## Notes

+ It's recommended that you create a virtual environment before starting to set-up your app.

```bash
virtualenv vsp
```
Hint: vsp is the name of the virtual environment, you may want to modify that

+ To create the requirements.txt file, you can always use
```bash
pip freeze > requirements.txt
```

+ You do not need a Procfile

+ The app.json helps to use bash in dynos. The code below opens bash in a heroku dyno
```bash
heroku run bash -a my-app
```

+ To see that this is running, you can use:
```bash
heroku run python app.py
```
You should see a message: **Yes, you did it! This is running!**
