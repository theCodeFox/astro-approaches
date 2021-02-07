# astro-approaches

### **App Overview**
Information app utilising NASA’a API (Asteroids - NeoWs) to track near Earth objects. Gives basic info on asteroids and how many close approaches are due in the coming week utilising some basic metrics. The page is simple, clean and responsive.

---

### **Tech**
Python: verion 3.9.0

Flask: version 1.1.2

Charts JS: [Cloud Flare 1.0.2](https://cdnjs.cloudflare.com/)

---

### **Code Home**
Repo: [astro-approaches](https://github.com/theCodeFox/astro-approaches) 

---
### **How to View**
You will need some technical knowledge and access to github/git so you can pull down and run the code. You may also need to install or update your python and flask the the versions above
1. open terminal/command line/bash (dealers choice)
2. cd into area you are happy to copy the repo to
3. git clone https://github.com/theCodeFox/astro-approaches.git
4. cd into repo (cd astro-approaches)
5. create a new txt file called PI_Key.txt to hold your free NASA API key in the same layer as this readme
6. create a .gitignore file to ignore that file and protect your API key in the same layer as this readme
7. go to https://api.nasa.gov/ and sign up for a free API key
8. put that key in the text file
9. check everything is saved
10. in your terminal type; python ./main.py

Note: this should spin up this mini project into your default browser. I have left the project with debug mode on as it is not currently set up to be deployed. If it doesn't spin up, but is showing as running in your terminal, you can also use the following url; http://127.0.0.1:5000/