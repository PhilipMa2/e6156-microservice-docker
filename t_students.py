#
# Test files inside of resource directories is kind of sloppy.
# There are better approaches.
# You can look up best practices for project structure on the web.
# I cannot explicitly cover and explain every concept in class.
#
import json
from resources.students import StudentsResource as StudentsResource


def t1():

    s = StudentsResource()
    result = s.get_students()
    print("t1: students = \n", json.dumps(result, indent=2))


if __name__ == "__main__":
    t1()

