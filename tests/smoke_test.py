import requests

# URL of your already-running API
API_URL = "http://127.0.0.1:8080"

try:
    # Check health endpoint
    r = requests.get(f"{API_URL}/health")
    r.raise_for_status()  # raise exception if status code != 200
    health = r.json()
    assert health.get("status") == "ok"
    print("✅ Smoke test passed: API running and health OK.")

except Exception as e:
    print("❌ Smoke test failed:", e)
