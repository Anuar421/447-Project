from flask_table import Table, Col, LinkCol

class Results(Table):
    date = Col('date')
    county = Col('county')
    state = Col('state')