from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.kernel import create_kernel
import semantic_kernel as sk
from semantic_kernel.planning import SequentialPlanner
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Global kernel instance
kernel = None

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default"

class ImageRequest(BaseModel):
    prompt: str

@app.on_event("startup")
async def startup_event():
    global kernel
    kernel = await create_kernel()

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Create a context for the user
        context = kernel.create_new_context()
        context["input"] = request.message
        context["user_id"] = request.user_id
        
        # Import the diet advice skill
        diet_skill = kernel.import_skill(DietAdviceSkill(), skill_name="DietAdvice")
        
        # Use the skill
        result = await kernel.run_async(
            diet_skill["diet_advice"],
            input_str=request.message,
            context=context
        )
        
        return {"response": result.result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_image")
async def generate_image(request: ImageRequest):
    try:
        # Use OpenAI's DALL-E to generate an image
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Image.create(
            prompt=request.prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
