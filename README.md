## The intrduction of the project   

This project is going to build our small website.In this website,we can sign up with our E-mail and log in.When we logged on to the website,we can share our favorite books,movies,and more.That other readers can comment on your posts.So let's enjoy anyway.   

The project is budiding by the flask,so let’s just do it.    

As we all is known,if we want to build a project,we should design the whole architecture of the project.So I'll list the folders and files bellow.   

- movies_books_and_more
  - \_pycache_(the cache folder of the whole project,it’s good to ignore this)
  - App
    - forms(we are adding)
      - \_\_init\_\_.py
    - models(we are adding)
      - \_\_init\_\_.py
    - static(we are adding)
      - css
        - bootstrap
          - bootstrap-theme.css
          - ···
        - main.css
      - img
        - 404.jpg
        - return_top.png
      - js
        - bootstrap
        	- bootstrap.js
        	- bootstrap.min.js
        - jquery-1.11.3.min.js
    - templates(we are adding)
      - common
      	- base.html
    - views(we are adding)
      - \_\_init\_\_.py
    - \_\_init\_\_.py
    - email.py
    - extensions.py
    - settings.py
  - migrations(database migration files in the folder.But we don't edit them directly)
  - LICENSE(this is a license file,just ignore this)
  - manage.py
  - README.md
  - requirement.txt 

 ```bash
# This project is building in the virtualenv,if your virtual 
# If your virtualenv doesn't have a flask environment,just run the command bellow
source <name of your virtualenv>/bin/active
pip install requirement.txt
 ```

## The Seccond Day   

Today I added some new files in the folder which called templates,the files are the error-page of the website.I had writed the function to capture the error.the function is in the file which named “\_\_init\_\_.py” that is in the folder which called App.It’s seems like that.    

 ```python
def errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/error404.html')
	@app.errorhandler(500)
    def server_error(e):
        return render_template('errors/error500.html')
 ```

Of cause I know it can be better.But,my ability is limited, level is average,so it’s my way.    

 I certainly did more than that today.I writed the “manage.py”,as we all is know,this file is used to run server.It need too complicated.So I writed it like this.

```python
from flask_script import Manager
from flask_migrate import MigrateCommand

from App import createApp

app = createApp('default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

In addition to that,I also edited the “extensions.py” and “settings.py”.Emmmm,ok,just browse them in the project by yourself.    

By the way,to build a website is too tired.  