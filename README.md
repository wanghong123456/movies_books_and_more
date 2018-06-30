## The intrduction of the project   

This project is going to build our small website.In this website,we can sign up with our E-mail and log in.When we logged on to the website,we can share our favorite books,movies,and more.That other readers can comment on your posts.So let's enjoy anyway.   

The project is budiding by the flask,so let’s just do it.    

As we all is known,if we want to build a project,we should design the whole architecture of the project.So I'll list the folders and files bellow.   

- books_and_movies_and_more
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
      		- bootstrap-theme.css.map
      		- bootstrap-theme.min.css
      		- bootstrap.css
      		- bootstrap.css.map
      		- bootstrap.min.css
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

  