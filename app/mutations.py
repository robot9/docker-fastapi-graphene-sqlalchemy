from typing import List, Dict, Union

import graphql
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from app.models import Department as DepartmentModel
from app.models import Employee as EmployeeModel
from app.models import Role as RoleModel
from app.database import db_session, get_or_create
from app.queries import Department, Role, Employee


class InputDepartment(graphene.InputObjectType):
    name = graphene.String(required=True)


class InputRole(graphene.InputObjectType):
    name = graphene.String(required=True)


class InputEmployee(graphene.InputObjectType):
    name = graphene.String(required=True)
    hired_on = graphene.DateTime(required=False)


class MutationDepartmentCreate(graphene.Mutation):
    class Arguments:
        department = InputDepartment(required=True)
    
    department = graphene.Field(Department)
    @staticmethod
    def mutate(
        args: Dict,
        info: graphql.execution.base.ResolveInfo,
        department: InputDepartment
    ):
        db_dep = get_or_create(db_session, DepartmentModel, name = department.name)
        db_session.commit()

        return MutationDepartmentCreate(department=db_dep)


class MutationRoleCreate(graphene.Mutation):
    class Arguments:
        role = InputRole(required=True)
    
    role = graphene.Field(Role)
    @staticmethod
    def mutate(
        args: Dict,
        info: graphql.execution.base.ResolveInfo,
        role: InputRole
    ):
        db_role = get_or_create(db_session, RoleModel, name = role.name)
        db_session.commit()
        return MutationRoleCreate(role=db_role)


class MutationEmployeeCreate(graphene.Mutation):
    class Arguments:
        role = InputRole(required=True)
        department = InputDepartment(required=True)
        employee = InputEmployee(required=True)

    employee = graphene.Field(Employee)
    @staticmethod
    def mutate(
        args: Dict,
        info: graphql.execution.base.ResolveInfo,
        role: InputRole,
        department: InputDepartment,
        employee: InputEmployee
    ):
        db_role = get_or_create(db_session, RoleModel, name = role.name)
        db_session.commit()
        db_dep = get_or_create(db_session, DepartmentModel, name = department.name)
        db_session.commit()
        db_employee = EmployeeModel()
        db_employee.name = employee.name 
        if employee.hired_on:
            db_employee.hired_on = employee.hired_on
        db_employee.department = db_dep 
        db_employee.role = db_role
        db_session.add(db_employee)
        db_session.commit()
        return MutationEmployeeCreate(employee=db_employee)


class Mutation(graphene.ObjectType):
    create_department = MutationDepartmentCreate.Field()
    create_role = MutationRoleCreate.Field()
    create_employee = MutationEmployeeCreate.Field()