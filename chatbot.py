
import re
import random

knowledge_base = {
    "greeting": {
        "patterns": ["halo", "hai", "selamat pagi", "selamat siang"],
        "responses": [
            "Halo! Selamat datang di Chatbot Informasi Kampus. Ada yang bisa saya bantu?"
        ]
    },
    "jadwal_kuliah": {
        "patterns": ["jadwal kuliah", "jadwal kelas", "kapan kuliah"],
        "responses": [
            "Jadwal kuliah dapat dilihat melalui portal akademik pada menu Jadwal Kuliah."
        ]
    },
    "lokasi_kampus": {
        "patterns": ["lokasi kampus", "alamat kampus", "dimana kampus"],
        "responses": [
            "Informasi lokasi kampus dapat dilihat melalui website resmi universitas."
        ]
    },
    "kontak_admin": {
        "patterns": ["kontak admin", "hubungi admin", "nomor admin"],
        "responses": [
            "Untuk menghubungi admin akademik, silakan melihat informasi kontak di portal resmi kampus."
        ]
    },
    "terima_kasih": {
        "patterns": ["terima kasih", "makasih", "thanks"],
        "responses": [
            "Sama-sama! Senang bisa membantu."
        ]
    },
    "goodbye": {
        "patterns": ["bye", "sampai jumpa", "keluar", "exit"],
        "responses": [
            "Sampai jumpa! Semoga harimu menyenangkan."
        ]
    }
}

FALLBACK_RESPONSE = (
    "Maaf, saya belum memahami pertanyaan Anda. "
    "Silakan coba gunakan kalimat atau kata kunci lain."
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
    print("CHATBOT INFORMASI KAMPUS".center(50))
    print("=" * 50)
    print("Bot : Halo! Ada yang bisa saya bantu?")
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
