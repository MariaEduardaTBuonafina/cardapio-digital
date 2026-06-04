# 🍽️ Cardápio Digital — Cantina da Squad

![Build Status](https://github.com/SEU-USUARIO/cardapio-digital/actions/workflows/docker-build.yml/badge.svg)

> Projeto final da disciplina de DevOps — AV2.
> Aplicação web de cardápio digital com backend em Python/Flask e frontend em HTML/CSS/JavaScript, containerizada com Docker e com pipeline de CI/CD via GitHub Actions.

---

## 📋 Sobre o Projeto

O **Cardápio Digital da Cantina da Squad** é uma aplicação web que exibe um menu interativo de restaurante. O backend fornece os dados do cardápio através de uma API REST, e o frontend consome essa API e exibe as informações de forma elegante ao usuário.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | Python 3.11 + Flask |
| **Frontend** | HTML5 + CSS3 + JavaScript |
| **Servidor Web** | Nginx (Alpine) |
| **Containerização** | Docker + Docker Compose |
| **CI/CD** | GitHub Actions |
| **Controle de Versão** | Git + GitHub |

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/SEU-USUARIO/cardapio-digital.git
cd cardapio-digital
```

**2. Copie o arquivo de variáveis de ambiente:**
```bash
cp .env.example .env
```

**3. Suba os containers com Docker Compose:**
```bash
docker compose up --build
```

**4. Acesse a aplicação no navegador:**
- 🌐 **Frontend:** http://localhost:8080
- 🔌 **API Backend:** http://localhost:5000/cardapio

**5. Para parar os containers:**
```bash
docker compose down
```

---

## 👥 Equipe

| Nome | Contribuição |
|------|-------------|
| Maria Eduarda Trevizane | Estrutura base do projeto e Backend (Flask API) |
| João Vitor Rodrigues | Frontend (HTML, CSS, JavaScript) |
| Maria Clara Trevizane | Dockerfiles e Docker Compose |
| Luís Fernando Andrade | GitHub Actions (CI/CD) e Documentação |

---

## 📁 Estrutura do Projeto
cardapio-digital/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── .gitignore
├── .env.example
├── docker-compose.yml
└── README.md