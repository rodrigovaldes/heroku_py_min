# Simple python job in Heroku

## Notes

1. It's recommended that you create a virtual environment before starting to set-up your app.

```bash
virtualenv vsp
```
Hint: vsp is the name of the virtual environment, you may want to modify that

2. To create the requirements.txt file, you can always use
```bash
pip freeze > requirements.txt
```

3. You do not need a Procfile

4. The app.json file helps to run vim in the dynos.
```bash
heroku run bash -a my-app
```
