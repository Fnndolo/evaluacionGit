"""
Algoritmo basico: orden de atencion de pacientes segun el nivel de triage.

Contexto: EPS - apoyo al microservicio de citas / urgencias.
Regla: se atiende primero el nivel de triage mas critico (1 = mas urgente,
5 = menos urgente). Si dos pacientes tienen el mismo nivel, se atiende
primero a quien llego antes.

Ejecutar:  python orden_triage.py
"""


def ordenar_por_triage(pacientes):
    """Devuelve una nueva lista de pacientes en el orden en que deben ser atendidos."""
    for paciente in pacientes:
        if not 1 <= paciente["triage"] <= 5:
            raise ValueError(f"Triage invalido para {paciente['nombre']}: {paciente['triage']}")
    # La hora de llegada usa formato HH:MM, por eso se puede comparar como texto.
    return sorted(pacientes, key=lambda p: (p["triage"], p["llegada"]))


if __name__ == "__main__":
    sala_de_espera = [
        {"nombre": "Ana", "triage": 3, "llegada": "08:05"},
        {"nombre": "Luis", "triage": 1, "llegada": "08:20"},
        {"nombre": "Marta", "triage": 3, "llegada": "07:50"},
        {"nombre": "Carlos", "triage": 5, "llegada": "07:30"},
        {"nombre": "Sofia", "triage": 2, "llegada": "08:10"},
    ]

    print("Orden de atencion:")
    for turno, p in enumerate(ordenar_por_triage(sala_de_espera), start=1):
        print(f"{turno}. {p['nombre']} (triage {p['triage']}, llego a las {p['llegada']})")
