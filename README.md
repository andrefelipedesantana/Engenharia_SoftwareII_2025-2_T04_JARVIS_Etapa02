# ⚙️ Atividade 2 – Gerência de Configuração  
**Engenharia de Software II**

Este repositório contém todos os **artefatos, evidências, scripts, prompts, análises manuais e análises via Inteligência Artificial** utilizados na **Atividade 02** da disciplina de **Engenharia de Software II**.

O foco desta etapa foi a **análise das estratégias de Gerência de Configuração** do projeto **microsoft/JARVIS (HuggingGPT)**, com ênfase em:

- Modelo de fluxo de trabalho (Branching Model)
- Estratégia de releases
- Uso de branches, merges, tags e histórico de commits
- Grau de maturidade do processo de versionamento

---

## 💡 Projeto Analisado — JARVIS (HuggingGPT)

O **JARVIS** é um sistema baseado em **Large Language Models (LLMs)** que atua como um **orquestrador central**.  
Ele recebe uma tarefa complexa, divide em subtarefas e as delega para **LLMs especializadas**, hospedadas na plataforma **Hugging Face**, consolidando os resultados em uma resposta final.

Por se tratar de um projeto **ativo, colaborativo e de código aberto**, o JARVIS é um excelente estudo de caso para análise de **fluxos de versionamento, integração contínua e releases**.

---

## 🎯 Objetivo da Atividade 2

O objetivo desta atividade foi **analisar como o projeto JARVIS gerencia sua configuração ao longo do tempo**, respondendo principalmente às seguintes questões:

- Qual **modelo de branching** é adotado? (GitHub Flow, Trunk-Based, Gitflow, etc.)
- Existe uma **estratégia formal de releases**?
- O projeto utiliza **versionamento semântico (SemVer)**?
- Qual o **nível de maturidade** do processo de desenvolvimento?
- Como a equipe lida com **integrações, merges e contribuições externas**?

Para isso, foram utilizadas **três abordagens complementares**:
1. **Análise via LLM (Hugging Face)**
2. **Análise Manual / Visual**
3. **Análise Estatística**

---

## 👥 Equipe

| Nº | Nome                                  | Matrícula       |
|----|--------------------------------------|-----------------|
| 01 | André Felipe de Santana Conceição    | 202300061527    |
| 02 | David Vieira Reis                    | 202100011299    |
| 03 | Adailton Moura da Silva              | 202100011154    |
| 04 | Enzo Emanuel Maia Costa              | 202300061901    |
| 05 | Rafael Souza Prata                   | 202300061750    |
| 06 | Vinicius Morais Souza                | 202200060106    |
| 07 | Felipe Ferreira da Silva             | 202100113360    |
| 08 | João Filipe de Araújo Santos Rezende | 202100011548    |

---

## 🗂️ Estrutura do Repositório

O repositório está organizado de acordo com os **tipos de análise realizados na Etapa 2**.

```text
📦 Engenharia_SoftwareII_2025-2_T04_JARVIS_Etapa02
│
├── 📂 Análise de logs e evidências via IA/
│   ├── 📂 André Felipe - 202300061527/
│   ├── 📂 David Vieira Reis - 202100011299/
│   ├── 📂 Rafael Souza Prata - 202300061750/
│   └── 📂 Vinicius Morais Souza - 202200060106/
│
├── 📂 Análise Manual/
│   ├── 📂 Adailton Moura da Silva - 202100011154/
│   ├── 📂 Enzo Emanuel - 202300061901/
│   └── 📂 Felipe Ferreira - 202100113360/


│
└── 📄 README.md
```
Cada pasta individual contém:

- Scripts utilizados para coleta de dados  
- Logs do Git (`git log`, `git branch`, `git tag`)  
- Prompts enviados às LLMs  
- Respostas das IAs  
- Evidências textuais e visuais  
- Análises e conclusões individuais  

---

## 🤖 Análise via LLM (Hugging Face)

A análise automatizada com IA teve como objetivo verificar se uma **LLM** consegue identificar corretamente:

- O **Branching Model**  
- A **Estratégia de Release**  
- Evidências técnicas no histórico do Git  

### 🔹 Modelos Utilizados

- **Qwen/Qwen2.5-72B-Instruct**  
- **Meta-Llama-3-8B-Instruct**  
- **DeepSeek-R1**  

### 🔹 Estratégia de Fornecimento de Dados

Foram utilizados:

- `git log --graph --oneline`  
- `git branch -r`  
- `git tag`  

Além disso, os dados foram consolidados em **arquivos `.txt`**, preparados especificamente para consumo por **LLMs**.

---

## 🔍 Análise Manual / Visual

A análise manual foi realizada diretamente:

- Pela interface do **GitHub**  
- Pelo histórico de commits  
- Pela estrutura de branches  
- Pela observação da frequência de merges e integrações  

Essa abordagem teve como objetivo **validar ou refutar** os resultados obtidos pelas análises via IA.

---

## 📊 Análise Estatística

A análise estatística teve como foco:

- Frequência de commits  
- Ausência ou presença de tags  
- Padrões de entrega contínua  
- Identificação de possíveis estratégias de release  
  (Continuous Delivery, Rapid Release, LTS)  

