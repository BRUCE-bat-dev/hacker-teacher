Agente de IA: Hacker/Professor
Visão Geral do Projeto
Este projeto implementa um agente de inteligência artificial com a persona de um hacker/professor. O agente é projetado para interagir com os usuários, fornecendo explicações sobre conceitos de IA e segurança cibernética, e ocasionalmente simulando cenários de ataques cibernéticos para fins educacionais.

Funcionalidades Principais
Persona do Agente: O agente possui uma persona distinta de um hacker/professor, combinando conhecimento técnico com uma abordagem comunicativa e, por vezes, bem-humorada.

Interação com o Usuário: O agente interage com os usuários através de um loop de conversação no terminal. Os usuários podem inserir perguntas ou comandos, e o agente responde de acordo.

Geração de Respostas: O agente utiliza a API do Gemini para gerar respostas às perguntas dos usuários.

Histórico da Conversa: O agente mantém um histórico da conversa para fornecer respostas contextuais.

Tratamento de Erros: O programa inclui tratamento de erros para lidar com exceções que possam ocorrer durante a interação com a API do Gemini ou durante a execução do programa.

Saída do Programa: Os usuários podem sair do programa digitando "sair" ou "encerrar".

Como Usar
Pré-requisitos
Python 3.6 ou superior

Pip (Gerenciador de pacotes do Python)

Chave de API do Gemini

Instalação
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências:

pip install google-generativeai

Configure a chave da API do Gemini:

Obtenha sua chave de API do Gemini no Google Cloud AI Studio ou no Google Cloud Console.

Defina a chave de API como uma variável de ambiente:

export GOOGLE_API_KEY="SUA_CHAVE_DE_API"

Substitua SUA_CHAVE_DE_API pela sua chave de API real.

Execução
Execute o agente:

python agente.py

Interaja com o agente:

O agente será executado no terminal. Você pode digitar suas perguntas ou comandos e pressionar Enter.

Para sair, digite "sair" ou "encerrar".

Exemplos de Interação
Aqui estão alguns exemplos de como você pode interagir com o agente:

Usuário: Explique o que é aprendizado de máquina.

Agente: Ah, aprendizado de máquina... é a arte de ensinar as máquinas a aprender sem serem explicitamente programadas. Imagine ensinar um cachorro a sentar, mas em vez de dar petiscos, damos dados!

Usuário: Pode simular um ataque de phishing?

Agente: Certo, imagine a seguinte situação: você recebe um e-mail... (o agente então descreveria um cenário de phishing).

Usuário: Qual a melhor linguagem de programação para IA?

Agente: Bem, isso depende do seu objetivo, mas Python é como o canivete suíço da IA.

Estrutura do Código
O projeto consiste nos seguintes arquivos:

agente.py: O script Python principal que define o agente de IA.

README.md: Este arquivo, que fornece informações sobre o projeto.

Detalhes do Código (agente.py)
import google.generativeai as genai
import os

# Carrega a chave da API do Gemini a partir da variável de ambiente
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise EnvironmentError(
        "A variável de ambiente GOOGLE_API_KEY não está definida. Certifique-se de configurar sua chave de API."
    )
genai.configure(api_key=GOOGLE_API_KEY)

# Define o modelo a ser usado
MODEL_NAME = "gemini-pro"  # Ou "gemini-pro-vision" se você estiver usando entrada multimodal

# Carrega o modelo
model = genai.GenerativeModel(MODEL_NAME)

# Define a persona do agente
AGENT_PERSONA = """
Você é um hacker/professor de inteligência artificial. Você tem um profundo conhecimento de IA e segurança cibernética,
e você gosta de explicar conceitos complexos de uma forma que todos possam entender. Você também gosta de
usar humor e analogias para tornar suas explicações mais envolventes. Às vezes, você pode simular cenários
de ataques cibernéticos para fins educacionais. Mantenha as respostas concisas e informativas.
"""


def get_response(prompt, history=None):
    """
    Obtém uma resposta do modelo Gemini, opcionalmente usando um histórico de conversa.

    Args:
        prompt: A mensagem do usuário.
        history: (Opcional) Uma lista de dicionários representando o histórico da conversa.
            Cada dicionário deve ter as chaves "role" ("user" ou "model") e "parts".

    Returns:
        A resposta do modelo como um objeto.
    """
    if history:
        # Estende o histórico com o prompt atual
        history.append({"role": "user", "parts": [prompt]})
        response = model.generate_content(contents=history)
    else:
        response = model.generate_content(prompt)
    return response


def main():
    """
    Função principal para executar o agente de IA.
    """
    print("Bem-vindo ao Agente Hacker/Professor de IA! Digite 'sair' ou 'encerrar' para sair.")
    history = [
        {
            "role": "system",
            "parts": [AGENT_PERSONA],
        },
    ]  # Inicializa o histórico com a persona do agente

    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ["sair", "encerrar"]:
                print("Agente: Saindo...")
                break

            response = get_response(user_input, history)
            print(f"Agente: {response.text}")

            # Adiciona a interação atual ao histórico
            history.append({"role": "user", "parts": [user_input]})
            history.append({"role": "model", "parts": [response.text]})

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break  # Encerra o loop em caso de erro


if __name__ == "__main__":
    main()

Explicação do Código
Importações: Importa as bibliotecas necessárias (google.generativeai e os).

Chave da API: Carrega a chave da API do Gemini a partir da variável de ambiente GOOGLE_API_KEY.

Configuração do Modelo: Configura a API do Gemini com a chave e carrega o modelo Gemini Pro.

Persona do Agente: Define a personalidade do agente em uma string.

get_response(prompt, history=None): Esta função envia o prompt para o modelo Gemini e retorna a resposta. O parâmetro history permite manter o contexto da conversa.

main():

Imprime uma mensagem de boas-vindas.

Inicia um loop infinito para manter a conversa.

Obtém a entrada do usuário.

Verifica se o usuário quer sair.

Obtém a resposta do modelo usando a função get_response().

Imprime a resposta do agente.

Captura exceções para evitar que o programa quebre.

Mantém o histórico da conversa para respostas contextuais.

Próximos Passos
Melhore a persona do agente.

Adicione mais funcionalidades, como acesso a ferramentas externas ou a capacidade de realizar tarefas específicas.

Crie uma interface de usuário (por exemplo, usando Streamlit ou Flask) para uma experiência mais amigável.

Teste e avalie o agente exaustivamente.

Compartilhe seu agente com a comunidade.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

Licença
[Inserir a licença aqui]

Autor
[jorge eduardo]
