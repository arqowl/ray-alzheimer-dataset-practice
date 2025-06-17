# Análise de Biomarcadores para Predição da Doença de Alzheimer

Este projeto utiliza um modelo de Machine Learning com PyTorch para classificar pacientes como portadores da Doença de Alzheimer (AD) ou como parte do grupo de controle, com base em um conjunto de biomarcadores sanguíneos. O fluxo de trabalho completo, desde o carregamento dos dados até a avaliação do modelo, é orquestrado no notebook Jupyter `biomarkers_notebook.ipynb`.

## Estrutura dos Arquivos

* **`biomarkers_notebook.ipynb`**: Notebook principal que contém todo o processo, desde a verificação do ambiente (GPU) até o treinamento e avaliação do modelo.
* **`datasets.py`**: Script Python que define a classe `RayAlzheymerDataset`, responsável por carregar os dados do arquivo CSV e prepará-los para o PyTorch.
* **`models.py`**: Script que define a arquitetura da rede neural, a classe `MLPModel`.

---

## Fluxo de Trabalho Detalhado

### 1. Carregamento e Preparação dos Dados (`datasets.py`)

O arquivo `datasets.py` é fundamental para a organização e o pré-processamento dos dados.

* **Classe `RayAlzheymerDataset`**: O script define uma classe que herda da classe `Dataset` do PyTorch.
* **Leitura do CSV**: O código lê os arquivos de dados, como `AD-Train-120.csv` e `AD-Test-120.csv`. Ele está configurado para usar `;` como delimitador de colunas e `,` como separador decimal.
* **Seleção de Features (Biomarcadores)**: Um passo crucial do pré-processamento é a seleção de features. O código seleciona apenas **18 biomarcadores específicos** para treinar o modelo, além da coluna `CLASS`. Os biomarcadores selecionados são:
    > "ANG-2", "RANTES", "MCP-3", "HCC-4", "PARC", "IL-8", "EGF", "GCSF", "GDNF", "ICAM-1", "IGFBP-6", "IL-1a", "IL-3", "IL-11", "M-CSF", "PDGF-BB", "TNF-a", "TRAIL R4".
* **Codificação dos Rótulos**: A classe converte a coluna de texto `CLASS` em um formato numérico, onde a classe 'AD' se torna `1` e as outras se tornam `0`.
* **Conversão para Tensores**: Ao final do processo, os dados (features) e os rótulos (labels) são convertidos em tensores do PyTorch.

### 2. Arquitetura do Modelo (`models.py`)

O modelo de classificação é definido no arquivo `models.py`.

* **Classe `MLPModel`**: O nome da classe que define o modelo é `MLPModel`.
* **Estrutura**: O modelo consiste em uma **única camada linear (`nn.Linear`)** que mapeia os dados de entrada para a saída.
* **Funcionalidade**: A saída da camada linear passa por uma **função de ativação sigmoide (`torch.sigmoid`)**. O parâmetro `hidden_channels` é definido no notebook (`128`), mas não é utilizado na arquitetura do modelo.

### 3. Treinamento e Avaliação (`biomarkers_notebook.ipynb`)

O notebook `biomarkers_notebook.ipynb` une as etapas de dados e modelo para executar o experimento completo.

* **Configuração do Ambiente**: O notebook inicia verificando a disponibilidade de uma GPU (CUDA) e a define como o `device` a ser usado.
* **DataLoaders**: Os dados de treino e teste são carregados em `DataLoader`s com um tamanho de lote (batch size) de 32. O `DataLoader` de treino é configurado para embaralhar (`shuffle=True`) os dados a cada época.
* **Treinamento**:
    * **Otimizador**: Utiliza o otimizador `Adam` com uma taxa de aprendizado (`learning_rate`) de 0.001 e um `weight_decay` de 1e-5.
    * **Função de Perda (Loss)**: Usa a `nn.BCELoss` (Binary Cross-Entropy Loss) como critério.
    * **Loop de Treinamento**: O modelo é treinado por 100 épocas. A saída do notebook mostra que a perda (loss) diminui progressivamente de um valor inicial de 0.6325 para 0.3888.
* **Avaliação**: Após o treinamento, o desempenho do modelo é medido no conjunto de teste. Os resultados são:
    * **Acurácia**: **95.06%**.
    * **F1 Score**: **0.6829**.
    * **Curva ROC (AUC)**: A área sob a curva é de **0.96**.

## Como Executar

1.  **Ambiente**: Certifique-se de ter um ambiente Python com `torch`, `pandas`, `scikit-learn` e `matplotlib` instalados.
2.  **Estrutura de Diretórios**: Os arquivos de dados (`AD-Train-120.csv`, etc.) devem estar localizados em um diretório `datasets/ray_dataset/`.
3.  **Execução**: Abra e execute as células do notebook `biomarkers_notebook.ipynb` em ordem.

## Conclusão

O projeto demonstra que é possível desenvolver um classificador de alto desempenho para a Doença de Alzheimer. O resultado sugere que o subconjunto de 18 biomarcadores selecionados é um conjunto de features com alta relevância para a distinção entre pacientes com AD e o grupo de controle, dado o alto desempenho do modelo.
