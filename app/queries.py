from typing import List, Dict, Union

import graphql
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from app.models import Department as DepartmentModel
from app.models import Employee as EmployeeModel
from app.models import Role as RoleModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node,)


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    all_roles = SQLAlchemyConnectionField(Role.connection)
    all_departments = SQLAlchemyConnectionField(Department.connection)
    role = graphene.Field(Role)
    employee = graphene.Field(
        Employee,
        eid=graphene.Argument(type=graphene.Int, required=False)
    )

    @staticmethod
    def resolve_employee(
        args: Dict,
        info: graphql.execution.base.ResolveInfo,
        eid: Union[int, None] = None,
    ):
        query = Employee.get_query(info=info)
        if eid:
            query = query.filter(EmployeeModel.id == eid)
        return query.first()