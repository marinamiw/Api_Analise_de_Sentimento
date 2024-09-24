from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fast_api.schemas import SentimentResponse, SentimentRequest
from fast_api.models import Model, get_model


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/predict',response_model=SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    #vai retornar o resultado do parametro, no caso função get_model (a analise de sentimento que o modelo ira fazer)

    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment=sentiment,
        confidence=confidence,
        probabilities=probabilities
    )
