# API em Python com framework Django e OpenApi Spec

## Dependências

* Python >= 3.8
* Django >= 3.0

## Criando a aplicação

```sh
mkdir usersapi
cd usersapi

python3 -m venv env
source env/bin/activate

pip install django
pip install djangorestframework

django-admin startproject usersapi .
cd usersapi
django-admin startapp quickstart
cd ..

python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
```

## Configurando a aplicação

Com a aplicação criada, execute os passos abaixo.

1. Crie o serializers.py
2. Crie o views.py
3. Crie o urls.py
4. Configure o settings.py
5. Instale as dependências

```sh
pip3 install drf-spectacular
pip3 install django-rest-swagger
```

6. Configure as *annotations* da OpenApi Spec para cada recurso no views.py, como feito neste projeto.

Foi utilizado o drf-spectacular por conta da sua capacidade de gerar OpenAPI Spec 3.0 e customizar diversas informações através das *annotations*.

Para mais informações utilize as [referências](##referências).

## Executando a aplicação

```sh
python manage.py runserver
```

## Testando

Com a aplicação executando:

* Você pode acessar a url http://127.0.0.1:8000/users/ no navegador e utilizar a UI para interagir com a API.
* Você pode consumir os recursos via curl ou Postman

```sh
curl http://127.0.0.1:8000/users/ 
```

* Você pode acessar a interface do swagger através da url http://127.0.0.1:8000/docs/

## Exportando a OpenApi Spec

```sh
python ./manage.py generateschema --file openapi-schema.yml
```

## Referências

* [Django - tutorial](https://www.django-rest-framework.org/usersapi/quickstart/#quickstart)
* [Django - exemplo](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)
* [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html)
