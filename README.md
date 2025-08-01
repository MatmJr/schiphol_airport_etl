# ✈️ schiphol\_airport\_etl

Este projeto realiza um processo de **ETL (Extract, Transform, Load)** dos dados da [**API do Aeroporto de Schiphol**](https://www.schiphol.nl/en/developer-center/our-flight-api-explored/), na Holanda. A partir dos dados extraídos, são realizadas análises e visualizações interativas em um dashboard desenvolvido com Streamlit.

## 📂 Estrutura do Repositório

* `analises/` – Contém os notebooks ou scripts com a **análise de dados** realizada após o ETL.
* `dashboards/` – Contém o **dashboard em Streamlit**, com visualizações baseadas nos dados transformados.
* `etl/` – Módulo responsável por **extrair, transformar e carregar** os dados da API.
* `main.py` – Arquivo principal para **executar o processo de ETL** completo.

## 🔐 Configuração de Variáveis de Ambiente

Para acessar a API do Schiphol, você precisa de um **APP\_ID** e **APP\_KEY**. Para isso:

1. Acesse o site oficial da API e realize seu cadastro para obter as credenciais.
2. Crie um arquivo chamado **`.env`** na **raiz do projeto** com o seguinte conteúdo:

```
APP_ID=seu_app_id_aqui
APP_KEY=sua_app_key_aqui
```

> O projeto utiliza a biblioteca `python-dotenv` para carregar essas variáveis de forma segura.

## ⚙️ Como Executar o Projeto

### 1. Crie um ambiente virtual (recomendado)

No terminal, execute:

```bash
python -m venv venv
```

Ative o ambiente virtual:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

### 2. Instale as dependências

Certifique-se de que o arquivo `requirements.txt` esteja presente na raiz do projeto e execute:

```bash
pip install -r requirements.txt
```

### 3. Execute o pipeline ETL

Para extrair os dados da API, transformá-los e salvá-los em CSV:

```bash
python main.py
```

### 4. Execute o dashboard interativo

Após a execução da ETL, você pode visualizar os insights no dashboard com:

```bash
streamlit run dashboards/dashboard.py
```

