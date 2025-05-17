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
        prompt: A mensagem do utilizador.
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

