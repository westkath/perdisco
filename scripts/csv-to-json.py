import json


# CSV to JSON Conversion Script
def read_lines(filename):
    data = []

    with open(filename, 'r') as file:
        data = [line.strip() for line in file.readlines()]

    return data[1:]


def create_json_data(data):
    json_data = []

    for line in data:
        raw = line.split('","')
        item = {}

        item["id"] = raw[0][1:]
        item["author"] = raw[1]
        item["read"] = bool(raw[2])
        item["readDate"] = raw[3]
        item["review"] = raw[4]
        item["title"] = raw[5][:-1]

        json_data.append(item)

    return json_data


def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write("[\n")

        for entry in data[:-1]:
            file.write(json.dumps(entry) + ",\n")

        file.write(json.dumps(data[-1]))

        file.write("]")


def convert_to_json(filename):
    data = read_lines(filename)
    json = create_json_data(data)
    save_to_file("books.json", json)


# Entry Point
if __name__ == "__main__":
    convert_to_json("books.csv")
