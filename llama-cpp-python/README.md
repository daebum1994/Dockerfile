# TODO
- [ ] Dockerfile 수정 필요

# INFO
- cuda : 12.4
- OS : ubuntu 22.04
- python : 3.10
- torch : 2.4.1
- llama-cpp-python : 0.3.4


- [github : llama-cpp](https://github.com/ggerganov/llama.cpp)
- [github : llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

# Command r+ 08-2024
- [원본 모델 링크](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024)
- [GGUF 모델 링크](https://huggingface.co/pmysl/c4ai-command-r-plus-GGUF)

# 모델 Convert 사용방법 
- llama-cpp 설치 후 해당 디렉토리에서 수행할 수 있음.
- quantization_type : 
- output format 
  - use f32 for float32
  - f16 for float16
  - bf16 for bfloat16
  - q8_0 for Q8_0
  - tq1_0 or tq2_0 for ternary
  - auto for the highest-fidelity 16-bit float type depending on the first loaded tensor type
- [한글 설명 참고 링크](https://dytis.tistory.com/72)
```
cd llama.cpp
python convert_hf_to_gguf.py [model_path] --outtype [quantization_type]
```

# llama-cpp CUDA 설치
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```