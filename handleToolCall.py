import json
from tools.audioGeneratorTool import *
from tools.imageGeneratorTool import *
from tools.priceTool import *

def handle_tool_calls(message):
    responses = []
    cities = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_ticket_price":
            arguments = json.loads(tool_call.function.arguments)
            city = arguments.get('destination_city')
            cities.append(city)
            price_details = get_ticket_price(city)
            responses.append({
                "role": "tool",
                "content": price_details,
                "tool_call_id": tool_call.id
            })
    return responses, cities

getpriceTool = [{"type": "function", "function": get_price_function}]
