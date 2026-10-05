import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent  # Updated import

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY nahi mili! Apni .env file check karein.")

# 2. Initialize Model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0.3,
)

# 3. Define Tool
@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the exact result."""
    return a * b

tools = [multiply]

# 4. Create Agent using standard create_agent
system_prompt = "You are a careful assistant. Use the multiply tool for any multiplication."
agent_executor = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

# 5. Question and Execution
question = "What is 4871 multiplied by 3926? Answer with the exact number only."
print(f"Asking Agent: {question}\n")

inputs = {"messages": [("user", question)]}
result = agent_executor.invoke(inputs)

# 6. Print Output
print("AI Response:", result["messages"][-1].content)

# 7. Print ASCII Graph (agent_executor par call karna hai)
print("\n--- Agent Architecture Graph ---")
print(agent_executor.get_graph().draw_ascii())