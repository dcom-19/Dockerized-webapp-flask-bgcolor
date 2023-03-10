## Dockerized-webapp-flask-bgcolor
This is a simple flask webapp that displays a colored background and a dynamic greeting message. 

### Dynamic Color
The color can be specified in two different ways:

  1. As a command line argument with --colorhexcode as the argument. Accepts one of the following colors according the list below.
  2. As an Environment variable APP_COLORHEXCODE. Accepts one of the following colors according the list below.
    
In any other case, a random color is picked from the list below.

Note 1: Accepted colors are in hex format: [#ff0000,#00ff00,#0000ff,#808000,#800080,#000080] which are red, green, blue, olive, purple and navy respectively. 
Note 2: Command line argument precedes over environment variable.

### Dynamic Title
The dynamic greeting message can be specified in two different ways:

  1. As a command line argument with --title as the argument. Accepts any text message!
  2. As an Environment variable APP_TITLE. Accepts any text message.
    
In any other case, the static text "Cloud Computing - University of West Attica" is applied.

Note 3: Command line argument precedes over environment variable.
## Follow these steps in order to create your Dockerized-webapp-flask-bgcolor

1. First of all you have to clone this repository on your server.
```bash
    mkdir -p ~/MyProjects
    cd ~/MyProjects
    git clone https://github.com/dcom-19/dockerized-webapp-flask-bgcolor.git
```
2. Now you have to build the Docker Image locally.
```bash
    cd ~/MyProjects/dockerized-webapp-flask-bgcolor
    sudo docker build . -t chatzidakis/webapp-flask-bgcolor:2.0
```
3. Now you have to spin up as many containers you want in different ports.

Random color and Static title without any command line argument nor environmental variable.
```bash
    sudo docker run -p 8002:8000 chatzidakis/webapp-flask-bgcolor:2.0
```
Blue color with environmental variable and the Static title:
```bash
    sudo docker run -p 8000:8000 -e APP_COLORHEXCODE=#00ff00 chatzidakis/webapp-flask-bgcolor:2.0
```
Navy color with command line argument and the static title:
```bash
    sudo docker run -p 8001:8000 chatzidakis/webapp-flask-bgcolor:2.0 --colorhexcode=#ff0000
```
Red color and Dynamic title with environmental variables:
```bash
    sudo docker run -p 8003:8000 -e APP_COLORHEXCODE=#00ff00 -e APP_COLORHEXCODE="Test Title" chatzidakis/webapp-flask-bgcolor:2.0
```
Olive color and Dynamic title with command line arguments:
```bash
    sudo docker run -p 8004:8000 chatzidakis/webapp-flask-bgcolor:2.0 --colorhexcode=#ff0000 --title="Test Title"
```
