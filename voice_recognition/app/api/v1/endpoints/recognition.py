from fastapi import APIRouter, UploadFile, File
import httpx
import json
from app.schemas.audio import Audio
from app.schemas.response import PostResponse
from app.core.config import settings
from app.core.utils import read_audio
from app.core.utils import delete_audio
from app.core.utils import validate_format

router = APIRouter()

@router.get('/message')
def message():
    return {'message': 'it\'s working'}


@router.post('/upload_audio', response_model=PostResponse[Audio])
async def upload_audio(file: UploadFile = File(...)):
    path: str = 'app/static/audio'
    path_audio = f'{path}/{file.filename}'
    ext: str = file.filename.split('.')[-1]

    headers: dict = {
        'authorization': f'Bearer {settings.BASE_TOKEN}',
        'Content-Type': f'audio/{ext}'
        }

    if validate_format(ext):
        with open(path_audio, 'wb') as audio:
            cont = await file.read()
            audio.write(cont)

        audio = read_audio(path_audio)
        delete_audio(path_audio)
        res = httpx.post(settings.API_WIT_AI_ENDPOINT, headers=headers, data=cont)
        res =  "[" + res.content.decode('utf-8').replace("\r", ",") + "]"  
        
        res_format = json.loads(res)
        text = res_format[-1]['text']

        return PostResponse[Audio](text=text)
    else:
        return PostResponse[Audio](text="Invalid format", message="Audio no converted")
