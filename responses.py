from transformers import pipeline
import config

# Initialize the text generation pipeline with the model specified in config
chatbot_pipeline = pipeline(
    "text-generation",
    model=config.MODEL_NAME,
    torch_dtype="auto"
)

def get_response(user_message):
    # Generate a response with sample-based generation enabled
    response = chatbot_pipeline(
        user_message,
        max_length=100,         # Set higher if more detailed answers are needed
        num_return_sequences=1,
        temperature=0.7,        # Adjusts creativity
        top_k=50,               # Considers the top 50 choices for each token
        top_p=0.9,              # Uses cumulative probability for token selection
        do_sample=True,         # Enables sampling
        truncation=True         # Explicit truncation to avoid overlength responses
    )
    # Extract and return the generated text from the response
    return response[0]["generated_text"]
