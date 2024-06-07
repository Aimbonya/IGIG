class Applicant:
    def __init__(self, last_name, instrument):
        self.last_name = last_name
        self.instrument = instrument

class Exam:
    def __init__(self, specialty):
        self.specialty = specialty
        self.applicants = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def find_applicant(self, last_name):
        for applicant in self.applicants:
            if applicant.last_name == last_name:
                return applicant
        return None

    def sort_applicants(self):
        self.applicants.sort(key=lambda x: x.last_name)
