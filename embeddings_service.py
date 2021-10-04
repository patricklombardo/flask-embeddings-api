import tensorflow_hub as hub


class EmbeddingsService:
    def __init__(self, remote=False):
        self.__remote = remote
        self.__ready = False
        self.__embed = None

    def load_embed_service(self):
        if self.__remote:
            self.__embed = hub.load(
                "https://tfhub.dev/google/universal-sentence-encoder/4"
            )
            self.__ready = True
        else:
            self.__embed = hub.load("./universal-sentence-encoder_4")
            self.__ready = True
        return self.__ready

    def get_status(self):
        return self.__ready

    def generate_embeddings(self, sentences: list):
        if self.__ready:
            embeddings = self.__embed(sentences)
            embeddings_list = embeddings.numpy().tolist()
            return embeddings_list
        else:
            return 503
