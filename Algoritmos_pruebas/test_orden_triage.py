"""
Pruebas unitarias del algoritmo de orden por triage.

Ejecutar:  python -m unittest test_orden_triage.py
"""
import unittest

from orden_triage import ordenar_por_triage


class TestOrdenTriage(unittest.TestCase):

    def test_atiende_primero_el_triage_mas_urgente(self):
        pacientes = [
            {"nombre": "A", "triage": 4, "llegada": "07:00"},
            {"nombre": "B", "triage": 1, "llegada": "09:00"},
        ]
        orden = [p["nombre"] for p in ordenar_por_triage(pacientes)]
        self.assertEqual(orden, ["B", "A"])

    def test_mismo_triage_atiende_primero_al_que_llego_antes(self):
        pacientes = [
            {"nombre": "A", "triage": 3, "llegada": "08:30"},
            {"nombre": "B", "triage": 3, "llegada": "08:10"},
        ]
        orden = [p["nombre"] for p in ordenar_por_triage(pacientes)]
        self.assertEqual(orden, ["B", "A"])

    def test_rechaza_triage_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            ordenar_por_triage([{"nombre": "A", "triage": 7, "llegada": "08:00"}])

    def test_lista_vacia(self):
        self.assertEqual(ordenar_por_triage([]), [])


if __name__ == "__main__":
    unittest.main()
