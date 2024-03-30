from collections import UserDict

# Базовий клас для поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені
class Name(Field):
    pass

# Клас для зберігання телефонного номера
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Невірний формат номера телефону")

# Клас для запису контакту
class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ім'я контакту
        self.phones = []        # Телефонні номери контакту

    # Додавання телефонного номера до запису
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Видалення телефонного номера з запису
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    # Редагування телефонного номера
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    # Пошук телефонного номера в записі
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    # Перетворення запису в рядок
    def __str__(self):
        return f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(str(p) for p in self.phones)}"

# Клас для адресної книги
class AddressBook(UserDict):
    # Додавання запису до адресної книги
    def add_record(self, record):
        self.data[record.name.value] = record

    # Пошук запису за ім'ям
    def find(self, name):
        return self.data.get(name)

    # Видалення запису за ім'ям
    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Створення адресної книги
book = AddressBook()

# Створення запису для John та додавання телефонних номерів
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

# Створення запису для Jane та додавання телефонного номера
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів в книзі
for name, record in book.data.items():
    print(record)

# Пошук запису John, редагування телефонного номера та виведення
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Пошук телефонного номера в записі John та виведення
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")
