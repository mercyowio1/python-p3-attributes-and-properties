#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
        self._name = None
        self._job = None
        self.name = name  # Using the setter for name
        self.job = job  # Using the setter for job

    # Name property
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()  # Convert to title case before saving

    # Job property
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job