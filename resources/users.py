from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_number: str
    month: str
    year: str
    day:str
    gender: str
    subjects: str
    hobbies: str
    images: str
    current_address: str
    state: str
    city: str


new_user = User(
    first_name ='Ann',
    last_name = 'Ivanova',
    user_email = 'test@test.com',
    user_number = '1111111111',
    month = 'June',
    year = '2000',
    day = '3',
    gender =  'Female',
    hobbies = 'Reading',
    images = 'butterflies.png',
    current_address = 'Russia',
    subjects ='Computer Science',
    state = 'Uttar Pradesh',
    city = 'Merrut',
)