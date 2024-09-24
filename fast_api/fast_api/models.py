class Model:
    def __init__(self):
        # Simular que o modelo foi carregado
        self.class_names = ["positivo", "negativo", "neutro"]  # Definir as classes corretamente

    def predict(self, test):
        # Simulando a predição com uma classe aleatória
        import random
        predicted_class = random.choice(self.class_names)
        confidence = random.uniform(0.7, 1.0)
        probabilities = {class_name: random.uniform(0.0, 1.0) for class_name in self.class_names}
        return predicted_class, confidence, probabilities

model = Model()

def get_model():
    return model

#Apenas um placeholder