import os
from sagemaker.predictor import retrieve_default
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import replicate

dotenv_path = '.env'
load_dotenv(dotenv_path=dotenv_path)
endpoint_name = os.getenv('ENDPOINT_NAME')
flux_model_name = os.getenv('FLUX_MODEL_NAME')

class Prompt(BaseModel):
    text: str

app = FastAPI()

@app.get("/mar")
async def get_msg(prompt: Prompt):
    predictor = retrieve_default(endpoint_name)
    payload = {
        "inputs": prompt.text + '.',
        "parameters": {
            "max_new_tokens": 256,
            "top_p": 0.9,
            "temperature": 0.2
        }
    }
    response = predictor.predict(payload)
    refined_response = response[0]['generated_text']

    keyword = "Response:"
    pos = refined_response.find(keyword)
    result = "error"

    if pos != -1:
        result = refined_response[pos + len(keyword):].strip()
    
    return { 'response': result }

@app.get("/img")
async def get_img(prompt: Prompt):
    print("get_img")
    try:
        output = replicate.run(
            flux_model_name,
            input={
                "model": "dev",
                "width": 848,
                "height": 848,
                "prompt": prompt.text,
                "lora_scale": 1,
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "webp",
                "guidance_scale": 3.5,
                "output_quality": 80,
                "num_inference_steps": 28
            }
        )
        print(output[0])
        return { 'img': output[0] }
    except replicate.exceptions.ModelError as e:
        return { 'error': 'maybe another time :>' }