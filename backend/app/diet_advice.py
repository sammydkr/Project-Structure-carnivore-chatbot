import semantic_kernel as sk
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

class DietAdviceSkill:
    @sk_function(
        description="Provides advice on carnivore and ketogenic diets, including benefits and food recommendations.",
        name="diet_advice",
        input_description="The user's query about the diet."
    )
    def diet_advice(self, context: sk.SKContext) -> str:
        # This function will be called by the kernel when the user asks for diet advice.
        # We can have a predefined response or use AI to generate it.
        # For now, we return a predefined response, but we can also use the AI to generate a response.
        
        prompt = context["input"]
        
        # We can use the kernel to generate a response, but for simplicity, we return a string.
        # In a more advanced version, we would call the AI service here.
        return "I am a carnivore diet assistant. I recommend eating red meat, eggs, bacon, chicken, and low-oxalate vegetables. Avoid junk food, sugars, and seed oils."
