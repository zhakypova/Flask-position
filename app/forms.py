from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, \
    SubmitField, SelectField, validators, ValidationError, DateField

from .models import Position, Employee

class PositionForm(FlaskForm):
    name = StringField(label="название должности", validators=[validators.DataRequired()])
    department = StringField(label="название отдела", validators=[validators.DataRequired()])
    wage = IntegerField(label="ставка з/п", validators=[validators.DataRequired()])
    submit = SubmitField(label="сохранить позицию")

    def validate_wage(self, wage):
        if wage.data is None:
            raise ValidationError('поле обязательно к заполнению')
        if wage.data < 0:
            raise ValidationError('заработная плата не может быть отрицательной')

    def validate_name(self, name):
        if name.data is None:
            raise ValidationError('поле обязательно к заполнению')

class EmployeeForm(FlaskForm):
    name = StringField(label="ФИО клиента", validators=[validators.DataRequired()])
    birth_date = DateField('дата рождения')
    position_id = SelectField('id позиции')
    submit = SubmitField(label="save")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for position in Position.query.all():
            result.append((position.id, position.name))
        self.position_id.choices = result

    def validate_name(self, name):
        if name.data is None:
            raise ValidationError('поле обязательно к заполнению')

    def validate_birth_date(self, birth_date):
        if birth_date.data is None:
            raise ValidationError('поле обязательно к заполнению')






