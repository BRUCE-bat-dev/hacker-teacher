import google.generativeai as genai
import os

# Sua chave de API do Gemini
GOOGLE_API_KEY = "AIzaSyAMw_HllFnm_loNHHlLcpR06ExBGzglUrE"

# Configure a chave de API
genai.configure(api_key=GOOGLE_API_KEY)

# Define o modelo a ser usado
MODEL_NAME = "gemini-pro"  # Ou "gemini-pro-vision" se estiver a usar entrada multimodal

# Carrega o modelo
model = genai.GenerativeModel(MODEL_NAME)

# Define a persona do agente
AGENT_PERSONA = """
Você é um hacker/professor de inteligência artificial. Você tem um profundo conhecimento de IA e segurança cibernética,
e você gosta de explicar conceitos complexos de uma forma que todos possam entender. Você também gosta de
usar humor e analogias para tornar as suas explicações mais envolventes. Por vezes, você pode simular cenários
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

