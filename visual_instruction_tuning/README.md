# Environment

Currently, we need to install all the packages **expect PEFT**, and then use the provided PEFT to finished the training and evalutaion.


We recommend to use the Anaconda following:
```
conda create --name moslora_vlm python=3.10 -y
source activate moslora_vlm
```

After that, you need to install the xtuer:
```
git clone https://github.com/InternLM/xtuner.git
cd xtuner
```
Then, do some modifications in xtuner/requirements/runtime.txt, including

- delete: peft>=0.4.0 
- add: accelerate==0.29.3 
- modify: torch -> torch==2.1.2;  torchvision -> torchvision==0.16.2; mmengine>=0.10.3 -> mmengine==0.10.3

Then, run the command to install xtuner:
```
pip install .
```


# Dataset and Pretrained weight

Get the training data following [here](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/dataset_prepare.md#llava-dataset). Since we just finetune the model without pretraining the project, so no need to get the LLaVA-Pretrain folder.

The data structure:

```
./data/llava_data
├── LLaVA-Instruct-150K
│   └── llava_v1_5_mix665k.json
└── llava_images
    ├── coco
    │   └── train2017
    ├── gqa
    │   └── images
    ├── ocr_vqa
    │   └── images
    ├── textvqa
    │   └── train_images
    └── vg
        ├── VG_100K
        └── VG_100K_2
```

Then, downloading the pretrained projects: 

[LLaMA 3](https://huggingface.co/xtuner/llava-llama-3-8b-pretrain/tree/main) |
[InternLM2](https://huggingface.co/xtuner/llava-internlm2-7b-pretrain/tree/main)


# Training and Inference

After that, modify the parameters:

-- llm_name_or_path 
-- visual_encoder_name_or_path 
-- pretrained_pth

in the provided python file (kaiming_*.py). 

And modify the start.sh to set YOUR_PATH and CUDA_VISIBLE_DEVICES.

Run
```
bash start.sh
```
to train.

After training, you need to merge the weights following [this](https://github.com/InternLM/xtuner/blob/main/xtuner/configs/llava/README.md#model-conversion-and-merge). 

Therefore, you can used the trained and converted weights for evalutions using [VLMEvalKit](https://github.com/open-compass/VLMEvalKit).

## Initialization of Mixer

Change the code in this [line]() to switch the initialization method.


# Acknowledge

This code is modifed based on the [xtuner](https://github.com/InternLM/xtuner/blob/main/xtuner/configs/llava/README.md), we thank for their efforts.
