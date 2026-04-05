from rpc import RPCClient
from server import rpc_server
from models import StudentProfile
from marshalling import marshal_student

client = RPCClient(rpc_server)

# Valid student profile
student = StudentProfile(
    name="Suriya Kumari P",
    id=500,
    grades=[29, 45, 99]
)

response = client.call(
    "calculate_grade_average",
    marshal_student(student)
)

print("Response:", response)

# Invalid data test
invalid_student_data = {
    "name": "Suriya Kumari P",
    "id": "500",
    "grades": [34, 56]
}

error_response = client.call(
    "calculate_grade_average",
    invalid_student_data
)

print("Error Response:", error_response)