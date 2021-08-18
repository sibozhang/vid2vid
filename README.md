# vid2vid
modifed version of [vid2vid](https://github.com/NVIDIA/vid2vid) for [Speech2Video](https://github.com/sibozhang/Speech2Video) and [Text2Video](https://github.com/sibozhang/Speech2Video).

# Setup
1. git clone
```
git clone git@github.com:sibozhang/vid2vid.git
```

2. setup env
torchvision need to be 0.2.2 to be compatible with torch 0.4.1
```
python3 -m venv ../venv/vid2vid
source ../venv/vid2vid/bin/activate
pip install --upgrade pip
pip3 install https://download.pytorch.org/whl/cu92/torch-0.4.1-cp36-cp36m-linux_x86_64.whl 
pip install torchvision==0.2.2 
pip install numpy==1.16.4
pip install dominate requests
pip install pillow
pip install opencv-python 
pip install scipy 
pip install pytz
```

# Trained model
Please build 'checkpoints' folder in the current folder and put trained model in it.

VidTIMIT fadg0 (Female) [Download](https://www.dropbox.com/sh/lk6et49v2uyfzjx/AADAFAp02_b3FQchaYxOZ0EMa?dl=0)

# Q&A
1. Get vid2vid working
```
*cd vid2vid/models/flownet2_pytorch
*export CUDA_HOME=/tools/cuda-9.2.88/
*comment “--user” in /flownet2_pytorch/install.sh //so it will install to python under venv, otherwise it install to .local
*bash install.sh
```
2.  Q: File "/mnt/scratch/sibo/vid2vid/util/util.py", line 62, in tensor2im
    image_numpy = image_tensor.cpu().float().numpy()
RuntimeError: PyTorch was compiled without NumPy support

A: pip install torch==0.4.1.post2


## Citation
Speech2Video Synthesis with 3D Skeleton Regularization and Expressive Body Poses

Miao Liao*, Sibo Zhang*, Peng Wang, Hao Zhu, Xinxin Zuo, Ruigang Yang. [PDF](https://arxiv.org/pdf/2007.09198.pdf) [Result Video](https://youtu.be/MUlRtgbGeUs)
[1 min Spotlight](https://youtu.be/04oqf7kDzXo) [10 min Presentation](https://youtu.be/E8Dvef0Z4sw)
```
@inproceedings{liao2020speech2video,
  title={Speech2video synthesis with 3D skeleton regularization and expressive body poses},
  author={Liao, Miao and Zhang, Sibo and Wang, Peng and Zhu, Hao and Zuo, Xinxin and Yang, Ruigang},
  booktitle={Proceedings of the Asian Conference on Computer Vision},
  year={2020}
}
```

## Ackowledgements
This code is based on the vid2vid framework.
