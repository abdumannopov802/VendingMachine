class Ichimlik:
    def __init__(self, ichimlik_nomi, ichimlik_narxi) -> None:
        self.ichimlik_nomi = ichimlik_nomi
        self.ichimlik_narxi = ichimlik_narxi
    
    @property
    def nomi(self):
        return self.ichimlik_nomi
    @property
    def narxi(self):
        return self.ichimlik_narxi
    
    def __str__(self) -> str:
        return f"Ichimlik nomi --> {self.nomi}, narxi --> {self.narxi}"