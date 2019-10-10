#!/usr/bin/env python3
import connexion
from flask_cors import CORS

app = connexion.FlaskApp(__name__, specification_dir = '../../openapi/')
app.add_api('specification.yaml')

# CORS added to support health check monitoring in Cucumber dashboard
CORS(app.app)
