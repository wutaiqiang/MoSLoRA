from huggingface_hub.repocard import RepoCard
from diffusers import DiffusionPipeline
import torch
import os

model = "stabilityai/stable-diffusion-xl-base-1.0"

subject="cat"
templates = [
    "A picture of a ikat {} in the jungle",
    "A picture of a ikat {} in the snow",
    "A picture of a ikat {} on the beach",
    "A picture of a ikat {} on a cobblestone street",
    "A picture of a ikat {} on top of pink fabric",
    "A picture of a ikat {} on top of a wooden floor",
    "A picture of a ikat {} with a city in the background",
    "A picture of a ikat {} with a mountain in the background",
    "A picture of a ikat {} with a blue house in the background",
    "A picture of a ikat {} on top of a purple rug in a forest",
    "A picture of a ikat {} with a wheat field in the background",
    "A picture of a ikat {} with a tree and autumn leaves in the background",
    "A picture of a ikat {} with the Eiffel Tower in the background",
    "A picture of a ikat {} floating on top of water",
    "A picture of a ikat {} floating in an ocean of milk",
    "A picture of a ikat {} on top of green grass with sunflowers around it",
    "A picture of a ikat {} on top of a mirror",
    "A picture of a ikat {} on top of the sidewalk in a crowded street",
    "A picture of a ikat {} on top of a dirt road",
    "A picture of a ikat {} on top of a white rug",
    "A picture of a red ikat {}",
    "A picture of a purple ikat {}",
    "A picture of a shiny ikat {}",
    "A picture of a wet ikat {}",
    "A picture of a cube shaped ikat {}",
]


prompts = [template.format(subject) for template in templates]


for method in ["lora", "lora-mixer"]:
    if method == "lora":
        path = "./lora-trained-xl-{}".format(subject.replace(" ", "_"))
    elif method == "lora-mixer":
        path = "./lora-trained-xl-mixer-{}".format(subject.replace(" ", "_"))

    pipe = DiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    pipe.load_lora_weights(path)

    for prompt in prompts:
        print(prompt)
        image = pipe(prompt, num_inference_steps=50).images[0]

        output_p_dir="output_images/{}/{}".format(subject, prompt.replace(" ", "_"))

        os.makedirs(output_p_dir, exist_ok=True)

        image.save("{}/{}.jpg".format(output_p_dir, method))