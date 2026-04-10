import torch
from omegaconf import OmegaConf
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class SentimentClassification:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path)

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
        
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        predicted_class_id = logits.argmax().item()
        confidence = probabilities[0][predicted_class_id].item()

        return {
            "label": self.model.config.id2label[predicted_class_id],
            "confidence": round(confidence, 4)
        }