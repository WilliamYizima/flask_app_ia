first commit

1. Criar um ambiente virtual:
    - Empacota minhas dependências
    ```BASH
    virtualenv -p python3 ENV 
    ```
2. Ativar o ambiente virtual:
    ```BASH
    source ENV/bin/activate 
    ``` 
3. Criar arquivo de dependências:
    ```BASH
    pip freeze > requirements.txt 
    ```  

4. Para instalar as dependências
    ```BASH
    pip install -r requirements.txt 
    ```