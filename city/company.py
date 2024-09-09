class Job:
    def __init__(self, title, pay, company):
        self.title = title
        self.pay = pay
        self.company = company  # Reference to the company offering the job

class Company:
    def __init__(self, name):
        self.name = name
        self.jobs = []

    def add_job(self, title, pay):
        job = Job(title, pay, self)  # Pass 'self' to associate the job with the company
        self.jobs.append(job)

    def get_jobs(self):
        return self.jobs

    def find_job_by_title(self, title):
        for job in self.jobs:
            if job.title == title:
                return job
        return None
