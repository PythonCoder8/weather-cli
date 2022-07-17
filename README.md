# weather-cli
A command line program to find the weather of a city selected by the user. Written in python 3. It uses the [openweathermap.org](openweathermap.org) api to receive a json file and filter out ingormation from the json received. 

This program uses the [pprint](https://docs.python.org/3/library/pprint.html) module and the [requests](https://pypi.org/project/requests/) module. Pprint is already installed with python 3 but requests isn't.

Install requests using either of the following commands:

```
pip install requests
pip3 install requests
```
When running the program it will prompt the user to enter a city. To be specific and make sure that it shows the weather of the right city, type in the country too.

For example, if you wanted to find the weather in Toronto, you would type:

```
Toronto, CA
```

If you wanted to find the weather in Los Angeles, you would type:

```
Los Angeles, US
```
