import requests

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("1. Testing GET /")
    res_root = requests.get(f"{BASE_URL}/")
    print(res_root.json())
    print("-" * 30)

    print("2. Testing GET /health")
    res_health = requests.get(f"{BASE_URL}/health")
    print(res_health.json())
    print("-" * 30)

    print("3. Testing POST /predict (English & Vietnamese)")
    headers = {"Content-Type": "application/json"}
    
    payload_en = {"text": "So bad"}
    res_predict_en = requests.post(f"{BASE_URL}/predict", json=payload_en, headers=headers)
    print("English Result:", res_predict_en.json())
    
    payload_vi = {"text": "Món ăn rất giòn"}
    res_predict_vi = requests.post(f"{BASE_URL}/predict", json=payload_vi, headers=headers)
    print("Vietnamese Result:", res_predict_vi.json())
    print("-" * 30)
    
    print("4. Test empty string")
    payload_err = {"text": "   "}
    res_err = requests.post(f"{BASE_URL}/predict", json=payload_err, headers=headers)
    print("Error Result:", res_err.json())

if __name__ == "__main__":
    test_api()