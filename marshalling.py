from models import StudentProfile

def marshal_student(student: StudentProfile) -> dict:
    return {
        "name": student.name,
        "id": student.id,
        "grades": student.grades
    }

def unmarshal_student(data: dict) -> StudentProfile:
    # Type validation
    if not isinstance(data["id"], int):
        raise TypeError("Student ID must be integer")

    if not all(isinstance(g, int) for g in data["grades"]):
        raise TypeError("Grades must be integers")

    return StudentProfile(
        data["name"],
        data["id"],
        data["grades"]
    )