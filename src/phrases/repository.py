import csv


class PhrasesRepository:
    def __init__(self):
        self.__phrases = self.__load_phrases()

    def __load_phrases(self):
        with open("src/phrases/data.csv", "r") as file:
            data = file.readlines()

        data = [
            line
            for line in csv.reader(
                data,
                quotechar='"',
                delimiter=",",
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
        ]

        return [dict(zip(data[0], row)) for row in data[1:]]

    def get_all(self):
        return self.__phrases

    def get_all_authors(self):
        authors = []
        for phrase in self.__phrases:
            authors = [*authors, *phrase["author"].split(",")]

        return sorted(set(authors))

    def get_author_phrases(self, author: str):
        return [p["phrase"] for p in self.__phrases if p["author"] == author]
