from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class Message(Model):
    message: str
 
AGENT_MAILBOX_KEY = "3653321a-8aba-48f4-a79d-f1e6a71e81b5"
SEED_PHRASE = "snowy"
 
# Now your agent is ready to join the agentverse!
agent = Agent(
    name="user",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)
fund_agent_if_low(agent.wallet.address())
 
@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
 
 
if __name__ == "__main__":
    agent.run()