import json
from core.modelos import DataLoader, StatsService

def main():
    loader = DataLoader("data/dados.csv")
    df = loader.load()

    service = StatsService(df)

    stats = {
        "qtd_total": service.qtd_total(),
        "receita_total": service.receita_total(),
        "preco_medio": service.preco_medio(),
        "desafio_fp": service.desafio_fp("qtd", limite=2)
    }

    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    main()