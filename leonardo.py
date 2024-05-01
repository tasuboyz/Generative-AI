import requests
import instance
import config

class LeonardoAI:
    def __init__(self):
        self.admin_id = config.admin_id
        self.bot = instance.bot
        self.url = "https://cloud.leonardo.ai/api/rest/v1"
        self.url_gen =f"{self.url}/generations"
        self.url_element = f"{self.url}/elements"
        self.url_model = f"{self.url}/platformModels"
        self.token = config.leonardo_token
        self.leonardo_diffusion_XL = "1e60896f-3c26-4296-8ecc-53e2afecc132"
        self.PhotoReal_model = "b75a5b32-ca22-4b1d-bb0a-883c26783c71"
        self.test_model = 'b700cad2-0e4b-422a-a794-781f20d1e89e'
        self.headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.token}"
        }
        
    def generation(self, prompt, alchemy=False, highContrast=False, highResolution=False, photoReal=False, elements=None, model_id=None, size="512x512"):
        width = size.split("x")[0]
        height = size.split("x")[1]
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.token}"
        }
        payload = {
            "height": int(height),
            "prompt": prompt,
            "width": int(width),
            "num_images": 1,
            "alchemy": alchemy,
            "guidance_scale": 7,
            "highContrast": highContrast,
            "highResolution": highResolution,
            #"modelId" : self.leonardo_diffusion_XL,
            "photoReal": photoReal,
            #"photoRealStrength": 0.5,
            "negative_prompt": "too many feet, too many fingers, long neck, 2 heads, duplicate, abstract, disfigured, deformed, figure, framed, disfigured, bad art, deformed, poorly drawn, extra limbs, weird colors, 2 heads, elongated body, cropped image, out of frame, draft, deformed hands, twisted fingers, double image, malformed hands, multiple heads, extra limb, ugly, poorly drawn hands, missing limb, cut-off, over satured, grain, lowères, bad anatomy, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, out of focus, long body, disgusting, extra fingers, groos proportions, missing arms, mutated hands, cloned face, missing legs"
        }
        if alchemy or photoReal:
            payload["presetStyle"] = "CINEMATIC"
        else:
            payload["presetStyle"] = "LEONARDO"
            
        if photoReal:
            payload["alchemy"] = True
            payload["photoRealVersion"] = "v2"
            payload["modelId"] = model_id
            # payload["modelId"] = None
        else:
            payload["modelId"] = model_id

        if elements is not None:
            elements = {key: float(value) for key, value in elements.items()}
            payload["elements"] = [{"akUUID": id, "weight": weight} for id, weight in elements.items()]
        else:
            payload["elements"] = None

        response = requests.post(self.url_gen, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return f"Error: {response.text}"
        
    def get_image(self, generation_id, prompt=None):
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
        response = requests.get(url, headers=self.headers)
        result = response.json()
        result = result["generations_by_pk"]
        result = result["generated_images"]
        result = result[0]
        return result["url"]
    
    # def get_image(self, generation_id, prompt):
    #     prompt = self.clean_prompt_for_url(prompt)
    #     if prompt.endswith('_'):
    #         prompt = prompt[:-1]
    #     url =f"https://cdn.leonardo.ai/users/8d44b3af-399e-4af0-a041-483d44f48cac/generations/{generation_id}/Default_{prompt}_0.jpg"
    #     return url
    
    def clean_prompt_for_url(self, prompt: str) -> str:
        cleaned_prompt = "".join(c if c.isalnum() else "_" for c in prompt)
        cleaned_prompt = cleaned_prompt.rstrip("_")
        cleaned_prompt = cleaned_prompt.lstrip("_")
        while "__" in cleaned_prompt:
            cleaned_prompt = cleaned_prompt.replace("__", "_")
        cleaned_prompt = cleaned_prompt[:54]        
        return cleaned_prompt
 
    def get_element(self):
        response = requests.get(self.url_element, headers=self.headers)
        result = response.json()
        return result
    
    def get_model(self):
        response = requests.get(self.url_model, headers=self.headers)
        result = response.json()
        return result


