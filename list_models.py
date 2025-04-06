# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load API Key
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Check if API key is loaded
# if not API_KEY:
#     print("❌ GEMINI_API_KEY not found! Check your .env file.")
# else:
#     print("✅ GEMINI_API_KEY loaded successfully.")

# # Initialize API
# try:
#     genai.configure(api_key=API_KEY)
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content("Say hello")
#     print("✅ Model is working! Response:", response.text)
# except Exception as e:
#     print(f"❌ Error: {e}")

import google.generativeai as genai

genai.configure(api_key="AIzaSyDZ6uPYolsHjurPXZqJgx6z7ZR5mS4zItQ")

for model in genai.list_models():
    print(model.name)
