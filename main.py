from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import paintcalx

app = FastAPI(title="PaintCalx API", description="Professional paint calculation API")

class PaintVolumeRequest(BaseModel):
    total_surface: float
    door_window_surface: float
    wall_type: str
    coat_count: int
    coverage: float
    custom_coefficients: Optional[Dict[str, float]] = None

class ComponentProportionsRequest(BaseModel):
    total_volume: float
    proportions: Dict[str, float]

class UnitConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str

@app.post("/calculate/paint-volume")
async def calculate_paint_volume_endpoint(request: PaintVolumeRequest):
    try:
        result = paintcalx.calculate_paint_volume(
            total_surface=request.total_surface,
            door_window_surface=request.door_window_surface,
            wall_type=request.wall_type,
            coat_count=request.coat_count,
            coverage=request.coverage,
            custom_coefficients=request.custom_coefficients
        )
        return {"success": True, "data": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculate/component-proportions")
async def calculate_component_proportions_endpoint(request: ComponentProportionsRequest):
    try:
        result = paintcalx.calculate_component_proportions(
            total_volume=request.total_volume,
            proportions=request.proportions
        )
        return {"success": True, "data": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert-units")
async def convert_units_endpoint(request: UnitConversionRequest):
    try:
        result = paintcalx.convert_units(
            value=request.value,
            from_unit=request.from_unit,
            to_unit=request.to_unit
        )
        return {"success": True, "data": {"converted_value": result}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "PaintCalx API is running", "version": "1.0.0"}