Essa análise complementa as abordagens anteriores, trazendo uma **visão quantitativa** do processo.

---

## 📌 Conclusão Geral

A partir das análises realizadas (IA, manual e estatística), foi possível concluir que o projeto **JARVIS**:

- Não adota versionamento semântico formal (**SemVer**)  
- Não utiliza **tags de release** no Git  
- Opera majoritariamente em um fluxo **GitHub Flow / Trunk-Based**  
- Realiza integrações frequentes diretamente na branch **`main`**  
- Possui um nível de maturidade **moderado**, com boas práticas de colaboração, porém com oportunidades claras de melhoria em **automação, versionamento e controle de releases**  

---

## ▶️ Como Executar as Análises por Modelo

Esta seção descreve, de forma objetiva, como cada modelo de IA foi utilizado durante a análise da gerência de configuração do projeto JARVIS.

---

### 🟣 Qwen/Qwen2.5-72B-Instruct

#### ✔️ Como Executar

Para a análise com o modelo **Qwen**, foi utilizada uma abordagem de **extração estruturada de dados**, automatizada por meio de um script em Python.

**Passos:**

1. Clone o repositório do projeto JARVIS localmente:
   ```bash
   git clone https://github.com/microsoft/JARVIS.git

Execute o script Python de extração de evidências (`script.py`), que coleta:

- Grafo de commits (`git log --graph --oneline`)
- Branches remotas (`git branch -r`)
- Tags (`git tag`)

  > 📌 **Localização do Script de Extração**

O arquivo `script.py`, responsável pela extração de logs e evidências do repositório, está localizado na seguinte estrutura de diretórios:

```text
📦 Engenharia_SoftwareII_2025-2_T04_JARVIS_Etapa02
│
├── 📂 Análise de logs e evidências via IA/
│   ├── 📂 André Felipe - 202300061527/
         ├── script.py 
```

O script gera automaticamente um arquivo consolidado:

- `log_para_ia.txt`

2. Acesse o **HuggingChat (Qwen)** na plataforma **Hugging Face**.

3. Cole o prompt de análise junto com o conteúdo do arquivo `log_para_ia.txt`.

4. Analise a resposta retornada pelo modelo, focando em:

- Branching Model
- Estratégia de Releases
- Evidências técnicas no histórico do Git

### 🟢 Meta-Llama-3-8B-Instruct

#### ✔️ Como Executar

1. Gere manualmente os arquivos de evidência a partir do repositório JARVIS:

```bash
git branch -a
git log --merges --oneline --all
git log main -n 50
```
2. Salve as saídas em arquivos .txt.

3. Acesse a página do modelo Meta-Llama-3-8B-Instruct no Hugging Face.

4. Na interface de inferência, cole:

O prompt estruturado

O conteúdo dos arquivos de evidência

5. Avalie o resultado com base nas evidências fornecidas, sem assumir informações não observáveis.

### 🔵 DeepSeek-R1

#### ✔️ Como Executar

1. Gere o histórico completo de commits:

```bash
git log > log.txt
```
2. Acesse o modelo DeepSeek-R1 no Hugging Face.

3. Envie o prompt técnico junto com o conteúdo completo do arquivo log.txt.

4. Solicite explicitamente que a análise seja baseada exclusivamente nas evidências observáveis.

5. Utilize a resposta para avaliar:

Estratégia de releases

Modelo de fluxo de trabalho

Grau de maturidade do processo

---

## 🔧 Infraestrutura (Ambiente de Execução)

As análises com LLM foram realizadas utilizando exclusivamente a infraestrutura das próprias plataformas de IA, acessadas via navegador, sem execução em ambientes de notebook ou *cloud compute* gerenciados pelo grupo.

---

### ☁️ Ambiente de Nuvem — Interface Nativa das LLMs

A execução ocorreu diretamente nas interfaces web das LLMs, que disponibilizam inferência imediata a partir da inserção de prompts.

**Infraestrutura adotada (padrão da plataforma):**

- **Plataforma:** Hugging Face / HuggingChat  
- **Execução:** Interface Web (Chat / Inference)  
- **Processamento:** Infraestrutura gerenciada pelo provedor da LLM  
- **GPU / CPU:** Gerenciada internamente pela plataforma  
- **RAM e Disco:** Não expostos ao usuário  
- **Configuração local:** Não necessária  

Esse ambiente foi utilizado para:

- Qwen/Qwen2.5-72B-Instruct  
- Meta-Llama-3-8B-Instruct  
- DeepSeek-R1  


## 📚 Relatório e Material Complementar

- 📄 **Relatório Completo (PDF – Etapa 2):**  
  [Acesse aqui](https://docs.google.com/document/d/1LzsOySSWbhy81r3u3X7ldHWZYF_D6ev-isXvMyRwxqQ/edit?pli=1&tab=t.0#heading=h.35j97j8nvhs5).

- 🎥 **Vídeo do Grupo:**  
  [Acesse aqui](https://drive.google.com/file/d/1nwgLRhP7H86so4XC7LhvmYyNlCcLmOYX/view?usp=drive_link).


