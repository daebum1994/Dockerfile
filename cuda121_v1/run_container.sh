docker run -d -it \
 --gpus all \
 -p 6715:6715 \
 -v /raid/:/home/raid/ \
 --name llm121_dbyuk llm_cu121:1.0
