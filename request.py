import requests

# Define the API endpoint
url = "http://127.0.0.1:8000/answer"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}
# data = {
    # 'context': 'The year is 2042. The world is a very different place than it was just a few decades ago. Climate change has caused widespread devastation, and many major cities have been abandoned. The global economy has collapsed, and there is widespread poverty and hunger. In this bleak new world, a new kind of hero has emerged: the climate refugee.',
    # 'question': 'What challenges do climate refugees face?'
# }

context = input("\nEnter the Context: ")
question = input("\nEnter the Question: ")

data = { 'context': context, 'question': question}

response = requests.post(url, headers=headers, data=data)
result = response.json()
answer = result["answer"]
print("\nAnswer:", answer)
#print(result)