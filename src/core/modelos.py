import pandas as pd
from core.metrics import analisar

class DataLoader:
    """Responsável por carregar e validar os dados CSV."""

    def __init__(self, path: str):
        self.path = path

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)

        colunas_obrigatorias = {"produto", "preco", "qtd"}
        if not colunas_obrigatorias.issubset(df.columns):
            raise ValueError("CSV não possui as colunas mínimas necessárias")

        return df


class StatsService:
    """Serviço responsável pelo cálculo das estatísticas."""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df["receita"] = self.df["preco"] * self.df["qtd"]

    def qtd_total(self) -> int:
        return int(self.df["qtd"].sum())

    def receita_total(self) -> float:
        return float(self.df["receita"].sum())

    def preco_medio(self) -> float:
        return float(self.df["preco"].mean())

    def desafio_fp(self, coluna: str, limite: int) -> dict:
        return analisar(self.df[coluna].tolist(), limite)
``