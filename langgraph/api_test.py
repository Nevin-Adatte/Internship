import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()

# Test 1: Check if API token is set
def check_api_token():
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if token:
        print(f"✅ API Token found: {token[:10]}...")  # Show first 10 chars only
        return token
    else:
        print("❌ API Token not found in environment variables")
        return None

# Test 2: Test API connection
def test_api_connection():
    try:
        print("\n🔄 Testing HuggingFace API connection...")
        
        # Initialize the model
        llm = HuggingFaceEndpoint(
        repo_id="gpt2",
        model_kwargs={
            "max_length": 50,
            "temperature": 0.7
        }
    )
        
        print("✅ Model initialized successfully")
        
        # Test with a simple prompt
        test_prompt = "Hello, this is a test"
        print(f"🔄 Testing with prompt: '{test_prompt}'")
        
        response = llm.invoke(test_prompt)
        print(f"✅ API Response: {response}")
        
        return True
        
    except Exception as e:
        print(f"❌ API Connection failed: {e}")
        return False

# Run tests
if __name__ == "__main__":
    print("=== HuggingFace API Test ===")
    
    # Check token
    token = check_api_token()
    
    if token:
        # Test connection
        success = test_api_connection()
        
        if success:
            print("\n🎉 All tests passed! Your API is working correctly.")
        else:
            print("\n❌ API test failed. Check your token and internet connection.")
    else:
        print("\n❌ Please set your HUGGINGFACEHUB_API_TOKEN environment variable first.")