import plivo

auth_id = "XXXXX"
auth_token = "XXXX"

client = plivo.RestClient(auth_id, auth_token)

response = client.calls.create(
    from_="+XXXXXX",     # Plivo number
    to_="+XXXXXX",      # Destination number
    answer_url="https://appallingly-populationless-eun.ngrok-free.dev/ivr",
    answer_method="GET"
)

print(response)
