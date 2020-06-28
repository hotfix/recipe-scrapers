from ._abstract import AbstractScraper


class FoodAndWine(AbstractScraper):

    @classmethod
    def host(self):
        return 'foodandwine.com'
