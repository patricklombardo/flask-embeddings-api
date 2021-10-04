import tensorflow_hub as hub


class EmbeddingsService:
    def __init__(self, library_override=None):
        """[summary]

        Args:
            library_override ([str], optional): Override default location for universal-sentence-encoder (i.e. point to local installation) Defaults to None.
        """
        self.__library_override = library_override
        self.__ready = False
        self.__embed = None

    def load_embed_service(self):
        if self.__library_override:
            self.__embed = hub.load(self.__library_override)
            self.__ready = True
        else:
            self.__embed = hub.load(
                "https://tfhub.dev/google/universal-sentence-encoder/4"
            )
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
