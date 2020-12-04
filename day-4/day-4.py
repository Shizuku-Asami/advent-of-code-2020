import re
import itertools
from pprint import pprint

def get_data(file):
    f = open(file, "r")
    data = f.readlines()
    data1 = [re.sub('\n', '', line) for line in data]
    return data1

def parser(data):
    list_of_dict = []
    for row in data:
        if row == '':
            list_of_dict.append('')
        else:
            a = row.split()
            if True:
                for i in a:
                    b  = {i.split(':')[0]: i.split(':')[1]}
                    list_of_dict.append(b)
            else:
                break
    return list_of_dict

def combine_dict(data):
    l = []
    ll = []
    d = dict()
    data1 = data + ['']
    for el in data1:
        if isinstance(el, dict):
            l.append(el)
            #print(f'l = {l}, len(l) = {len(l)}')
        else:
            for i in l:
                for key, value in i.items():
                    d[key] = value
            ll.append(d)
            #print(f'll = {ll}, len(ll) = {len(ll)}')
            l = []
            d = dict()
    # print(f'll = {ll}, len(ll) = {len(ll)}')
    #for i in ll:
    #    print(len(i))
    return ll

def validate_data(data):
    valid = []
    not_valid = []
    for d in data:
        if set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']) or set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valid.append(True)
        else:
            not_valid.append(False)
    return {'valid': len(valid), 'not_valid': len(not_valid)}

def is_valid_year(year):
    if 1920 <= int(year) <= 2002:
        return True
    else:
        return False

def is_valid_issue_year(year):
    if 2010 <= int(year) <= 2020:
        return True
    else:
        return False

def is_valid_expiration_year(year):
    if 2020 <= int(year) <= 2030:
        return True
    else:
        return False

def is_valid_height(height):
    if re.search('cm$', height):
        number = float(re.findall('\d+', height)[0])
        if 150 <= number <= 193:
            return True
        else:
            return False
    elif re.search('in$', height):
        number = float(re.findall('\d+', height)[0])
        if 59 <= number <= 79:
            return True
        else:
            return False
    else:
        return False

def is_valid_hair_color(color):
    if re.search(r'^#([a-f]|[0-9]){6}', color):
        return True
    else:
        return False

def is_valid_eye_color(color):
    if color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False

def is_valid_pid(pid):
    if re.match('^[0-9]{9}$', pid):
        return True
    else:
        return False
        
def validate_passport(data):
    valid = []
    not_valid = []
    for d in data:
        if set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']) or set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            result = is_valid_year(d['byr']) & is_valid_issue_year(d['iyr']) & is_valid_expiration_year(d['eyr']) & is_valid_height(d['hgt']) & is_valid_hair_color(d['hcl']) & is_valid_eye_color(d['ecl']) & is_valid_pid(d['pid'])
            if result:
                valid.append(True)
            else:
                not_valid.append(False)
        else:
            not_valid.append(False)
    return {'valid': len(valid), 'not_valid': len(not_valid)}


def main():
    data = get_data('input.txt')
    parsed_data = parser(data)
    data_to_validate = combine_dict(parsed_data)
    print(validate_passport(data_to_validate))
    # print(len(parsed_data))
    print(validate_data(data_to_validate))
    # print(is_valid_height('20in'))
    # print(is_valid_hair_color('#000000'))
    # print(is_valid_eye_color('gry'))
    # print(is_valid_pid('012435689'))
    for i, d in enumerate(data_to_validate):
        if set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']) or set(d.keys()) == set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            result = is_valid_year(d['byr']) & is_valid_issue_year(d['iyr']) & is_valid_expiration_year(d['eyr']) & is_valid_height(d['hgt']) & is_valid_hair_color(d['hcl']) & is_valid_eye_color(d['ecl']) & is_valid_pid(d['pid'])
            # print(i,d , is_valid_year(d['byr']), is_valid_issue_year(d['iyr']), is_valid_expiration_year(d['eyr']), is_valid_height(d['hgt']), is_valid_hair_color(d['hcl']), is_valid_eye_color(d['ecl']), is_valid_pid(d['pid']), f'(result = {result})')
            print(i, d['pid'], is_valid_pid(d['pid']))
    # print(is_valid_issue_year('1971'))
    
if __name__ == "__main__":
    main()