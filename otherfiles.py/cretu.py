import pandas as pd
import financial_functs as ff
# Création d'un DataFrame avec des rendements journaliers simulés
data = {
    'A_DR': [0.5, -0.2, 0.3, 0.1, -0.1],  # Rendements journaliers pour l'action A
    'B_DR': [-0.3, 0.4, -0.2, 0.2, 0.1],  # Rendements journaliers pour l'action B
}

closing_df = pd.DataFrame(data)

print(ff.calculate_daily_returns(closing_df))
