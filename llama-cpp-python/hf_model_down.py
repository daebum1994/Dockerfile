from huggingface_hub import hf_hub_download

#https://huggingface.co/pmysl/c4ai-command-r-plus-GGUF
# Hugging Face 리포지토리와 파일 정보
repo_id = "lmstudio-community/c4ai-command-r-08-2024-GGUF"
filename = "c4ai-command-r-08-2024-Q8_0.gguf"

# 파일 다운로드
file_path = hf_hub_download(repo_id=repo_id, local_dir="./", filename=filename)
print(f"파일이 다운로드되었습니다: {file_path}")


