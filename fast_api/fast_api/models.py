class Model:
    def __init__(self):
        # Simular que o modelo foi carregado
        self.class_names = ["positivo", "negativo", "neutro"]  # Definir as classes corretamente

    def predict(self, test):
        import random
               # Gerando valores aleatórios para as classes
        probabilities = {
            "positivo": random.uniform(0, 1),
            "negativo": random.uniform(0, 1),
            "neutro": random.uniform(0, 1)
        }

        # Encontrando a classe com o maior valor
        predicted_class = max(probabilities, key=probabilities.get)
        
        # A confiança será o valor da classe prevista
        confidence = probabilities[predicted_class]

        return predicted_class, confidence, probabilities


model = Model()

def get_model():
    return model

#Apenas um placeholder