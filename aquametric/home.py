from flask import abort, Blueprint, current_app, jsonify, redirect, render_template, send_file, url_for
import os

from . import util

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/sensor/<sensor_id>')
def sensor(sensor_id):
    
    sensor_config = current_app.config["SENSOR_CONFIG"]
    data_dir = current_app.config["DATA_DIR"]
    logfile = util.get_logfile_path(data_dir, sensor_id)

    if sensor_id not in util.get_sensor_list(sensor_config):
        abort(500, "Sensor ID is not in the sensor list.")
    if not os.path.isfile(logfile):
        abort(500, "No data exists for the sensor.")

    sensor_info = util.get_sensor_info(sensor_id, sensor_config)

    return render_template(
        'sensor.html',
        sensor_name=sensor_info["prettyname"],
        sensor_id=sensor_id,
        sensor_image=sensor_info["img"]
    )

@bp.route('/sensors.json')
def sensorconfig():
    return send_file(current_app.config["SENSOR_CONFIG"])

@bp.route('/units.json')
def data_units():
    return jsonify(util.data_units)

@bp.route('/favicon.ico')
def favicon():
    return send_file(
        os.path.join(current_app.root_path, 'static/images/favicon.ico'),
        mimetype='image/vnd.microsoft.icon'
    )
