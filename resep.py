
import re
import random

knowledge_base = {
    "greeting": {
        "patterns": ["halo", "hai", "selamat pagi", "selamat siang"],
        "responses": [
            "Halo! Selamat datang di Chatbot Resep Masakan. Sebutkan bahan makanan yang kamu miliki, seperti telur, tempe, nasi, kentang, atau bayam."
        ]
    },
    "resep_telur": {
        "patterns": ["telur", "resep telur", "omelet"],
        "responses": [
            "Telur dadar: kocok telur dengan sedikit garam, lalu masak di wajan hingga matang."
        ]
    },
    "resep_tempe": {
        "patterns": ["tempe", "resep tempe"],
        "responses": [
            "Tempe tumis: potong tempe, tumis dengan bawang dan sedikit kecap hingga matang."
        ]
    },
    "resep_nasi": {
        "patterns": ["nasi", "nasi goreng"],
        "responses": [
            "Nasi goreng: tumis bawang, masukkan nasi dan kecap, kemudian aduk hingga panas merata."
        ]
    },
    "resep_kentang": {
        "patterns": ["kentang", "resep kentang"],
        "responses": [
            "Kentang rebus: potong kentang, rebus hingga empuk, lalu sajikan dengan bumbu sesuai selera."
        ]
    },
    "resep_sayur": {
        "patterns": ["bayam", "sayur", "wortel"],
        "responses": [
            "Sayur bening: rebus air, tambahkan irisan wortel dan bayam, lalu masak hingga matang."
        ]
    },
    "terima_kasih": {
        "patterns": ["terima kasih", "makasih", "thanks"],
        "responses": [
            "Sama-sama! Selamat mencoba resepnya."
        ]
    },
    "goodbye": {
        "patterns": ["keluar", "sampai jumpa", "bye", "exit"],
        "responses": [
            "Terima kasih sudah menggunakan Chatbot Resep Masakan. Sampai jumpa!"
        ]
    }
}

FALLBACK_RESPONSE = (
    "Maaf, saya belum menemukan resep yang sesuai. "
    "Silakan coba masukkan bahan seperti telur, tempe, nasi, kentang, atau bayam."
)


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join(text.split())
    return text


def match_intent(user_input):
    processed = preprocess(user_input)

    for intent, data in knowledge_base.items():
        for pattern in data["patterns"]:
            pola = preprocess(pattern)

            if f" {pola} " in f" {processed} ":
                return intent

    return None


def generate_response(intent):
    if intent is None:
        return FALLBACK_RESPONSE

    responses = knowledge_base[intent]["responses"]
    return random.choice(responses)


def get_response(user_input):
    intent = match_intent(user_input)
    return generate_response(intent)


def run_chatbot():
    print("=" * 50)
    print("CHATBOT RESEP MASAKAN".center(50))
    print("=" * 50)
    print("Bot : Halo! Selamat datang di Chatbot Resep Masakan.")
    print("Bot : Sebutkan bahan makanan yang kamu miliki.")
    print("Bot : Ketik 'keluar' untuk mengakhiri percakapan.\n")

    while True:
        user_input = input("Anda: ").strip()

        if not user_input:
            print("Bot : Silakan masukkan pertanyaan Anda.\n")
            continue

        intent = match_intent(user_input)
        response = generate_response(intent)

        print("Bot :", response)
        print()

        if intent == "goodbye":
            break


if __name__ == "__main__":
    run_chatbot()
