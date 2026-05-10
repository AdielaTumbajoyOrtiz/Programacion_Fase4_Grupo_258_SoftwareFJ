import logging
from abc import ABC, abstractmethod

# Configuración de LOGS (Requisito Anexo 3)
logging.basicConfig(filename='software_fj_errores.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Clase Abstracta
class Servicio(ABC):
    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

# Herencia y Polimorfismo
class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas):
        return horas * 15.0

class Cliente:
    def __init__(self, nombre, id_cliente):
        if not nombre: 
            raise ValueError("El nombre es obligatorio")
        self.__nombre = nombre # Encapsulación
        self.__id = id_cliente

    def __str__(self):
        return f"Cliente: {self.__nombre}"

# Manejo de Excepciones y Robustez
def ejecutar_sistema():
    print("--- SOFTWARE FJ ACTIVO ---")
    try:
        # Intento de registro válido
        c = Cliente("Adiela Tumbajoy", "258")
        print(f"Éxito: {c}")
        
        # Intento de registro con error para probar robustez
        c_error = Cliente("", "000")
    except Exception as e:
        logging.error(f"Error detectado: {e}")
        print(f"Manejo de Error: {e}. El sistema NO se detuvo.")
    finally:
        print("Proceso finalizado correctamente.")

if __name__ == "__main__":
    ejecutar_sistema()
