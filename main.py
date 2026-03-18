from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trade Opportunities API is running"}

@app.get("/sector/{sector}")
def get_trade_opportunities(sector: str):
    return {
        "sector": sector,
        "analysis": "Growing sector with strong potential",
        "opportunities": [
            "High demand",
            "Investment growth",
            "Emerging startups"
        ],
        "risks": [
            "Market volatility",
            "Regulatory changes"
        ]
    }
