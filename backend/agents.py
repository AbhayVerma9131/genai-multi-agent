import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="YOUR_PROJECT_ID", location="asia-south1")

model = GenerativeModel("gemini-1.5-flash")


def planner_agent(user_input):
    prompt = f"""
    Break this task into steps:
    {user_input}
    """
    return model.generate_content(prompt).text


def executor_agent(user_input):
    prompt = f"Execute this task:\n{user_input}"
    return model.generate_content(prompt).text


def critic_agent(output):
    prompt = f"Improve this output:\n{output}"
    return model.generate_content(prompt).text


def orchestrator(user_input):
    plan = planner_agent(user_input)
    result = executor_agent(user_input)
    final = critic_agent(result)

    return {
        "plan": plan,
        "result": final
    }
