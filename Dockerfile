FROM tensorflow/tensorflow:2.9.1-gpu


#RUN rm /etc/apt/sources.list.d/cuda.list
#RUN rm /etc/apt/sources.list.d/nvidia-ml.list
#RUN apt-key del 7fa2af80
#RUN apt-get update && apt-get install -y --no-install-recommends wget
#RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
#RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt update && \
    apt-get install -y python3-pip vim wget git && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y libglib2.0-0 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/list/*

RUN python3 -m pip install --upgrade pip pillow
RUN pip3 install dominate==2.6.0 visdom==0.1.8.9 wandb==0.12.14 dominate tqdm opencv-python tf_slim scikit-image matplotlib


WORKDIR /workspace
RUN git config --global --add safe.directory /workspace
