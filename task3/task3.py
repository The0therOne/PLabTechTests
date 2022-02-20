import sys
import json

test_json_file = sys.argv[1]
values_json_file = sys.argv[2]

with open(test_json_file, 'r') as test_json:
    tests_file = json.loads(test_json.read())

with open(values_json_file, 'r') as values_json:
    values_file = json.loads(values_json.read())


def set_value(id):
    for value in values_file['values']:
        if value['id'] == id:
            return value['value']

def parse_inner_values(lst):
    if 'value' in lst:
        lst['value'] = set_value(lst['id'])
    if 'values' in lst:
        for i in range(len(lst['values'])):
            parse_inner_values(lst['values'][i])


for test in tests_file['tests']:
    parse_inner_values(test)

with open('report.json', 'w') as report_json:
    json.dump(tests_file, report_json)