from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from app.models import Category
from datetime import datetime

class EditTransactionForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    category_type = HiddenField('Category Type')  # Hidden field to store category type

    def __init__(self, *args, **kwargs):
        category_type = kwargs.pop('category_type', None)  # Extract category_type if passed
        super(EditTransactionForm, self).__init__(*args, **kwargs)

        # Populate the category choices with existing categories
        categories = Category.query.all()

        # Set default category based on the provided category type
        if category_type:
            self.category_type.data = category_type
            # Separate the selected category from the others
            selected_category = [c for c in categories if category_type.lower() in c.name.lower()]
            other_categories = [c for c in categories if c not in selected_category]

            # Place the selected category at the top of the list
            self.category.choices = (
                [(selected_category[0].id, selected_category[0].name)] +
                [(c.id, c.name) for c in other_categories]
            )
        else:
            self.category.choices = [(c.id, c.name) for c in categories]

class AddTransactionForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], default=datetime.today().date())
    category = SelectField('Category', coerce=int, validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(AddTransactionForm, self).__init__(*args, **kwargs)
        # Populate the category choices with existing categories
        categories = Category.query.all()
        self.category.choices = [(category.id, category.name) for category in categories]
