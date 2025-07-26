from src.models.person_model import Person


person_mock = Person(
    id=1,
    first_name="Fredy",
    last_name="Luque",
    email="fredy_luque@hotmail.com",
)


class TestPerson:
    def test_create_person(self):
        person = Person(
            id=1,
            first_name="Fredy",
            last_name="Luque",
            email="fredy_luque@hotmail.com",
        )

        assert person is None
