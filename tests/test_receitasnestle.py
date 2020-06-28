from tests import ScraperTest
from recipe_scrapers.receitasnestle import Receitasnestle

class TestReceitasnestleScraper(ScraperTest):

    scraper_class = Receitasnestle

    def test_host(self):
        self.assertEqual(
            'receitasnestle.com.br',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Pé-de-moleque'
        )

    def test_yields(self):
        self.assertEqual("30 docinhos", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            'https://www.receitasnestle.com.br/images/default-source/recipes/p&#233;-de-moleque-alta.jpg?sfvrsn=5bcf78fc_0',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 xícara (chá) de açúcar',
                '1 xícara (chá) de amendoim sem pele torrado',
                '1  Leite MOÇA® (lata ou caixinha) 395g'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Em uma panela, misture o a&#231;&#250;car e o amendoim e leve ao fogo baixo, mexendo sempre at&#233; o a&#231;&#250;car caramelizar, sem deixar escurecer.\nAdicione o Leite MO&#199;A em fio e mexa com colher de cabo longo, por cerca de 15 minutos ou at&#233; a massa se desprender do fundo da panela.\nUnte uma superf&#237;cie lisa de m&#225;rmore ou assadeira com manteiga, despeje a mistura e nivele com a ajuda de uma esp&#225;tula ou rolo de massa.\nDeixe esfriar e corte em losangos.',
            self.harvester_class.instructions()
        )
