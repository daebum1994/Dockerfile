docker run -d -it \
 --gpus all \
 -v /home/dockering/dbyuk/:/home/ \
 -v /mnt/seaweedfs/llm_data/:/home/0_data \
 -v /mnt/seaweedfs/llm_models:/home/0_models \
 --shm-size=80gb \
 --name llama_cpp_python_dbyuk llama_cpp_python:1.0
