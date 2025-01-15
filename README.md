## vllm, llama-cpp-python 도커파일 
- Dockerfile 레이어 정리 필요
- vllm 0.4, 0.6
- llama-cpp-python 0.3.4

## llm-DockerFile
- cuda121_v1
  - nvidia driver >= 450
  - CUDA 12.1
  - torch = 2.1.1
  - vllm = 0.4
  - cuda121_v2
  - CUDA 12.1
  - torch = 2.4
  - vllm = 0.6
- cuda118
  - nvidia driver >= 525
  - CUDA 12.1
  - torch = 2.1.1

### Make Image
- ./make_img.sh

### Run Container
- ./run.sh
  - port, volume 설정 확인
- conda 가상환경 확인 후 사용

#### vllm Enable more logging
- 다음 환경 변수를 사용하여 디버깅
```
export VLLM_LOGGING_LEVEL=DEBUG
export CUDA_LAUNCH_BLOCKING=1
export NCCL_DEBUG=TRACE
export VLLM_TRACE_FUNCTION=1
```

### vllm 실행시 NCLL 관련 오류 디버깅 
- NCCL WARN Error: failed to extend
- 컨테이너 shm-size 증가 시켜주면 해결됨.
- example 
```
docker run -d -it \
 --gpus all \
 -p 6711:6711 \
 -v /mnt/seaweedfs/llm_data/:/home/0_data \
 -v /mnt/seaweedfs/llm_models:/home/0_models \
 --shm-size=80gb \
 --name llm_test llm_cu121:2.0
```


