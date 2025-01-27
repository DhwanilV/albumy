import os.path

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
load_dotenv()

class CV():
    def __init__(self):
        self.endpoint = os.getenv("ENDPOINT")
        self.key = os.getenv("KEY")
        self.credentials = CognitiveServicesCredentials(self.key)
        self.client = ComputerVisionClient(
            endpoint=self.endpoint,
            credentials=self.credentials
        )

    def analyze_image(self, image_path):
        with open(image_path, "rb") as image_stream:
            image_analysis = self.client.analyze_image_in_stream(
                image_stream, 
                visual_features=[
                    VisualFeatureTypes.tags,
                    VisualFeatureTypes.description
                ]
            )
            
            description = image_analysis.description.captions[0].text
            tags = [tag.name for tag in image_analysis.tags]
            print(tags)
            return description, tags