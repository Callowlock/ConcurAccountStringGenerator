# errors.py


class UnequalLengthError(Exception):
    def __init__(self, message="Input lists must be the same length"):
        super().__init__(message)


class EmptyInputListError(Exception):
    def __init__(self, field_name):
        super().__init__(f"{field_name} cannot be empty.")


class UnknownDepartmentError(Exception):
    def __init__(self, invalid_value):
        super().__init__(f"Unknown department index: '{invalid_value}' (must be 0–7).")


class InvalidDeleteFlagError(Exception):
    def __init__(self, flag):
        super().__init__(f"Invalid delete flag: '{flag}'. Only 'Y' or 'N' allowed.")
