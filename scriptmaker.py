import json
input_json = open("./query.json", "r")
input_json_object = json.loads(input_json.read())
output = input_json_object["script"].replace(" ", "").replace("\n", "")
output = output.replace("#", str(input_json_object["query"]).replace("\n", ""))
output = output.replace(
    "@", str(input_json_object["projections"]).replace("\n", ""))
open("script.txt", "w").write(output)
input_json.close()
