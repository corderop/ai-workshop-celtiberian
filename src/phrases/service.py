class PhrasesService:
    def __get_readable_author(self, authors):
        authors_list = authors.split(",")

        if len(authors_list) == 1:
            return authors_list[0]
        else:
            authors_str = ", ".join(authors_list[:-1])
            authors_str += f" y {authors_list[-1]}"
            return authors_str

    def get_readable_phrases(self, phrases):
        return [
            f'"{p["phrase"]}" por {self.__get_readable_author(p["author"])}'
            for p in phrases
        ]
