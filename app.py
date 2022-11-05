from apihelper import check_endpoint_info, fill_optional_data
import dbhelper
from flask import Flask, request, make_response
import json
import dbcreds
from uuid import uuid4

app = Flask(__name__)

if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5007)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)
