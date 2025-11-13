import random

def run_job(job_id):
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Job {job_id} result: sum={sum(numbers)}, mean={sum(numbers)/len(numbers)}")

if __name__ == "__main__":
    run_job(1)

