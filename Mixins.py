import json

class SerializationMixin:

    # Serialize object to a dictionary or JSON format
    def to_dict(self):
        return self.__dict__   # __dict__ returns a dictionary representation of the object's attributes

    def to_json(self):
        return json.dumps(self.to_dict())
        

class SearchMixin:
    # Search objects based on attribute

    def match_attribute(self, attribute, value):
        return getattr(self, attribute, None) == value

class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = []  # Initialize a log list to store actions

    # Log actions performed on objects
    def log_action(self, action):
        self.log.append(action)
        print(f"Action logged: {action}")

class ValidationMixin:

    # Validate student grade
    def validate_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        return True
    

class gradeMixin:
    def grade_allocator(self, grade):
        match grade:
            case _ if 70 <= grade <= 100:
                return "A"
            case _ if 60 <= grade < 69:
                return "B"
            case _ if 50 <= grade < 59:
                return "C"
            case _ if 40 <= grade < 49:
                return "D"
            case _:
                return "F"