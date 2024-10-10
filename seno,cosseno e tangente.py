import math

def calcular_trigonometricas(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    return seno, cosseno, tangente

# Solicitar entrada do usuário
angulo = float(input("Digite o ângulo em graus: "))

# Calcular seno, cosseno e tangente
seno, cosseno, tangente = calcular_trigonometricas(angulo)

# Exibir os resultados
print(f"Seno de {angulo}°: {seno:.4f}")
print(f"Cosseno de {angulo}°: {cosseno:.4f}")
print(f"Tangente de {angulo}°: {tangente:.4f}")
