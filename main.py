from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
        if not self.validate_number():
            raise ValueError("Неправельний номер телефону.")
    
    def validate_number(self):
        return len(self.value) == 10 and self.value.isdigit()


class Record:
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones: list(Phone) = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)};"

    def add_phone(self, phone: Phone):
        # Добавляємо телефон в базу
        for p in self.phones:
            if p.value == phone:
                return "Телефон уже існує."
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))
        
    def edit_phone(self, phone: str, new_phone: str):
        # Провірка чи такий телефон вообще існує.
        if not any(p.value == phone for p in self.phones):
            raise ValueError("Номер який Ви хочете змінити - не існує.")
        
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
        
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


book = AddressBook()


lara = Record('Lara')
lara.add_phone('8888888888')
lara.add_phone('0000000000')
lara.add_phone('3806822212')

book.add_record(lara)

erik = Record('Erik')
erik.add_phone('3809799999')
erik.add_phone('4878471001')

book.add_record(erik)

for name, record in book.data.items():
    print(record)

book.find('Lara') # Contact name: Lara, phones: 8888888888; 0000000000; 3806822212;

book.delete('Lara')

# Видаляємо номер
erik.remove_phone('3809799999')
# Змінюємо номер
lara.edit_phone('8888888888', '1111111188')
# Шукаємо номер
lara.find_phone('3806822212') # 3806822212
