import os
from agents import Agent, Runner
import asyncio   

# Agentes especializados directamente

oneminuteagent = Agent(
    name="One-Minute Challenge",
    instructions="You are a specialist in generating simple, fun, everyday topics in Spanish for a One-Minute Challenge game. Respond with a short topic only. Include the English translation in the response.",
    model="gpt-4o",
)

wordhotpotagent = Agent(
    name="Word Hot Potato",
    instructions="You are a specialist in generating fun, easy-medium-difficulty Spanish vocabulary words for a vocabulary game. Respond with just one Spanish word. Include the English translation in the response.",
    model="gpt-4o",
)

scenariogeneratoragent = Agent(
    name="Scenario Generator",
    instructions="You are a specialist in creating short, fun, role-play scenarios in Spanish and assigning a role to the student. Format as 'Scenario: ...; Role: ...'. Include the English translation in the response.",
    model="gpt-4o",
)

# Runner para ejecutar agentes

async def run_agent(agent: Agent, user_input: str) -> str:
    try:
        # Ejecuta el agente usando Runner.run estático
        result = await Runner.run(agent, user_input)
        # Usa final_output si está presente, si no recurre a output
        return getattr(result, 'final_output', None) or getattr(result, 'output', '')
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

    # Mostrar solo el resultado del agente
    print(output)

# Ejecutar
if __name__ == "__main__":
    asyncio.run(main())
