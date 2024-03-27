import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL
)
from io import BytesIO
import base64
import os


class InferlessPythonModel:
    def initialize(self):
        # Load VAE component
        self.vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix", 
            torch_dtype=torch.float16
        )
        
        # Configure the pipeline
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            "cagliostrolab/animagine-xl-3.0", 
            vae=self.vae,
            torch_dtype=torch.float16, 
            use_safetensors=True, 
        )
        self.pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(self.pipe.scheduler.config)
        self.pipe.to('cuda')


    def infer(self, inputs):
        prompt = inputs["prompt"]
        negative_prompt = inputs["negative_prompt"]
        
        image = self.pipe(
            prompt, 
            negative_prompt=negative_prompt, 
            width=832,
            height=1216,
            guidance_scale=7,
            num_inference_steps=28
        ).images[0]

        buff = BytesIO()
        image.save(buff, format="JPEG")
        img_str = base64.b64encode(buff.getvalue()).decode()
        return { "generated_image_base64" : img_str }
        
    def finalize(self):
        self.pipe = None
