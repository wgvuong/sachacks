# sachacks - Smiskify
Spotify Data Visualizer Web App developed for SacHacks but Andrew Tri Tran, Kelly Phan, Ryan Hang, and William Vuong

##### Table of Contents  
* [General Info](#general-info)  
* [Technologies](#technologies)
* [Dependencies](#dependencies) 
* [Setup](#setup)
   
## General Info
The web application uses the Spotify API to analyze your top songs of the last 6 months to determine what personality-based Smiski matches your music taste! Intaking the song attributes of your top listens, we assign you a Smiski based on your most defining feature from your music. It is our unique approach to building a data visualizer from Spotify.

## Technologies
Project is created with:
- Visual Studio Code
- HTML and CSS
- Python 3.10 and Flask
- Python API and OAuth 2.0
  
## Dependencies
Ensure you have the following dependencies installed using 'pip'
Flask: A web application framework for Python
```
$ pip install Flask
```
Request: A library for making HTTP requests
```
$ pip install requests
```
Config: A configuration file management
```
$ pip install config
```

## Setup 
Prequisites: Python 3.10 or later is required to run this. You can download it from python.org<br />
Installation: Clone our repository<br />
Configuration:<br />
- Spofify API Credentials: Create a Spotify Developer account and register your application to get the client ID and client secret.Set these values in your configuration file or as environment variables.
- Config File: Adjust the config.py file with your configuration settings.

```
$ python main.py
or
$ python3 main.py
```

