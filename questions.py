import streamlit as st
import pandas as pd
import os

# Título da página
st.title("Banco de Questões")

# Exibir logo
st.sidebar.image("logo.png", use_column_width=True)

# Nome do aluno na barra lateral
st.sidebar.title("Informações do Aluno")
nome = st.sidebar.text_input("Digite seu nome:")

# Disciplinas
disciplinas = {
    "Pensamento Computacional": [
        {
            "pergunta": "Qual é a primeira etapa do pensamento computacional? (Ordem adotada pelo professor)",
            "opcoes": ["Abstração", "Decomposição", "Reconhecimento de padrões", "Algoritmos"],
            "resposta_correta": "Abstração"
        },
        {
            "pergunta": "Qual é a segunda etapa do pensamento computacional? (Ordem adotada pelo professor)",
            "opcoes": ["Abstração", "Decomposição", "Reconhecimento de padrões", "Algoritmos"],
            "resposta_correta": "Decomposição"
        },
        {
            "pergunta": "Qual é a terceira etapa do pensamento computacional? (Ordem adotada pelo professor)",
            "opcoes": ["Abstração", "Decomposição", "Reconhecimento de padrões", "Algoritmos"],
            "resposta_correta": "Reconhecimento de padrões"
        },
        {
            "pergunta": "Qual é a quarta etapa do pensamento computacional? (Ordem adotada pelo professor)",
            "opcoes": ["Abstração", "Decomposição", "Reconhecimento de padrões", "Algoritmos"],
            "resposta_correta": "Algoritmos"
        }
    ],
    "Sistemas Operacionais": [
        {
            "pergunta": "Qual é a função principal de um sistema operacional?",
            "opcoes": ["Gerenciar hardware", "Executar aplicativos", "Proteger dados", "Conectar à internet"],
            "resposta_correta": "Gerenciar hardware"
        },
        {
            "pergunta": "Qual é um exemplo de sistema operacional?",
            "opcoes": ["Microsoft Word", "Linux", "Google Chrome", "Python"],
            "resposta_correta": "Linux"
        },
        {
            "pergunta": "Qual sistema operacional é conhecido por sua interface gráfica de usuário?",
            "opcoes": ["MS-DOS", "Windows", "Linux", "Unix"],
            "resposta_correta": "Windows"
        },
        {
            "pergunta": "Qual sistema operacional é amplamente utilizado em servidores?",
            "opcoes": ["Windows", "macOS", "Linux", "Android"],
            "resposta_correta": "Linux"
        }
    ],
    "Lógica de Programação": [
        {
            "pergunta": "O que é um loop?",
            "opcoes": ["Uma estrutura de decisão", "Uma estrutura de repetição", "Uma variável", "Um tipo de dado"],
            "resposta_correta": "Uma estrutura de repetição"
        },
        {
            "pergunta": "Qual é a estrutura de decisão mais comum em programação?",
            "opcoes": ["Loop", "If-Else", "Variável", "Função"],
            "resposta_correta": "If-Else"
        },
        {
            "pergunta": "O que é uma variável?",
            "opcoes": ["Um tipo de dado", "Uma estrutura de repetição", "Um espaço na memória para armazenar valores", "Uma função"],
            "resposta_correta": "Um espaço na memória para armazenar valores"
        },
        {
            "pergunta": "O que é uma função?",
            "opcoes": ["Um tipo de dado", "Uma estrutura de repetição", "Um espaço na memória", "Um bloco de código que realiza uma tarefa específica"],
            "resposta_correta": "Um bloco de código que realiza uma tarefa específica"
        }
    ],
    "Organização e Arquitetura de Computadores": [
        {
            "pergunta": "O que é a unidade central de processamento (CPU)?",
            "opcoes": ["Memória", "Processador", "Disco rígido", "Placa-mãe"],
            "resposta_correta": "Processador"
        },
        {
            "pergunta": "Qual é a função da memória RAM?",
            "opcoes": ["Armazenar dados permanentemente", "Executar programas", "Armazenar dados temporariamente", "Conectar dispositivos"],
            "resposta_correta": "Armazenar dados temporariamente"
        },
        {
            "pergunta": "O que é um disco rígido?",
            "opcoes": ["Memória volátil", "Processador", "Armazenamento permanente", "Placa-mãe"],
            "resposta_correta": "Armazenamento permanente"
        },
        {
            "pergunta": "Qual componente é responsável por conectar todos os outros componentes do computador?",
            "opcoes": ["Memória", "Processador", "Disco rígido", "Placa-mãe"],
            "resposta_correta": "Placa-mãe"
        }
    ]
}

# Seleção de disciplina na barra lateral
st.sidebar.title("Disciplinas")
disciplina_selecionada = st.sidebar.selectbox("Escolha uma disciplina:", list(disciplinas.keys()))

# Adicionar o nome do professor abaixo das disciplinas
st.sidebar.markdown("### By Prof. Maurilio Benevento")

# Dicionário para armazenar as respostas dos alunos
respostas = {}

# Exibir perguntas da disciplina selecionada
if disciplina_selecionada:
    perguntas = disciplinas[disciplina_selecionada]
    with st.expander("Clique para ver as perguntas"):
        for i, pergunta in enumerate(perguntas):
            st.write(f"**{i+1}. {pergunta['pergunta']}**")
            resposta = st.radio(f"Escolha uma opção para a pergunta {i+1}:", pergunta["opcoes"], key=f"pergunta_{i}")
            respostas[f"pergunta_{i}"] = resposta

# Função para registrar as respostas no arquivo CSV
def registrar_respostas(nome, disciplina, respostas, perguntas):
    file_path = "respostas.csv"
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        df = pd.DataFrame(columns=["Nome", "Disciplina", "Pergunta", "Resposta", "Correta"])
    else:
        df = pd.read_csv(file_path)

    novas_respostas = []
    for i, pergunta in enumerate(perguntas):
        correta = respostas[f"pergunta_{i}"] == pergunta["resposta_correta"]
        novas_respostas.append({
            "Nome": nome,
            "Disciplina": disciplina,
            "Pergunta": pergunta["pergunta"],
            "Resposta": respostas[f"pergunta_{i}"],
            "Correta": correta
        })

    df = pd.concat([df, pd.DataFrame(novas_respostas)], ignore_index=True)
    df.to_csv(file_path, index=False)

# Botão para enviar respostas
if st.button("Enviar Respostas"):
    if nome:
        registrar_respostas(nome, disciplina_selecionada, respostas, perguntas)
        st.write(f"Obrigado, {nome}! Aqui estão suas respostas para a disciplina {disciplina_selecionada}:")
        score = 0
        for i, pergunta in enumerate(perguntas):
            st.write(f"**{i+1}. {pergunta['pergunta']}**")
            st.write(f"Sua resposta: {respostas[f'pergunta_{i}']}")
            if respostas[f'pergunta_{i}'] == pergunta["resposta_correta"]:
                st.write("Resposta correta! ✅")
                score += 1
            else:
                st.write(f"Resposta incorreta. A resposta correta é: {pergunta['resposta_correta']} ❌")
        
        # Mostrar o score final na barra lateral direita
        st.sidebar.title("Score Final")
        st.sidebar.write(f"{nome}, seu score final é: {score}/{len(perguntas)}")
    else:
        st.warning("Por favor, digite seu nome antes de enviar as respostas.")