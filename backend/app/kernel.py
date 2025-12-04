import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAITextEmbedding
from semantic_kernel.connectors.memory.chroma import ChromaMemoryStore
import os

async def create_kernel():
    kernel = sk.Kernel()
    
    # Configure AI service
    use_azure = os.getenv("USE_AZURE_OPENAI", "False").lower() == "true"
    
    if use_azure:
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        kernel.add_chat_service(
            "chat_completion",
            AzureChatCompletion(deployment, endpoint, api_key)
        )
        kernel.add_text_embedding_generation_service(
            "embedding",
            AzureTextEmbedding(os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"), endpoint, api_key)
        )
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        org_id = os.getenv("OPENAI_ORG_ID")
        kernel.add_chat_service(
            "chat_completion",
            OpenAIChatCompletion("gpt-4", api_key, org_id=org_id)
        )
        kernel.add_text_embedding_generation_service(
            "embedding",
            OpenAITextEmbedding("text-embedding-ada-002", api_key, org_id=org_id)
        )
    
    # Initialize memory store (optional, for memory in conversations)
    memory_store = ChromaMemoryStore(persist_directory="./chroma_db")
    kernel.register_memory_store(memory_store)
    
    return kernel
