# Nerdstore
<h3>Projeto, crawler de e-comerce, extraindo alguns produtos específicos</br></h3>
1 - Criado projeto e confiruando o mesmo(database postgresql) </br>
2 - Criado APP Main e o Modelo Produto e Test do model</br>
3 - Adicionando rest_framwork, serializer model Produto </br>
4 - Adiconando scrapy </br>
5 - Craindo projeto scrapy chamado scraper </br>
6 - Criando spider chamdo nerdstore </br>
7 - fazendo tratamento(<b>method: process_item</b>) dos dados e salvando no banco </br>
8 - criando comando para rodar o crawler dentro do app 'main' </br>
<h3>Intruções para rodar o projeto</br></h3>
1 - Partindo do pressuposto que o ambiende de desenvolvimento esteja instalado corretamente(crie banco no postgres), rode o seguinte commando: <b>pip install -r requirimentos.txt </b> </br>
2 - Rodando as migrações com o comando: <b>./manage.py migrate</b></br>
3 - Criando usuário administrador(opcional) com o comando: <b>./manage.py createsuperuser</b></br>
4 - Rodando spider para coleta de dados com o comando: <b>./manage.py crawl</b></br>
5 - Inicie o servidor com o comando: <b>./manage.py runserver</b></br>
6 - Acesse a url <b>http://localhost:8000/products/</b> </br>

