import json

def get_repair_info(defect_name):
    with open("repair_guide.json", "r") as file:
        repair_data = json.load(file)

    return repair_data.get(defect_name, None)