from ._abstract import AbstractScraper


class Receitasnestle(AbstractScraper):

    @classmethod
    def host(self):
        return 'receitasnestle.com.br'
