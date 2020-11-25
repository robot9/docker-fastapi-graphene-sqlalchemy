import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from app.database import engine, Base
from app.queries import Query
from app.mutations import Mutation

Base.metadata.create_all(bind=engine)

app = FastAPI()

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_route("/", GraphQLApp(schema=schema))