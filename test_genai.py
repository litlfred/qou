from google import genai
try:
    client = genai.Client()
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents='Hello, who are you?'
    )
    print("Success:", response.text)
except Exception as e:
    print("Error:", e)
