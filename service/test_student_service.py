import pytest

from service.student_service import StudentService
from model.student_model import Student


@pytest.fixture
def student_service():
    return StudentService()


def test_add_student(student_service):

    student = Student(
        name="Jenkins Test Student",
        email="jenkins_test@example.com",
        phone="9999999999",
        course="Python",
        age=21,
        status="Active"
    )

    result = student_service.add_student(student)

    assert result is not None


def test_get_all_students(student_service):

    result = student_service.get_all_students()

    assert result is not None
    assert isinstance(result, list)


def test_get_student_by_id(student_service):

    students = student_service.get_all_students()

    if not students:
        pytest.skip("No students available in database")

    student_id = students[0].student_id

    result = student_service.get_student_by_id(student_id)

    assert result is not None


def test_search_student(student_service):

    result = student_service.search_student("Jenkins")

    assert result is not None
    assert isinstance(result, list)


def test_add_student_name_validation(student_service):

    student = Student(
        name="",
        email="test@example.com",
        phone="9999999999",
        course="Python",
        age=21
    )

    with pytest.raises(ValueError, match="Name is required"):
        student_service.add_student(student)


def test_add_student_email_validation(student_service):

    student = Student(
        name="Test Student",
        email="",
        phone="9999999999",
        course="Python",
        age=21
    )

    with pytest.raises(ValueError, match="Email is required"):
        student_service.add_student(student)


def test_add_student_age_validation(student_service):

    student = Student(
        name="Test Student",
        email="test@example.com",
        phone="9999999999",
        course="Python",
        age=17
    )

    with pytest.raises(ValueError, match="Age must be 18 or above"):
        student_service.add_student(student)