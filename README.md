# Project-Structure-carnivore-chatbot
We are going to create a multi-language project that uses Azure AI, Semantic Kernel, OpenAI, and possibly more. The project will be a chatbot that gives advice on the carnivore and ketogenic diets, including generating images and providing nutrient advice.

We'll write the code for the main components.

Backend (Python - FastAPI)

First, let's set up the environment variables in .env:

OPENAI_API_KEY=your_openai_api_key
OPENAI_ORG_ID=your_org_id (optional)
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint (if using Azure)
AZURE_OPENAI_API_KEY=your_azure_openai_api_key (if using Azure)

We'll use Semantic Kernel, so we need to set up the kernel.
