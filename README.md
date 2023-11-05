# sachacks - Smiskify
Spotify Data Visualizer Web App developed for SacHacks but Andrew Tri Tran, Kelly Phan, Ryan Hang, and William Vuong

##### Table of Contents  
* [General Info](#general-info)  
* [Technologies](#technologies)
* [Dependencies](#dependencies) 
* [Setup](#setup)
   
## General Info
This project is a react application of a weather app taken from https://openweathermap.org's API. It displays an image and search bar on the left hand side and the current forecast along with the upcoming day ahead on the right hand side. This weather app uses React useState for state management, react-icons for styling, moment for parsing data objects, and environment variables.

## Technologies
Project is created with:
- Visual Studio Code
- HTML and CSS
- Python 3.10, Flask
- Python API, OAuth 2.0
  
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
Prequisites: Python 3.10 or later is required to run this. You can download it from python.org
Installation: Clone our repository
Configuration:
- Spofify API Credentials: Create a Spotify Developer account and register your application to get the client ID and client secret.Set these values in your configuration file or as environment variables.
- Config File: Adjust the config.py file with your configuration settings.

```
$ python main.py
or
$ python3 main.py
```

