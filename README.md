# E6156 - Topics in SW Engineering: Cloud Computing<br>First Example Microservice

__Author:__ Donald F. Ferguson

## Local Project Execution

### Setup

- The first step for local project execution is to create a [virtual environment](https://docs.python.org/3/library/venv.html).
This is a best practice for developing, testing and running multiple Python applications
on a single system. There are many [explanatiosn online](https://realpython.com/python-virtual-environments-a-primer/)
for the benefits of virtual environments.


- There are several approaches to creating a venv. I recommend setting up the environment
using [PyCharm's built in wizard/tools.](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)


- Activate the virtual environment. You can do this in PyCharm by opening a terminal window inside
PyCharm. There should be a terminal tab at the bottom of the PyCharm window.


- In the terminal, type ```pip install -r requirements.txt``` This will install the necessary
Python packages.

  
- You can now execute the application by using the ```run``` feature in PyCharm or directly
from the terminal prompt line by typing ```python main.py```


- You will see an initialization (logging) messages followed by the message
```
 Uvicorn running on http://0.0.0.0:8012 (Press CTRL+C to quit)
```


### Execution

- Click on ```http://0.0.0.0:8012``` link to open in the browser. You can also copy and past the link.
You will see something of the form

| <img src="./browser-screen-1.png"> |
| :---: |
| __Simple Execution__ |


- Accessing the URL ```http://0.0.0.0:8012/docs``` will navigate to the [OpenAPI](https://www.openapis.org/)
page/documentation for the application.


### Modification

1. Create a new GitHub project and clone the project.<br><br>
2. Change the name of the author in ```README.md```<br><br>
2. Copy the code from this example into the directory for the project.<br><br>
3. Follow the steps for:
   1. Creating a virtual environment for your version of the project.
   2. ```pip``` installing ```requirements.txt```
   3. Executing and accessing the application.
4. In ```main.py,``` modify the line ```return {"message": f"Hello {name}"}``` to return
a message of the form ```return {"message": f"Awesome cloud developer dff9 says Hello {name}"}```
Replace my uni with yours.
5. Rerun the application to test.


### Publish


<hr>

__Note:__
- The default behavior for virtual environment creation is to
create the venv in the current folder/project.
- You can create the venv anywhere on the file system.
- You do not want to venv pushed to GitHub. So, if the venv is inside the
project, remove the directory from the set of files that will be pushed.
The easiest way is to add to a [.gitignore file.](https://git-scm.com/docs/gitignore)

<hr>

<br>

- Commit and push your application to the GitHub repository.


- You have completed the first part of the initial assignment.




