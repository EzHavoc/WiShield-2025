from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, network_routes, encrypt_routes, websocket_routes
from app.config.database import engine, Base
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (adjust origins for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(network_routes.router, prefix="/api/network", tags=["Network Security"])
app.include_router(encrypt_routes.router, prefix="/api/encrypt", tags=["Encryption"])

# Include WebSocket routes
app.include_router(websocket_routes.router)

# Run the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
