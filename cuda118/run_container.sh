docker run -d -it \
 --gpus all \
 -p 6711:6711 \
 -v /raid/:/home/raid/ \
 --name llm118_dbyuk  llm_cu118:1.0

