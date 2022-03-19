from flask import render_template, flash
from app import app
from app.entryForm import LoginForm
from datetime import datetime
import json
# ...


@app.route('/entry', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # variable to keep counter of rows
        with open('./fileStorage.json', 'r') as f:
            storage_data = json.load(f)
        if not storage_data:
            row_counter = 0
        else:
            row_counter = 1
            last_row = storage_data[-1]
        row_number = last_row['No']
        row_counter = row_number + 1
        
        # data variables from user input
        dateIn = form.date_in.data.strftime("%m-%d-%Y")
        dateOut = form.date_out.data.strftime("%m-%d-%Y")
        data = [form.name.data, form.crates.data, dateIn, dateOut]
        
        # dict store data
        storage_dict = {'No': row_counter, 'data': data}
        
        # list with all dicts, for easier data retrival
        storage_data.append(storage_dict)

        # data to json then to json file
        with open('fileStorage.json', 'w') as json_file:
            json.dump(storage_data, json_file)

        flash(storage_dict)
        flash(storage_data)

    return render_template('entryForm.html', title='Entry Form', form=form)


@app.route('/inventory', methods=['GET'])
def inventory():
    # load storage
    with open('./fileStorage.json', 'r') as f:
        storage_data = json.load(f)
    data = storage_data
    total_produce = 0

    for val in data:
        total_produce += val['data'][1]

    # flash(data)
    return render_template('inventory.html', data=data, total_produce=total_produce)
