from flask import request, render_template, redirect, url_for, flash

from . import app, db
from .models import Position, Employee
from .forms import PositionForm, EmployeeForm

def index():
    title = 'список сотрудников'
    employees = Employee.query.all()
    return render_template('index.html', employees=employees, title=title)


def position_create():
    title = 'создание новой позиции'
    form = PositionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'позиция №{position.id} успешно добавлена', 'success')
            return redirect(url_for('index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'ошибка в поле "{field}", текст ошибки: {error}', 'danger')

    return render_template('position_form.html', form=form, title=title)

def position_delete(position_id):
    position = Position.query.filter_by(id=position_id).first()
    if request.method == 'GET':
        return render_template('position_delete.html', position=position)
    if request.method == 'POST':
        db.session.delete(position)
        db.session.commit()
        flash(f'позиция №{position.id} успешно удалена', 'success')
        return redirect(url_for('position'))

def position_update(position_id):
    position = Position.query.filter_by(id = position_id).first()
    form = PositionForm(request.form, obj=position)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(position)
            db.session.commit()
            flash(f'позиция №"{position.id}" успешно обновлена', 'success')
            return redirect(url_for('index', position_id=position.id))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'ошибка в поле "{field}", текст ошибки: {error}', 'danger')
    return render_template('position_form.html', form=form, position=position)

def employee_create():
    title = 'создание нового сотрудника'
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'сотрудник №{employee.id} успешно добавлен', 'success')
            return redirect(url_for('index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'ошибка в поле "{field}", текст ошибки: {error}', 'danger')

    return render_template('employee_form.html', form=form, title=title)

def employee_detail(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return render_template('employee_detail.html', employee=employee)

def employee_delete(employee_id):
    employee = Employee.query.filter_by(id = employee_id).first()
    form = EmployeeForm(request.form)
    if request.method == 'GET':
        return render_template('employee_delete.html', employee=employee, form=form)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        flash(f'сотрудник №{employee.id} успешно удален', 'success')
        return redirect(url_for('index'))

def employee_update(employee_id):
    employee = Employee.query.filter_by(id = employee_id).first()
    form = EmployeeForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.commit()
            flash(f'сотрудник №{employee.id} успешно обновлен', 'success')
            return redirect(url_for('employee_detail', employee_id=employee_id))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'ошибка в поле "{field}", текст ошибки: {error}', 'danger')
    return render_template('employee_form.html', form=form, employee=employee)