
  

# SQLAlchemy Awesome Pagination

###  [**Github**](https://github.com/ivke-99/sqlalchemy_awesome_pagination)

SQLAlchemy Awesome Pagination is a small utility library that paginates an SQLAlchemy

object and returns the results ready for api serving.

  

If you are creating a service/micro-service oriented architecture, and cannot use fastapi/flask or other frameworks built in paginations or libraries, this is for you.

  

The sole purpose of this project was creating a minimal yet effective library to be used independently of frameworks.

  
  

## Installation

  

The project requires sqlalchemy >= 1.1 installed.

  

Install with pip

  

```pip install sqlalchemy_awesome_pagination```

## Features

  

- Pagination

- Sorting by sqlalchemy column

- Sorting by direction

  
  

## Usage/Examples

**paginate()** accepts 5 params:

  

**query** - SqlAlchemy object to be paginated

  

**page_number** - Page to be returned (starts and defaults to 1).

  

**page_size** - Maximum number of results to be returned in the page (defaults

to the total results).

  

**direction** - asc/desc - defaults to asc

  

**sort_by** - table column for sorting - defaults to sqlalchemy default sorting column(mostly id)

  

```python

from sqlalchemy_awesome_pagination import paginate

from app import models

  

query =  self.db.query(

models.User.username,

models.User.email

)

  

results =  paginate(query, 2, 10, "asc", "email")

results2 =  paginate(query)

results3 =  paginate(query, 1, 15, "desc")

results4 =  paginate(query, 2, 20, None, "email")

```

  
  

## Authors

  

- [@ivke-99](https://www.github.com/ivke-99)

  
  

## Credits

  

This library is an adjusted version of the pagination module from

- [SQLAlchemy filters](https://github.com/juliotrigo/sqlalchemy-filters)

  

Big thanks to the authors and contributors for the idea!

  
  

## Contributing

  

Contributions are always welcome! :)