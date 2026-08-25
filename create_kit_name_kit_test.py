import sender_stand_request
import data

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    token_response = sender_stand_request.post_new_user(data.user_body)
    return token_response.json()["authToken"]

def positive_assert(kit_name):
    kit_name = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kits(kit_name,get_new_user_token())

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name["name"]

def negative_assert(kit_name):
    kit_name = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kits(kit_name,get_new_user_token())

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "Has introducido un nombre de kit no válido. " \
                                              "El nombre solo puede contener letras del alfabeto latino, espacios, números, " \
                                              "la longitud debe ser de 1 a 511 caracteres."

def test_1_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_2_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_create_kit_special_chars_in_name_get_success_response():
    positive_assert("№%@")

def test_4_create_kit_space_in_name_get_success_response():
    positive_assert( " A Aaa ")

def test_5_create_kit_numbers_in_name_get_success_response():
    positive_assert( "123")

def test_6_create_kit_0_letters_in_name_get_error_response():
    negative_assert("")

def test_7_create_kit_512_letters_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_8_create_kit_no_name_get_error_response():
    kit_name = data.kit_body.copy()
    kit_name.pop("name")
    negative_assert(kit_name)

def test_9_create_user_number_type_name_get_error_response():
    negative_assert(123)