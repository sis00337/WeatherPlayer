from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class WordSearchForm(FlaskForm):

    """Create the form."""

    word_search = StringField('Search', validators=[InputRequired()],
                              render_kw={"placeholder": "Please enter City Name"})
    submit = SubmitField('Generate Playlist!')

