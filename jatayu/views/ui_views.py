from jatayu.controller.util import import_devices
from jatayu import app


@app.route('/devices')
def devices():
    devices = import_devices()
    return {'Devices': devices}
