import time
from llama_cpp import Llama

start_time = time.time()
model_path = "./c4ai-command-r-08-2024-Q8_0.gguf"

#n_gpu_layers: Number of layers to offload to GPU (-ngl). If -1, all layers are offloaded
llm = Llama(model_path=model_path, n_ctx=2048, n_gpu_layers=-1, flash_attn=True)
output = llm(
      "<|START_OF_TURN_TOKEN|><|USER_TOKEN|>Who are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>", # Prompt
      max_tokens=1024, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["<|END_OF_TURN_TOKEN|>"], # Stop generating just before the model would generate a new question
      echo=False # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

print(output["choices"][0]["text"])
end_time = time.time()
elapsed_time = end_time - start_time  # 실행 시간 계산
print(f"Elapsed time: {elapsed_time:.2f} seconds")

"<|START_OF_TURN_TOKEN|><|USER_TOKEN|>Who are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"