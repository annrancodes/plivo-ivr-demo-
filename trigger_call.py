import plivo

auth_id = "MANZJJOGRLNZK0ZMZIMM"
auth_token = "NmU2ZmRhMjYtOTE1OS00YWRiLWJlNmEtNTIxYzUy"

client = plivo.RestClient(auth_id, auth_token)

response = client.calls.create(
    from_="+14692463987",     # Plivo number
    to_="+918031274121",      # Destination number
    answer_url="https://appallingly-populationless-eun.ngrok-free.dev/ivr",
    answer_method="GET"
)

print(response)
