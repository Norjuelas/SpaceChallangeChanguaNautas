class CondicionesEspacio:
    def __init__(self, ph=7):
        self.ph = ph

    def definir_ph(self, Fe_percentage, S_percentage, H_percentage):
        """Define el pH del ambiente según los porcentajes de los elementos."""
        if Fe_percentage == 50 and S_percentage == 50:
            self.ph = 7  # Todos mueren
        elif Fe_percentage < 10 and S_percentage < 10:
            self.ph = 7
            if H_percentage > 50:
                self.ph = 5
        else:
            if Fe_percentage > 40:
                self.ph = 9
                if Fe_percentage > 60:
                    self.ph = 11
                    if Fe_percentage > 90:
                        self.ph = 14

            if S_percentage > 40:
                self.ph = 5
                if S_percentage > 60:
                    self.ph = 3
                    if S_percentage > 90:
                        self.ph = 1  # Inviable

    def ajustar_condiciones(self, organismo):
        """Ajusta la vida del organismo según el pH."""
        if self.ph <= 3:
            print(f"El organismo {organismo.behavior} no sobrevive debido al pH extremadamente ácido.")
        elif self.ph >= 11:
            print(f"El organismo {organismo.behavior} no sobrevive debido al pH extremadamente alcalino.")
        else:
            print(f"El organismo {organismo.behavior} puede sobrevivir en el pH actual: {self.ph}.")
