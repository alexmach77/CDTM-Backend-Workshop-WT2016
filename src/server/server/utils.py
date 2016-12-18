from flask import abort, jsonify, make_response

def json_abort(code, text):
    # type: (object, object) -> object
    json = {
        'result': False,
        'error': {
            'status': code,
            'text': text
        }
    }
    abort(make_response(jsonify(json), code))
