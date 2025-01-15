FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN apt-get update && apt-get install -y locales git wget net-tools vim openssh-server awscli
RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
RUN \    
    apt-get update && \
    apt-get install -y nano curl wget gcc build-essential sudo

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
RUN /bin/bash -c "conda create -n llm python=3.10 -y" 
RUN /bin/bash -c "source activate llm && pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118" 

    
    
