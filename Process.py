import unicodedata
import json 
import random 

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def convert_to_unsigned(full_name_with_accents):
    return remove_accents(full_name_with_accents)

    # Sử dụng hàm convert_to_unsigned
# full_name_with_accents = "Nguyễn Văn An"
# full_name_unsigned = convert_to_unsigned(full_name_with_accents)
# print(full_name_unsigned)

def process_json_element(element):
    """
    Hàm này xử lý một phần tử JSON.
    """
    name = element.get("first_name", "")
    age = element.get("last_name", 0)
    city = element.get("full_name", "")

    #print(f"Tên: {name}, Họ : {age}, Họ và tên: {city}")
    return city

def readfile():
    with open('Data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for json_element in data:
            Fullname = process_json_element(json_element)
            ran = random.randint(1,10000)
            full = (convert_to_unsigned(Fullname)).replace(" ","") + str(ran)+ "@gmail.com"
            json_element["Emai"]= full
    with open('information.json', 'w', encoding='utf-8') as file:
            # Use json.dump to write the data to the file
            json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    readfile()
