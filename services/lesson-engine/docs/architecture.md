# Overview
Defines the architecture and my work process to complete the lesson engine.


# Goal 1: Input -> Output
The Engine needs to recieve a lesson request, create the lesson plan, and then return it to whatever called it.

## Questions
- How will the engine recieve/send responses? Is this an indpendent "thing" running all the time or packaged code called by another service?
    - If this needs to manage something iteself to manage requests, then it needs to be independent
- How will it create the lesson plan?
    - Needs a prompt to tell it to create a lesson plan
    - Maybe a skill to define the output required in a lesson plan
    - Maybe another skill to break down lesson requests into steps?
    