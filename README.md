# 33º Projeto Tech News: 
<p align="center">
<img src="https://github.com/prtpj1/prtpj1/blob/main/Headers/33-TechNews.jpg?raw=true" alt="Header" />

---
<p align="center">
<a href="#project-description">Project Description</a> •
<a href="#in-this-project-i-learned-and-put-into-practice">Learning</a> •
<a href="#according-to-the-project-requirements-designated-by-trybe-i-learned-how-to">Requirements</a> •
<a href="#stacks">Stacks</a> •
<a href="#how-to-run-the-application">How to run the application</a>
</p>

---
<p align="center">
<a href="#descrição-do-projeto">Descrição do Projeto</a> •
<a href="#nesse-projeto-aprendi-e-coloquei-em-prática">Aprendizado</a> •
<a href="#de-acordo-com-os-requisitos-do-projeto-designados-pela-trybe-aprendi-como">Requisitos</a> •
<a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a> •
<a href="#como-rodar-a-aplicação">Rodar a Aplicação</a>
</p>

---
## Project Description
I developed this Computer Science project in Python during my learning period at Trybe, where I created functions to query news about technology from a specific website <em>(Trybe blog)</em> through web scraping.

## In this project, I learned and put into practice:
- Using Python's interactive terminal
- Writing my own modules and importing them into other codes
- Applying web scraping techniques
- Extracting data from HTML content
- Storing the retrieved data in a database

---
## According to the project requirements designated by Trybe, I learned how to:
- ✅ Create the `fetch` function
- ✅ Create the `scrape_novidades` function
- ✅ Create the `scrape_next_page_link` function
- ✅ Create the `scrape_noticia` function
- ✅ Create the `get_tech_news` function to fetch the news!
- ✅ Create the `search_by_title` function
- ✅ Create the `search_by_date` function
- ✅ Create the `search_by_tag` function
- ✅ Create the `search_by_category` function
- ✅ Create the `analyzer_menu` function
- ❌ Create the `top_5_news` function
- ❌ Create the `top_5_categories` function
- ❌ Implement the menu functionalities

<em>Note: In some projects, some requirements were not completed due to the accelerated dynamics of the course, not because I didn't know how to do them. At the time, I just needed a little more time.

I still haven't decided if it's better to leave it this way to demonstrate my progress during my learning or if it would be better to complete the requirements that were missing in the course projects.

Feedback is welcome.</em>

---
## Stacks
### BackEnd:
- Docker
- Python

<a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Docker2.png?raw=true" width="50" height="50" alt="Docker Icon" /></a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>

---
## :whale: How to run the application?
- Make sure that 🐋<strong>Docker</strong>🐋 is running on your computer
`systemctl status docker` <em><u>(if so, you will see the word "active" in green)</u></em>
- Clone the repository: <br>
`git clone git@github.com:prtpj1/project-tech-news.git`
- Access the project folder: <br>
`cd project-tech-news`
- Start the container for Docker <em>(the database will be exclusively in Docker)</em>: <br>
`docker-compose up -d`
- Create and enable the virtual environment: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Install the dependencies: <br>
`python3 -m pip install -r dev-requirements.txt`
- While inside the virtual environment  <em>(you will see <strong> <em>(.venv)</em> </strong> in your terminal indicating that the virtual environment is active and you are inside it)</em> type the command: <br>
`start-analyzer`

⚠️<strong>Important notes:</strong>⚠️ 
- The options on this app are in portuguese, as all the news scrapped from trybe's blog.
Below, the menu options to help english users:
```
    0 - Populate the database with news
    1 - Search for news by title
    2 - Search for news by date
    3 - Search for news by tag
    4 - Search for news by category
    5 - List top 5 news
    6 - List top 5 categories
    7 - Exit
```

- <strong>If this is your first time running the program</strong>, start by choosing option 0  <em>(zero)</em> to fill the database with news <em><u>(without this, the other options will not work)</u></em>
- When choosing how many news articles to go into the database, the larger the number, the longer the wait until you can use the other options <em>(the time may vary depending on your computer)</em>.
- If you are searching for keywords without a positive result, you can directly access the database and check all the news downloaded from the blog. To do this, follow the steps below in the terminal by typing the following commands:
  1 - `docker ps` ➡️ this will display the containers that are running
  2 - `docker exec -it <name or id> mongo` ➡️ it must be the container that has the mongo image 
  3 - `use tech_news` ➡️ this will make mongo use the correct database
  4 - `db.news.find().pretty()` ➡️ this will display all the news downloaded from the blog
  5 - `exit` ➡️ exit the mongo terminal

