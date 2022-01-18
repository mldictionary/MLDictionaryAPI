<h1 align="center">
  <img alt="icon" src="./.images/logo.png">
</h1>
<h1 align="center">MLDictionary API</h1>
<h2 align="center" >
ACCESS WORDS' DEFINITIONS<br><br>
    <a href="https://github.com/PabloEmidio/api-dictionary/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/PabloEmidio/api-dictionary?style=social"></a>
    <a href="https://github.com/PabloEmidio"><img alt="GitHub followers" src="https://img.shields.io/github/followers/PabloEmidio?label=Follow%20me&style=social"></a>
</h2>

---

# ⚈ About
A Flask API to access words' definitions

language options: English, Portuguese and Spanish

---

# ⚈ Required
This application uses Docker and Docker Compose, to install access the links bellow.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker compose](https://docs.docker.com/compose/install/)

---

# ⚈ How to use

  ``` 
  [example@example]$ git clone https://github.com/PabloEmidio/api-dictionary
  [example@example]$ cd api-dictionary
  [example@example api-dictionary]$ docker-compose up -d
  [example@example api-dictionary]$ URL="http://127.0.0.1:8088"; xdg-open $URL || sensible-browser $URL || x-www-browser $URL || gnome-open $URL
  ```

## Documentation

Proper documentation can be find in [extern deploy](https://mldictionaryapi.herokuapp.com/) or using the [local docker deploy](http://127.0.0.1:8088/) in your machine.

---

# ⚈ Tech Stack

The following tools were used in the construction of the project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/tutorial/)
- [MLDictionary](https://pypi.org/project/mldictionary/)
- [Redis](https://redis.com/)
- [Json](https://www.json.org/json-en.html)

---

# ⚈ Tree Directory

``` bash
.
├── mldictionary_api
│   ├── models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── const.py
│   │   ├── meanings.py
│   │   └── requests.py
│   ├── resources
│   │   ├── __init__.py
│   │   ├── const.py
│   │   ├── response.py
│   │   └── translator.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── api.py
│   │   └── views.py
│   ├── static
│   │   ├── css
│   │   │   ├── small_screen.css
│   │   │   └── style.css
│   │   └── js
│   │       └── scripts.js
│   ├── templates
│   │   └── index.jinja2
│   ├── __init__.py
│   ├── app.py
│   └── const.py
├── Dockerfile
├── LICENSE
├── Procfile
├── README.md
├── docker-compose.yml
└── requirements.txt

8 directories, 25 files

```

---

# ⚈ Bugs and Features
<p>
Please report any type of bug. Remember that this is an open source project and will evolve with everyone's help. :)<br>
Any report will be read and will get due attention
</p><br>
<p>
New features are being done and new ideas are being created always that possible...<br>
new ideas will be accepted...
</p>

