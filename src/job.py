import os
import random
import csv

def run_job(job_id, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    numbers = [random.randint(1, 100) for _ in range(10)]
    total = sum(numbers)
    mean = total / len(numbers)
    
    filename = os.path.join(output_dir, f"job_{job_id}.csv")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["numbers", "sum", "mean"])
        writer.writerow([numbers, total, mean])
    
    print(f"Job {job_id} completed: {filename}")

if __name__ == "__main__":
    run_job(1)
