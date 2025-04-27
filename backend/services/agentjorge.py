import os
from openai import Agent, Runner, AsyncOpenAI
import asyncio   

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# No usamos function_tool aquí

# Agentes especializados directamente

oneminuteagent = Agent(
    name="One-Minute Challenge",
    instructions="You are a specialist in generating simple, everyday topics in English for a One-Minute Challenge game. Respond with a short topic only.",
    model="gpt-4o",
)

wordhotpotagent = Agent(
    name="Word Hot Potato",
    instructions="You are a specialist in generating medium-difficulty Spanish vocabulary words for a vocabulary game. Respond with just one Spanish word.",
    model="gpt-4o",
)

scenariogeneratoragent = Agent(
    name="Scenario Generator",
    instructions="You are a specialist in creating short role-play scenarios in English and assigning a role to the student. Format as 'Scenario: ...; Role: ...'.",
    model="gpt-4o",
)

# Runner para ejecutar agentes

async def run_agent(agent: Agent, user_input: str) -> str:
    runner = Runner(agent=agent, client=client)
    try:
        result = await runner.run(user_input)
        return result.output
    except Exception as e:
        print("Error running agent:", e)
        return f"Error: {e}"

# Main de prueba

async def main():
    user_action = input("¿Qué quieres generar? (topic/word/scenario): ").strip().lower()

    if user_action == "topic":
        output = await run_agent(oneminuteagent, "Generate a topic, please.")
    elif user_action == "word":
        output = await run_agent(wordhotpotagent, "Generate a word, please.")
    elif user_action == "scenario":
        output = await run_agent(scenariogeneratoragent, "Generate a scenario, please.")
    else:
        output = "Acción no reconocida."

    print("\nResultado generado:\n", output)

    topic = await run_agent(oneminuteagent, "Generate a topic for the One-Minute Challenge")
    print("Generated topic:", topic)

# Ejecutar
if __name__ == "__main__":
    asyncio.run(main())
