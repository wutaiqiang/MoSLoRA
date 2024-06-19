# Environment

Currently, we need to install all the packages **expect PEFT**, and then use the provided PEFT to finished the training and evalutaion.


We recommend to use the Anaconda following:
```
conda create -n moslora_sd python=3.10
source activate moslora_sd
pip install -r requirements_sdxl.txt
```

After that, you need to install the diffusers:
```
git clone https://github.com/huggingface/diffusers
cd diffusers
pip install .
```

We suggest you use the Wandb for visualization. Just install Wandb via pip and then login. You can refer to [this](https://docs.wandb.ai/ref/python/login).

Then, initializing the accelerate via:
```
accelerate config
```

# Dataset

Get the training data from [here](https://github.com/google/dreambooth/tree/main/dataset)

Also, we provide a folder of cat in this repo.


# Training and Inference

After that, modify the train_sdxl_lora_cat.sh to your own path.

--instance_prompt: the prompt for the input images

--validation_prompt: the prompt for validation

--report_to="wandb": report to wandb

--lora_use_mixer: whether to use mixer


Just use following command to finetune:
```
bash train_sdxl_lora_cat.sh
```

After training, just run the:
```
python3 infer.py
```
to generate the images.


# Acknowledge

This code is modifed based on the [huggingface/diffusers/examples](https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/README_sdxl.md), we thank for their efforts.
