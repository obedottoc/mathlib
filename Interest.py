class Interest:

    @staticmethod
    def cagr(beginning_value: float, ending_value: float, num_years: int):
        if beginning_value <= 0 or num_years <= 0:
            raise ValueError("Beginning value and number of years must be positive.")
        return (ending_value / beginning_value) ** (1 / num_years) - 1
    
    @staticmethod
    def apr(periodic_rate:float, periods_per_year:int):
        if periods_per_year <= 0:
            raise ValueError("Periods per year must be positive.")
        return periodic_rate * periods_per_year
    
    @staticmethod
    def eir(apr:float, periods_per_year:int):
        if periods_per_year <= 0:
            raise ValueError("Periods per year must be positive.")
        return (1 + apr / periods_per_year) ** periods_per_year - 1