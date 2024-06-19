#!/bin/bash

source /home/tqwu/anaconda3/bin/activate moslora_vlm

YOUR_PATH=

export PYTHONPATH="$YOUR_PATH/visual_instruction_tuning"

export OMP_NUM_THREADS=1

export CUDA_VISIBLE_DEVICES= 

p=$YOUR_PATH/kaiming_mix_lora_llava_internlm2_chat_7b_qlora_clip_vit_large_p14_336_lora_e1_gpu4_finetune.py


XTUNER_DATASET_TIMEOUT=120 NPROC_PER_NODE=2 xtuner train $p --deepspeed deepspeed_zero2 --seed 1024

