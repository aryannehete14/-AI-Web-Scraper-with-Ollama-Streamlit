from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        print(f"\n--- Parsing Chunk {i} of {len(dom_chunks)} ---")
        print(f"Chunk Preview (first 5000 chars):\n{chunk[:5000]}")
        print(f"Parse Description:\n{parse_description}\n")

        try:
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": parse_description
            })
            print(f"Ollama Response:\n{response}\n")
            parsed_results.append(response)
        except Exception as e:
            print(f"Error from Ollama on chunk {i}: {e}")
            parsed_results.append("")

    return "\n".join(parsed_results)
