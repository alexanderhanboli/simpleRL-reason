from huggingface_hub import snapshot_download

model_name = "Qwen/Qwen2.5-Math-7B"
snapshot_id = "b101308fe89651ea5ce025f25317fea6fc07e96e"

snapshot_path = snapshot_download(repo_id=model_name, revision=snapshot_id)

print(f"model path: {snapshot_path}")