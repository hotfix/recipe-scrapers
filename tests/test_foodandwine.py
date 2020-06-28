from tests import ScraperTest

from recipe_scrapers.foodandwine import FoodAndWine


class TestFoodAndWineScraper(ScraperTest):

    scraper_class = FoodAndWine

    def test_host(self):
        self.assertEqual(
            'foodandwine.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Balsamic and Rosemary-Marinated Florentine Steak'
        )

    def test_yields(self):
        self.assertEqual("Serves : 4 to 6", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fcdn-image.foodandwine.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_-_1200x900%2Fpublic%2F200903-r-xl-balsamic-and-rosemary-marinated-florentine-steak.jpg%3Fitok%3DwjSJ1fA-',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 cup balsamic vinegar',
                '1/2 cup plus 2 tablespoons extra-virgin olive oil',
                '1/4 cup finely chopped rosemary',
                'One 3-pound porterhouse steak, about 4 inches thick',
                '2 teaspoons kosher salt',
                '2 teaspoons coarsely ground pepper'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'In a sturdy resealable plastic bag, combine the vinegar with 1/2 cup of the olive oil and the rosemary. Add the steak, seal the bag and refrigerate overnight, turning the bag several times. Preheat the oven to 425Â° and bring the steak to room temperature. Heat a grill pan. Remove the steak from the marinade and season with the salt and pepper. Rub the side with the remaining 2 tablespoons of olive oil. Grill over moderately high heat until nicely charred on the top and bottom, about 5 minutes per side. Transfer the steak to a rimmed baking sheet and roast for about 30 minutes, until an instant-read thermometer inserted into the tenderloin (the smaller section) registers 125Â°. Alternatively, build a fire on one side of a charcoal grill or light a gas grill. Grill the steak over moderate heat for 5 minutes on each side. Transfer the steak to the cool side of the grill, close the lid and cook for 30 minutes longer. Transfer the steak to a carving board and let rest for 10 minutes. Slice the steak across the grain and serve immediately.',
            self.harvester_class.instructions()
        )
