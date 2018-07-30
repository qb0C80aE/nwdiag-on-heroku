#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
from flask import Flask, request, send_file, abort, make_response, jsonify
import os
import subprocess
from threading import Lock

app = Flask(__name__)
lockObject = Lock()

def synchronized(lock):
    def wrap(f):
        def newFunction(*args, **kw):
            lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                lock.release()
        return newFunction
    return wrap

@app.route('/', methods=['POST'])
@synchronized(lockObject)
def create_diagram():
    f = open('input.json', 'wb')
    f.write(request.data)
    f.close()

    width = request.args.get('width')
    if (width is None) or (not width.isnumeric()):
        width = '320'

    height = request.args.get('height')
    if (height is None) or (not height.isnumeric()):
        height = '240'

    imagetype = request.args.get('imagetype')
    outputfile = 'output.png'
    if imagetype != 'png':
        imagetype = 'svg'
        outputfile = 'output.svg'

    cmd = ['nwdiag', '-T', imagetype, '-a', '--size', width + 'x' + height, '-o', outputfile, 'input.json']
    proc = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    if proc.returncode != 0:
        abort(make_response(jsonify(message=proc.stderr.decode('utf8')), 400))

    if imagetype == 'png':
        return send_file(outputfile, mimetype='image/png')
    else:
        return send_file(outputfile, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
