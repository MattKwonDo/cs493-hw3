In this assignment, you will be provided the design of a REST API and a test suite. The focus of this assignment is thus on implementing a REST API and deploying the service on Google App Engine. By the end of the assignment you will have a live REST API service on the cloud.

Instructions
Your REST service models a simple marina.

There are two types of resources, boats and slips (slips are "parking spots" for boats).
A boat is either at sea or it is assigned to a slip.
A slip has space for only one boat at a time. At any given time, a slip is
Either empty, when there is no boat at the slip, or
Occupied, when there is a boat in it.
There is no permanent assignment between a boat and a slip. As an example, the following sequence of events can happen
Boat A is in Slip 1.
Boat A departs and is at sea.
Boat B arrives at the marina and is now in Slip 1.
Boat A arrives at the marina and is now in Slip 4.