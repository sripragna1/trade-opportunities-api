from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(
    title="Trade Opportunities API",
    description="Provides market insights for Indian sectors",
    version="1.0.0"
)

# Request Model
class SectorRequest(BaseModel):
    sector: str

# Sample sector data (can be replaced with real APIs later)
sector_data = {
    "technology": ["AI", "Cloud Computing", "Cybersecurity", "SaaS"],
    "pharmaceuticals": ["Generic Drugs", "Vaccines", "Biotech"],
    "agriculture": ["Organic Farming", "Agri-Tech", "Export Crops"]
}

# Helper function
def generate_analysis(sector: str):
    trends = sector_data.get(sector.lower(), ["Market Expansion", "Innovation"])

    return {
        "sector": sector.capitalize(),
        "timestamp": datetime.utcnow(),
        "market_trend": random.choice(["Bullish", "Neutral", "Bearish"]),
        "top_opportunities": random.sample(trends, min(len(trends), 3)),
        "risk_level": random.choice(["Low", "Medium", "High"]),
        "investment_suggestion": random.choice([
            "Long-term investment recommended",
            "Short-term trading opportunity",
            "Wait and watch strategy"
        ])
    }

# API Endpoint
@app.post("/analyze")
def analyze_sector(request: SectorRequest):
    result = generate_analysis(request.sector)
    return {
        "status": "success",
        "data": result
    }

# Root endpoint
@app.get("/")
def home():
    return {"message": "Trade Opportunities API is running 🚀"}
