first commit

1. Criar um ambiente virtual:
    - Empacota minhas dependĂȘncias
    ```BASH
    virtualenv -p python3 ENV 
    ```
2. Ativar o ambiente virtual:
    ```BASH
    source ENV/bin/activate 
    ``` 
3. Criar arquivo de dependĂȘncias:
    ```BASH
    pip freeze > requirements.txt 
    ```  

4. Para instalar as dependĂȘncias
    ```BASH
    pip install -r requirements.txt 
    ```