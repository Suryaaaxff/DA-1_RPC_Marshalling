Lab DA-1: RPC Marshalling with Objects

## Objective

The aim of this lab is to build a Remote Procedure Call (RPC) system using Python that allows a method to be invoked remotely by passing a custom object called **StudentProfile**, while also performing type validation on the server side.

## Implemented Features

* Designed a **StudentProfile** class that stores student name, student ID, and grades.
* Implemented an RPC architecture with communication between client and server.
* Used **marshalling and unmarshalling** to convert objects into transferable format and reconstruct them on the server.
* Implemented a **validate_types()** function on the server to verify the data types of received values.
* Added **type safety** by raising `TypeError` when incorrect data types are sent.

## Validation Testing

* When correct data is provided, the system successfully calculates and returns the average grade.
* If the student ID is provided as a string instead of an integer, a `TypeError` is raised.
* If the grades contain values that are not integers, the system raises a `TypeError`.

## Result

The RPC system was successfully implemented with object marshalling and unmarshalling along with server-side type checking. The system ensures that invalid data from the client is rejected, improving the reliability and correctness of the RPC communication.

