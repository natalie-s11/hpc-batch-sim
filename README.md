Executive Summary

Problem: Need to simulate batch job orchestration for HPC concepts.

Solution: Local Python scheduler runs multiple “jobs,” logs outputs, demonstrates parallel execution.

System Overview

Course Concept: HPC batch job orchestration

Architecture Diagram: (Assets: scheduler → job pool → job scripts → outputs)

Data/Models/Services: random numbers, CSV outputs

How to Run

Docker commands above

Optional .env for NUM_JOBS

Design Decisions

Why Python + subprocess + multiprocessing

Tradeoffs: simplicity vs. real HPC complexity

Results & Evaluation

Screenshot of outputs/logs in /assets/screenshots

Validation: ensure all CSVs are created

What’s Next

Simulate job dependencies, variable runtimes, logging metrics

Optional: scale to simulated cluster nodes

Links

GitHub repo: https://github.com/natalie-s11/hpc-batch-sim/tree/main
