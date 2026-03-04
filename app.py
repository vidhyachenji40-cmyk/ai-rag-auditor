from google import genai
from langchain_community.document_loaders import TextLoader

# 1. Initialize the Client
client = genai.Client(api_key="AIzaSyCBhb72Qyu2hd470NJ2UT3aSSgk0eGx8WI")

# 2. Load your file
try:
    loader = TextLoader("sample_policy.txt")
    docs = loader.load()
    context = docs[0].page_content
except Exception as e:
    print(f"Error loading file: {e}")
    context = "Sample policy text: Company X aims for 95% accuracy in data processing."

# 3. Get the Answer using the 2026 Stable ID
query = "What companies are mentioned and what is the target accuracy?"
prompt = f"Context: {context}\n\nQuestion: {query}"

print("Generating Answer...")
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=prompt
)
generated_answer = response.text

# 4. Run the Audit
print("Running Audit...")
audit_prompt = f"Context: {context}\nQuestion: {query}\nResponse: {generated_answer}\nRate Faithfulness (0-1) and Relevancy (0-1) with reasons."

audit_result = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=audit_prompt
)

print("\n--- ANSWER ---")
print(generated_answer)

print("\n--- AUDIT RESULTS ---")
print(audit_result.text)