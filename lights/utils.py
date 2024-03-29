import json


def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data


def read_json(path):
    return json.loads(read_file(path))


def write_json(path, data):
    return write_file(path, json.dumps(data))


def write_file(path, data):
    file = open(path, "w")
    file.write(str(data))
    file.close()
    return data
