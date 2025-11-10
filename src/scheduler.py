from multiprocessing import Pool
from job import run_job

NUM_JOBS = 5

def launch_job(job_id):
    run_job(job_id)

if __name__ == "__main__":
    with Pool(processes=NUM_JOBS) as pool:
        pool.map(launch_job, range(1, NUM_JOBS + 1))
    print("All jobs completed!")
