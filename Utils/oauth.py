from pathlib import Path
from cryptography.hazmat.primitives import serialization
import jwt
import uuid
from datetime import datetime, timedelta
from Database.Schema.schema import AccountSchema


def generate_jwt():
    now = datetime.utcnow()
    payload = dict(
        iss="http//auth.coffeemesh.io/",
        sub=str(uuid.uuid4()),
        aud="http://127.0.0.1:8000/new_user",
        iat=(now + timedelta(hours=24)).timestamp(),
        scope="openid"
    )
    # private_key_text = Path("private_key.pem").read_text()
    # private_key = serialization.load_pem_private_key(private_key_text.encode(), password=None)

    return jwt.encode(payload=payload, algorithm="RS256")  # key=private_key


print(generate_jwt())