---

<em>Note: If you have any difficulties with the instructions and would like to give feedback, send me a message</em>

---
## Descrição do Projeto
Fiz este projeto de Ciência da Computação em Python durante meu período de aprendizagem na Trybe onde desenvolvi funções para fazer consultas em notícias sobre tecnologia de um site especifico <em>(blog da Trybe)</em> através da raspagem de dados.

---
## Nesse projeto, aprendi e coloquei em prática:
- Utilizar o terminal interativo do Python
- Escrever meus próprios módulos e importá-los em outros códigos
- Aplicar técnicas de raspagem de dados
- Extrair dados de conteúdo HTML
- Armazenar os dados obtidos em um banco de dados

---
## De acordo com os requisitos do projeto designados pela Trybe aprendi como:
- ✅ Criar a função `fetch`
- ✅ Criar a função `scrape_novidades`
- ✅ Criar a função `scrape_next_page_link`
- ✅ Criar a função `scrape_noticia`
- ✅ Criar a função `get_tech_news` para obter as notícias!
- ✅ Criar a função `search_by_title`
- ✅ Criar a função `search_by_date`
- ✅ Criar a função `search_by_tag`
- ✅ Criar a função `search_by_category`
- ✅ Criar a função `analyzer_menu`
- ❌ Criar a função `top_5_news`
- ❌ Criar a função `top_5_categories`
- ❌ Implementar as funcionalidades do menu


OBS: Em alguns projetos alguns requisitos não foram feitos devido a dinâmica acelerada do curso e não por eu não saber como fazê-los. Na época eu apenas precisaria de um pouco mais de tempo.

Ainda não decidi se é melhor deixar desta forma para demonstrar o meu progresso durante meu aprendizado ou se seria melhor completar os requisitos que ficaram faltando nos projetos do curso.

Feedbacks são bem vindos.

---
## Tecnologias Utilizadas
### BackEnd:
- Docker
- Python

<a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Docker2.png?raw=true" width="50" height="50" alt="Docker Icon" /></a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>

---
## :whale: Como rodar a aplicação?
- Confirme que o 🐋<strong>Docker</strong>🐋está rodando no seu computador
`systemctl status docker` <em><u>(se sim, você verá a palavra "active" na cor verde)</u></em>
- Clone o repositório: <br>
`git clone git@github.com:prtpj1/project-tech-news.git`
- Acesse a pasta do projeto: <br>
`cd project-tech-news`
- Suba o container para o Docker<em>(o banco de dados estará exclusivamente no docker)</em>: <br>
`docker-compose up -d`
- Crie e habilite o ambiente virtual: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências: <br>
`python3 -m pip install -r dev-requirements.txt`
- Já dentro do ambiente virtual  <em>(você verá <strong> <em>(.venv)</em> </strong> no seu terminal indicando que o ambiente virtual esta ativo e você esta dentro dele)</em>  digite o comando: <br>
`start-analyzer`

⚠️<strong>Observações importantes:</strong>⚠️ 
- <strong>Se for a primeira vez executando o programa</strong>, comece escolhendo a opção 0  <em>(zero)</em> para preencher o banco de dados com as noticias <em><u>(sem isso as outras opções não funcionarão)</u></em>
- Ao escolher quantas noticias irão para o banco de dados, quanto maior o número, maior será o tempo de espera até você poder usar as outras opções <em>(o tempo pode variar de acordo com o seu computador)</em>.
- Se estiver buscando por palavras sem um resultado positivo, você pode acessar diretamente o banco de dados e verificar todas as noticias baixadas do blog. Para isto, dentro do terminal, siga o passo a passo digitando os comandos abaixo:
  1 - `docker ps` ➡️ vai exibir os containers que estão rodando
  2 - `docker exec -it <nome ou id> mongo` ➡️ tem que ser o container que tem a imagem do mongo 
  3 - `use tech_news` ➡️ isso fará o mongo usar o banco de dados correto
  4 - `db.news.find().pretty()` ➡️ exibirá todas as noticias baixadas do blog
  5 - `exit` ➡️ sair do terminal do mongo

---
<em>OBS: Se tiver alguma dificuldade com as instruções e quiser dar um feedback me mande uma mensagem</em>

