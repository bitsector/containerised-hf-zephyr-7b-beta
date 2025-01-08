from transformers import pipeline

def download_model():
    pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype="auto", device_map="auto")
    print("Model downloaded and cached successfully.")

if __name__ == "__main__":
    download_model()