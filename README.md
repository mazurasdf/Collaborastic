# Collaborastic
  Collaborastic is an ongoing project designed by UI/UX students at **Flatiron School Chicago** and developed by web development students at **Coding Dojo Chicago**.
  The application itself aims to help people plan events when they might not have all the resources to host such an event.
  
  For example, suppose I am a designer and I would like to host a class about basic design principles. I would like to find an event space and perhaps 
  a caterer because I would like to serve food at this too. I can make an event and post that I am looking for a host in Chicago. I could pay 
  them $X and would like the event to be July 3. Other users may see this and reach out wanting to collaborate.
  
## What is the tech stack in this project?
  This project is built with **Python** using **Django 3.0** and a SQLite database on the backend. The front end is built with the latest version of **React**

## How can I clone this and run on my machine?
  **First of all, please make sure you install the latest stable version of [Python 3](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/)**.
  Second thing to note is that this could potentially be simpler to do if you use an IDE with built-in terminal like [VSCode](https://code.visualstudio.com/)

  To start, download the project on your machine and open your preferred terminal.
  At any location, such as directly outside the project, you will create a virtual environment to install python dependencies.
  
  On Windows Powershell, run `py -m venv env`. On Mac/Linux/Git Bash, run `python3 -m venv env`.
  
  Next, activate your virtual environment by running `source env/bin/activate` on Mac/Linux/Git Bash or `.\env\Scripts\activate` on Powershell.
  
  Great! Let's change directories to the root project folder. We will run the following commands:
  ```
  pip install -r requirements.txt
  cd frontend/
  npm install
  ```
  We've now installed the necessary dependencies for the project. Now let's get this project running! Let's open a second terminal without closing the first one.
  
  In the new terminal, go to the project root folder and run `python manage.py runserver`.
  
  In the first terminal, run `npm run start`.
  
  :tada:***Congratulations!!**:tada: * Your server is now up and running!
  
  
  ### Questions?
  Feel free to email the repo owner, Michael Mazur, at mazurasdf at gmail.com
