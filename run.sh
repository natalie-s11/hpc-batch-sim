#!/bin/bash
echo "Starting HPC batch simulation with $NUM_JOBS jobs..."

# Start the API in the background
python src/api.py &

# Run the scheduler
python src/scheduler.py

echo "All jobs completed!"
# Keep the API running after jobs finish
wait
