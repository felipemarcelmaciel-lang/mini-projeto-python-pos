# Mini‑Projeto Integrado em Python

# Mini‑Projeto Integrado em Python

## 📚 Disciplina
**Linguagem Python — Pós‑Graduação**  
Professor: Raphael Mauricio Sanches de Jesus  

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo consolidar os conceitos fundamentais da linguagem Python aplicados ao contexto de análise de dados e desenvolvimento de APIs, conforme abordado ao longo da disciplina.

Foram utilizados os seguintes pilares estudados em aula:

- Manipulação e análise de dados com **Pandas**;
- Aplicação de **Programação Funcional**, utilizando exclusivamente as funções `map`, `filter` e `reduce`;
- Desenvolvimento de uma **API REST** com o framework **FastAPI**;
- Aplicação de **Orientação a Objetos (POO)** para melhoria da organização, coesão e reutilização do código;
- Implementação de uma **interface interativa com Streamlit** para consumo da API e visualização dos dados.

---
## 📦 Tecnologias Utilizadas

- Python 3  
- Pandas  
- FastAPI  
- Pydantic  
- Uvicorn  
- Streamlit  
- Matplotlib  

---

## ⚙️ Instalação do Projeto

Clone o repositório e instale as dependências necessárias:

```bash
pip install -r requirements.txt


📊 Geração das Estatísticas
Para gerar o arquivo stats.json, execute o script responsável pela leitura do arquivo CSV e pelo cálculo das métricas estatísticas:
python src/make_stats.py

O arquivo stats.json será criado automaticamente na raiz do projeto contendo:

Quantidade total (qtd_total);
Receita total (receita_total);
Preço médio (preco_medio);
Resultado do mini‑desafio de Programação Funcional.


🌐 Execução da API (FastAPI)
Para iniciar o servidor da API, execute o comando:
uvicorn src.app:app --reload

A API ficará disponível no endereço:
http://127.0.0.1:8000

Endpoints Disponíveis


GET /health
Retorna o status da aplicação.


GET /stats
Retorna o conteúdo do arquivo stats.json.


POST /soma
Recebe dois valores numéricos no formato JSON e retorna sua soma.


Documentação Interativa (Swagger)
http://127.0.0.1:8000/docs


🖥️ Interface Streamlit (Opcional)
Foi desenvolvida uma interface interativa utilizando Streamlit, que consome a API FastAPI e permite:

Visualização das métricas estatísticas;
Exibição de um gráfico simples;
Teste interativo do endpoint /soma.

Para executar a interface Streamlit:
streamlit run ui/app.py

⚠️ Observação: A API FastAPI deve estar em execução simultaneamente para o correto funcionamento da interface.

✅ Considerações Finais
O projeto atende integralmente aos requisitos propostos na avaliação, contemplando os conceitos fundamentais da disciplina e boas práticas de desenvolvimento em Python. A utilização conjunta de Programação Funcional, Orientação a Objetos e integração entre API e interface gráfica resulta em uma solução coesa, organizada e extensível, adequada ao nível de uma pós‑graduação.

