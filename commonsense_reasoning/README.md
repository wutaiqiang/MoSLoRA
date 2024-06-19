# Environment

Currently, we need to install all the packages **expect PEFT**, and then use the provided PEFT to finished the training and evalutaion.

We recommend to use the Anaconda following:
```
conda create -n moslora python=3.10
source activate moslora
pip install -r requirements.txt
```

# Dataset

Get the train data and benchmarks from [here](https://github.com/AGI-Edgerunners/LLM-Adapters)

# Training and Inference

After that, modify the train_moslora.sh to your own path.

--model_p_or_n: the path or name of model

remove the --use_moslora and you would get the results of vanilla LoRA.

Just use:
```
bash train_moslora.sh
```

# Acknowledge

This code is modifed based on the [LLM-Adapters](https://github.com/AGI-Edgerunners/LLM-Adapters), we thank for their efforts.
