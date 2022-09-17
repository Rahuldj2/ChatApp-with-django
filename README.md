# ChatApp-with-django
## 1.Basic setup and Running instructions:

PRE-REQUISITES:
1. Visual Studio cocde
2. Python3(pip)
3. git bash(to clone repository)

Open Visual Studio code and open 'New terminal' and navigate to the folder/directory where you want to clone this repository.<br>
After this run the following commands on the terminal.
**********************************************************************************************************************************************************
### STEP 1: CLONE REPOSITORY
```
git clone https://github.com/Rahuldj2/ChatApp-with-django/
```
(All folders/files in this repository will be cloned into your system).

### STEP 2: CREATE VIRTUAL ENVIRONMENT
```
python -m venv newvirtualenv
```
Then press `ctrl`+`shift`+`p` on your keyboard to open command palette and navigate to "Python: select interpreter". <br>
Choose the root folder(where you are cloning repository) and choose "Python 3.9.7('newvirtualenv':venv) .\newvirtualenv\bin\python.exe".<br>
Restart VScode and open new terminal. Your terminal should look like this now(the path will vary of course):
![image](https://user-images.githubusercontent.com/89291885/190848271-4c528088-db8d-421f-bd5a-10ef6cd8a58b.png)

The basic setup is done. Now follow these instructions to run the django project:

### STEP 3: RUNNING THE PROJECT

Type this command on the terminal
```
cd ChatApp-with-django
```
Now you need to install django in the virtual environment. You can do this by running the command:
```
pip install django
```
then to run and view the webpage type:
```
python manage.py runserver
```
You will get this output on the terminal:
![image](https://user-images.githubusercontent.com/89291885/190853855-138eb458-ea8e-4cd6-85f7-5a9de3603f73.png)

Copy and paste the server link starting with https on google chrome to view the web page. A preview is shown below:
![image](https://user-images.githubusercontent.com/89291885/190853934-ba850d04-5cc6-4b5d-accc-c014df7d319e.png)

Now you can enter the chat room of your choice! To test the real time chat updates you can open the same link on a different tab and enter the
same chat room with different username:
![image](https://user-images.githubusercontent.com/89291885/190854189-7331c1df-7874-4897-83e2-58ca2e16cacb.png)

That is it! Hope you enjoy chatting in this app!
***************************************************************************************************************

## 2. Project Description and credits:

### ABOUT ME:
I am a novice to the field of web development and this is the first project that I have created. I built this website with the aim to hone my web development
skills and to get a first hand experience of building a website using HTML,CSS and DJANGO. I have followed various tutorials to learn web development and I would like 
to thank freeCodeCamp.org who have guided me to build this website through their tutorials on youtube.
(https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ).

### HOW TO BUILD THIS PROJECT:
An intermediate understanding of HTML(Hyper text Markup Language), CSS(Cascading style sheets) and Django is the pre-requisite for building this chat app.
Some javascript is also used in this project to provide real-time chat messaging updates.
HTML and CSS are required to build the front end i.e the structure and styles of the web page, and Django(alongwith sqlLite) is used for the backend i.e for
url routing,storing chat data etc.
