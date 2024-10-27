from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class TextPrompt(Model):
    text: str

class TextResponse(Model):
    text: str

AGENT_MAILBOX_KEY = "3653321a-8aba-48f4-a79d-f1e6a71e81b5"

agent = Agent(
    name="user",
    endpoint="http://127.0.0.1:8000",
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai/",
    seed="snowy"
)
fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1qv3laef6ex3x5ulk6rtxpc0s3t6p5n2hnmk39ze06h4gshrptfapwhj63dg"

prompts = [
    "How is the weather in London today?",
    "Compare the inflation rates of the past years in various European countries.",
]


@agent.on_event("startup")
async def send_message(ctx: Context):
    for prompt in prompts:
        await ctx.send(AI_AGENT_ADDRESS, TextPrompt(text=prompt))
        ctx.logger.info(f"[Sent prompt to AI agent]: {prompt}")


@agent.on_message(TextResponse)
async def handle_response(ctx: Context, sender: str, msg: TextResponse):
    ctx.logger.info(f"[Received response from ...{sender[-8:]}]:")
    ctx.logger.info(msg.text)


if __name__ == "__main__":
    agent.run()