from models.person_model import Person

import os


def create_person():
    person = Person(
        id=1,
        first_name="Fredy",
        last_name="Luque",
        email="fredy_luque@hotmail.com",
    )

    return person


def main():
    print(create_person)


if __name__ == "__main__":
    main()
