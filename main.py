"""
The application must satisfy these requirements:

    Written in Python 3.8 or later.
    Endpoints to create, read, list, update, and delete objects called "Widgets"
    Widget objects include the following properties (at least):
        Name (utf8 string, limited to 64 chars)
        Number of parts (integer)
        Created date (date, automatically set)
        Updated date (date, automatically set)
    Widgets are persisted to and retrieved from a SQLite file database.
    Include a README that describes how to setup and run the application.

Ideas to make the project even better:

    Include unit or functional test coverage
    Include an OpenAPI spec  -  make a swagger
    PEP8 compliance  - No spaghetti!
    Pass standard lint tests (ie: flake8 or similar)  -  like SonarLint (Don't make it buggy)
    Pass bandit security analysis  -  Able to pass CheckMarx
    Use Python type annotations """


#Database should be in local memory
#Maybe use flask for a clean front end?

from frontEnd import *
from backEnd import *


if __name__ == '__main__':
  #startDatabase()
  #insert()
  #update()
  #print(readAll())
  #print(read('Tim'))
  #delete(a8)
  #deleteAll()
  app.run()
