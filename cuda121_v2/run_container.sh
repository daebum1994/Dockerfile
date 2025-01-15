docker run -d -it \
 --gpus all \
 -p 6714:6714 \
 -p 6715:6715 \
 -v /home/dockering/dbyuk/docker_container_home:/home/docker/ \
 -v /mnt/seaweedfs/llm_data/:/home/0_data \
 -v /mnt/seaweedfs/llm_models:/home/0_models \
 --shm-size=80gb \
 --name llm_dbyuk llm_cu121:2.0