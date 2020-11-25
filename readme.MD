# docker-fastapi-graphene-sqlalchemy

Deploy your [GraphQL](https://graphql.org/) backend easily based on [graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy) with [FastAPI](https://fastapi.tiangolo.com/) using [Docker](https://www.docker.com/), with examples for CRUD operations triggered by graphQL


## Features
* [FastAPI](https://fastapi.tiangolo.com/)with [Uvicorn](https://www.uvicorn.org/)
* Python based GraphQL library(Graphene) 
* [SQLAlchemy](https://www.sqlalchemy.org/)
* Code examples
* Added MySQL and [PhpMyAdmin](https://www.phpmyadmin.net/) support


## Installation

1. Copy and set up your own `.ENV` file with your own username/password

```
cp example.env .ENV
```
2. Build volume for db storage
```
docker volume create --name=fastapi-db
```
3. Build and start docker containers 
```
docker-compose up -d
```
4. visit
* GraphiQL UI [http://localhost:5000](http://localhost:5000)
* PhpMyAdmin UI [http://localhost:8080](http://localhost:8080)

## Example Queries
* Create Department if not exist
```
mutation createDepartment {
  createDepartment(department: {name: "Engineering"}) {
    department {
      name
    }
  }
}
```

* Create an employee with required department and role, link to existing department/role if possible

```
mutation createEmployee {
  createEmployee(role: {name: "QA"}, department: {name: "Engineering"}, employee: {name: "Tom"}) {
    employee {
      name
      department {
        name
      }
      role {
        name
      }
    }
  }
}
```
* Return all employees
```
query getEmployee {
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
        role {
          name
        }
      }
    }
  }
}
```
* Return employee with certain id
```
query getEmployee {
  employee(eid: 1) {
    name
    department {
      name
    }
    role {
      name
    }
  }
}
```


## Credits
* Database model from [graphene-sqlalchemy examples](https://github.com/graphql-python/graphene-sqlalchemy/tree/master/examples/flask_sqlalchemy)
* SQLAlchemy operations from [demo-graphql-sqlalchemy-falcon](https://github.com/somada141/demo-graphql-sqlalchemy-falcon)