from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Union
import paintcalx

app = FastAPI(title="PaintCalx API", description="Professional paint calculation API")

class Components(BaseModel):
    base: float
    hardener: float
    pigment: float

class PaintCalculationRequest(BaseModel):
    surface_total: float
    surface_deductions: float
    wall_type: str  # "lisse" | "granuleux" | "tres_irregulier"
    custom_coefficient: Optional[float] = None
    coats: int
    coverage: float
    unit: str = "L"  # "L" | "mL" | "kg" | "g"
    components: Components

class PaintCalculationResponse(BaseModel):
    success: bool
    surface_effective: float
    volume_total: float
    unit: str
    components: Dict[str, float]
    error: Optional[str] = None

@app.post("/calculate", response_model=PaintCalculationResponse)
async def calculate_paint_endpoint(request: PaintCalculationRequest):
    try:
        # Validation des entrées
        if request.unit not in ["L", "mL", "kg", "g"]:
            raise ValueError("Unit must be L, mL, kg, or g")
        
        if request.wall_type not in ["lisse", "granuleux", "tres_irregulier"]:
            raise ValueError("Wall type must be lisse, granuleux, or tres_irregulier")
        
        # Préparation des coefficients personnalisés
        custom_coeffs = None
        if request.custom_coefficient:
            custom_coeffs = {request.wall_type: request.custom_coefficient}
        
        # Calcul du volume
        volume_result = paintcalx.calculate_paint_volume(
            total_surface=request.surface_total,
            door_window_surface=request.surface_deductions,
            wall_type=request.wall_type,
            coat_count=request.coats,
            coverage=request.coverage,
            custom_coefficients=custom_coeffs
        )
        
        # Calcul des composants
        components_dict = request.components.dict()
        component_result = paintcalx.calculate_component_proportions(
            total_volume=volume_result['total_volume'],
            proportions=components_dict
        )
        
        # Conversion unités si nécessaire
        final_volume = volume_result['total_volume']
        final_components = component_result
        
        if request.unit != "L":
            # Conversion du volume principal
            final_volume = paintcalx.convert_units(final_volume, "L", request.unit)
            # Conversion des composants
            for comp in final_components:
                final_components[comp] = paintcalx.convert_units(
                    final_components[comp], "L", request.unit
                )
        
        return PaintCalculationResponse(
            success=True,
            surface_effective=volume_result['effective_surface'],
            volume_total=final_volume,
            unit=request.unit,
            components=final_components
        )
        
    except ValueError as e:
        return PaintCalculationResponse(
            success=False,
            surface_effective=0,
            volume_total=0,
            unit=request.unit,
            components={},
            error=str(e)
        )

@app.get("/")
async def root():
    return {"message": "PaintCalx API v2.0 - Unified contract", "version": "2.0.0"}