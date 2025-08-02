from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse
import os
import logging

LOG_FILE_PATH = "app.log"

router = APIRouter()

@router.get("/download", response_class=FileResponse)
async def download_log():
    if not os.path.exists(LOG_FILE_PATH):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log file not found")
    if not os.path.isfile(LOG_FILE_PATH):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Log path is not a file")
    if not os.access(LOG_FILE_PATH, os.R_OK):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Log file is not readable")
    return FileResponse(LOG_FILE_PATH, media_type="text/plain", filename="app.log")

@router.delete("/")
async def delete_log():
    if not os.path.exists(LOG_FILE_PATH):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log file not found")
    if not os.path.isfile(LOG_FILE_PATH):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Log path is not a file")
    if not os.access(LOG_FILE_PATH, os.W_OK):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Log file is not writable")
    try:
        open(LOG_FILE_PATH, "w").close()
        return {"detail": "Log file emptied."}
    except Exception as exc:
        logging.error(f"Error emptying log file: {exc}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error emptying log file: {exc}")