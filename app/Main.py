from fastapi import FastAPI
from app.route.payment import router as payment_router

app = FastAPI(title = "RESILIENT-PAYMENT-BACKEND") #understand this line -> # This line initializes a FastAPI application instance with the title "RESILIENT-PAYMENT-BACKEND".

app.include_router(payment_router )
@app.get("/health")
def health_check():
    return {"status" : "Good"}

#Understaning : what is endpoint ? -> An endpoint in web development refers to a specific URL or URI (Uniform Resource Identifier) where a web service or API can be accessed by clients. It represents a specific function or resource that the server exposes to handle requests from clients. Each endpoint corresponds to a particular operation, such as retrieving data, submitting data, updating information, or deleting resources. Endpoints are typically defined by the combination of the HTTP method (GET, POST, PUT, DELETE, etc.) and the URL path.