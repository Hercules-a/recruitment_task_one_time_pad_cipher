import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from codecs import decode

tags_metadata = [
    {
        "name": "encode",
        "description": "Set massage and keyword. Function return encoded cipher."
    },
    {
        "name": "decode",
        "description": "Set cipher and keyword. Function return decoded massage."
    }
]


app = FastAPI(title="Enigma",
              description="Encode and decode message using One-Time Pad Cipher",
              openapi_tags=tags_metadata)

security = HTTPBasic()


class Enigma(BaseModel):
    # ASCII between 32 and 126
    def encode(self, message, key):
        cipher = ""
        letter_in_message = 0
        while letter_in_message < len(message):
            for letter_in_key in key:
                result = ord(message[letter_in_message]) - 32 + ord(letter_in_key) - 32
                new_letter = chr(result + 32) if result <= 94 else chr(result - 94 + 32)
                letter_in_message += 1
                cipher += new_letter
                if letter_in_message >= len(message):
                    break
        return cipher

    def decode(self, cipher, key):
        message = ""
        letter_in_cipher = 0

        while letter_in_cipher < len(cipher):
            for letter_in_key in key:
                result = (ord(cipher[letter_in_cipher]) - 32) - (ord(letter_in_key) - 32)
                new_letter = chr(result + 32) if result >= 0 else chr(result + 94 + 32)
                letter_in_cipher += 1
                message += new_letter
                if letter_in_cipher >= len(cipher):
                    break
        return message


def authorization(credentials):
    correct_username = username
    correct_password = "password"
    if not (correct_username == credentials.username and correct_password == credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.post("/encode", tags=["encode"])
def encode_message(message, key, credentials: HTTPBasicCredentials = Depends(security)):
    authorization(credentials)
    enigma = Enigma()
    return enigma.encode(message, key)


@app.post("/decode", tags=["decode"])
def encode_message(cipher, key, credentials: HTTPBasicCredentials = Depends(security)):
    authorization(credentials)
    cipher = decode(cipher, "unicode_escape")
    enigma = Enigma()
    return enigma.decode(cipher, key)


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
