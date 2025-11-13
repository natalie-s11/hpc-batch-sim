import requests, os, time
os.system("docker run --rm -d -p 8080:8080 hpc-batch-sim:latest")
r = requests.get("http://127.0.0.1:8080/health")
assert r.status_code == 200 and r.json()["status"] == "ok"
print("✅ Smoke test passed: API running and health OK.")
