'''The problem
Your task is to take entries of personal information in several potential formats and normalise each entry into a standard JSON format.
Input
Your program will be fed an input file of ​n​ lines. Each line contains “entry” information, which consists of a first name, a last name, a US phone number, a color, and a 5-digit ZIP code.
The order and format of these lines vary in three separate ways. The three different acceptable input formats are as follows:
aLastName,aFirstName,aPhoneNumber,aColor,aZipCode aFirstName,aLastName,aColor,aZipCode,aPhoneNumber aFirstName,aLastName,aZipCode,aPhoneNumber,aColor
For example:
Smith, John, (703)-742-0996, Blue, 10013
Randy, Johnson,Red, 11237, 703 955 0373
John, “Blutarsky, the 2nd”, 10013, 646 111 0101, Green
Some input lines may not conform to any of the formats listed above, they should be considered invalid, and should not interfere with the processing of subsequent valid lines. A line should be considered invalid if its phone number does not contain 10 digits (it may contain alphanumeric characters) and a ZIP code must contain, and only contain, 5 digits.
 Output
● The program should write a valid, formatted ​JSON​ object out to ​result.json​.
● Successfully processed lines should result in a normalized addition to the list associated
with the “​entries​” key.
● The “​entries​” list should be sorted in ascending alphabetical order by ​lastname, firstname​.
● For lines that were unable to be processed, a line number ​i ​(where ​1 ≤ i < n​) for each faulty
line should be appended to the list associated with the “​errors​” key. Sample
For the input, please use the following records:
Booker T., Washington, 87360, 373 781 7380, light blue Chandler, Kerri, (623)-668-9293, pink, 123123121
James Murphy, yellow, 83880, 018 154 6474
Asdfawefawea
We should receive the output:
{
"entries": [
{
"color": "yellow",
"firstname": "James", "lastname": "Murphy", "phonenumber": "018-154-6474", "zipcode": "83880"
}, {
} ],
"errors": [ 1,
3 ]
}
'''


import json
def is_phone_number(phone_number):
    count = 0
    for number in phone_number:
        if number.isnumeric():
            count += 1
    return count == 10

def is_zipcode(zcode):
    if not zcode.isnumeric():
        return False
    if len(zcode) != 5:
        return False
    return True


json_data = {
    "entries":[],
    "error":[]
}

with open("name.txt", "r") as namef:
    for i, line in enumerate(namef.readlines()):
        lines = line.split(",")
        if len(lines) != 5:
            json_data['error'].append(i)

        elif is_phone_number(lines[2].strip()) and is_zipcode(lines[4].strip()):
            json_data['entries'].append({
                    'color':lines[3],
                    'firstName':lines[1],
                    'lastName':lines[0],
                    'phoneNumber':lines[2],
                    'zipcode':lines[4]
            })
        elif is_zipcode(lines[2].strip()) and is_phone_number(lines[3].strip()): 
            json_data['entries'].append({
                    'color':lines[4].strip(),
                    'firstName':lines[0].strip(),
                    'lastName':lines[1].strip(),
                    'phoneNumber':lines[3].strip(),
                    'zipcode':lines[2].strip()

            })
        elif is_phone_number(lines[4].strip()) and is_zipcode(lines[3].strip()):
            json_data['entries'].append({
                    'color':lines[2].strip(),
                    'firstName':lines[0].strip(),
                    'lastName':lines[1].strip(),
                    'phoneNumber':lines[4].strip(),
                    'zipcode':lines[3].strip()
            })
        else:
            print(i)
            json_data["error"].append(i)

result_file = open("result.json", "w")
json.dump(json_data, result_file, indent=4, sort_keys=True)
result_file.close()