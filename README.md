DA-1 RPC Marshalling with Objects

Project Title:
RPC Marshalling with Objects using Python

Description:
This project implements a Python-based Remote Procedure Call (RPC) framework that supports remote method invocation using a custom object called StudentProfile. The system demonstrates object marshalling and unmarshalling, client-server communication, and server-side type validation to ensure correct data types before processing requests.

The client sends a marshalled StudentProfile object to the server. The server unmarshals the object, validates the data types, calculates the grade average, and returns the result to the client.

Objective:
The objective of this project is to implement an RPC framework that allows a client to remotely invoke a server method using a custom object while ensuring type safety through server-side validation.

Features:

* RPC client-server architecture
* StudentProfile object marshalling
* Object unmarshalling on the server
* JSON-based request and response communication
* Server-side type validation
* Error handling using TypeError
* Remote grade average calculation

Project Structure:
DA-1_RPC_Marshalling/
client.py
server.py
rpc.py
models.py
marshalling.py
results.md
README.txt

File Description:
rpc.py:
Contains the RPCServer and RPCClient classes that handle request-response communication using JSON.

server.py:
Registers the remote procedure calculate_grade_average and processes client requests.

client.py:
Creates a StudentProfile object, marshals it, sends the request to the server, and prints the response.

models.py:
Defines the StudentProfile class with name, id, and grades.

marshalling.py:
Handles marshalling (object to dictionary) and unmarshalling (dictionary to object) with type validation.

results.md:
Contains the output and results of the RPC execution.

How the System Works:

1. The client creates a StudentProfile object.
2. The object is marshalled into a dictionary.
3. The request is converted into JSON format.
4. The RPC server receives the request.
5. The server unmarshals the object.
6. The server validates the data types.
7. The server calculates the grade average.
8. The server sends the result back to the client.
9. The client prints the response.

How to Run the Project:
Open terminal in the project folder and run:
python client.py

Sample Output:
Response: {'status': 'success', 'result': 57.66}
Error Response: {'status': 'error', 'message': 'Student ID must be integer'}

Result:
The RPC framework was successfully implemented with object marshalling and unmarshalling. The system performs server-side type validation to ensure only valid data is processed. Invalid client requests are rejected, ensuring reliable RPC communication.

Technologies Used:
Python
JSON
Remote Procedure Call (RPC)
Object Marshalling
Client-Server Architecture
