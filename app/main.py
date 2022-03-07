from fastapi import FastAPI, File, status
from fastapi.responses import FileResponse
from .services import get_lighting_locations

app = FastAPI()


@app.post("/", status_code=status.HTTP_200_OK, response_class=FileResponse)
def lighting_plans(file: bytes = File(...)):
    """
    This endpoint takes a txt file and returns a PDF file with the lighting plans.\n
    It's color coded to show free spaces, light positions and walls.\n
    Yellow: Light positions\n
    Dark gray: Walls\n
    Light gray: Free spaces
    """
    return FileResponse(
        get_lighting_locations(file),
        media_type="application/pdf",
        filename="lighting_diagram.pdf",
    )
