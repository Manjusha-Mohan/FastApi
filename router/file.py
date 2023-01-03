from fastapi import APIRouter, File, UploadFile
import shutil
from PIL import Image

router = APIRouter(
    prefix='/file',
    tags=['file']
)
# text file upload

@router.post('/file')
def get_file(file:bytes = File(...)):
    content = file.decode('utf-8')
    lines =content.split('\n')
    return {'lines':lines}

# large file
@router.post('/uploadfile')
def get_uploadfile(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(upload_file.file,buffer)
        
    return{
        'filename':path,
        'type': upload_file.content_type
    }
