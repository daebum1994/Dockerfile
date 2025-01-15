FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
# 타임존 설정
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
# 필요한 패키지 설치 
RUN add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get install -y locales git wget net-tools vim openssh-server awscli

# 한글 설정
RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8

RUN apt install -y software-properties-common && \       
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    set "CMAKE_ARGS=-DLLAMA_OPENBLAS=on" && \
    set "FORCE_CMAKE=1"

RUN apt-get install -y nano curl wget gcc build-essential && \
    apt-get install gcc-11 g++-11 -y && \
    apt-get install build-essential -y && \
    apt-get install -y cmake

WORKDIR /usr/src/app
COPY ./ ./

# Install miniconda3
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version
RUN conda env list
RUN /bin/bash -c "conda init" 
RUN /bin/bash -c "conda create -n llama_cpp python=3.10 -y" 
RUN /bin/bash -c "source activate llama_cpp && pip install --upgrade pip && pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124 && pip install huggingface_hub" 

ENV export PATH="/usr/local/cuda-12.4/bin:$PATH"
ENV export LD_LIBRARY_PATH="/usr/local/cuda-12.4/lib64:$LD_LIBRARY_PATH"
RUN /bin/bash -c "source ~/.bashrc"

ENV CMAKE_ARGS="-DLLAMA_CUDA=on"
ENV FORCE_CMAKE=1
RUN /bin/bash -c "source activate llama_cpp && CMAKE_ARGS=-DLLAMA_CUBLAS=on FORCE_CMAKE=1 pip install llama-cpp-python==0.3.4 --force-reinstall --upgrade --no-cache-dir --verbose --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124"