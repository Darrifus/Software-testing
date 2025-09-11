import unittest
from fight import War1, War2, War, Warrior
import coverage

class TestGame(unittest.TestCase):

    def test_war1_pattern(self):

        # Каждый 4 удар этого воина должен быть 10, а не 20

        # Arrange
        w = War1('Max')
        # Act
        damage = [w.damage() for i in range(9)]
        # Assert
        self.assertEqual(damage,[20, 20, 20, 10, 20, 20, 20, 10, 20])

    def test_war2_pattern(self):

        # Каждый 3 удар этого воина должен быть 40, а не 20

        # Arrange
        w = War2('Peter')
        # Act
        damage = [w.damage() for i in range(7)]
        # Assert
        self.assertEqual(damage,[20, 20, 40, 20, 20, 40, 20])

    def test_health_is_not_negative(self):

        # Здоровье не должно быть меньше 0

        # Arrange
        w = Warrior('Peter')
        # Act
        w.set_health(-50)
        # Assert
        self.assertEqual(w.get_health(), 0)

    def test_health_is_reducing(self):

        # Здоровье должно уменьшаться при ударе

        # Arrange
        w1 = War1('Peter')
        w2 = War2('Max')
        war = War(w1,w2)
        start_health = w2.get_health()
        # Act
        war.hit(w1, w2)
        # Assert
        self.assertLess(w2.get_health(), start_health)

    def test_warrior_str(self):
        # __str__ должен возвращать имя и здоровье
        # Arrange
        w = Warrior("Max")
        # Act
        s = str(w)
        # Assert
        self.assertIn("Состояние бойца Max", s)
        self.assertIn("Здоворовье", s)

    def test_hit_until_death(self):
        # hit должен завершить бой, когда здоровье равно 0

        # Arrange
        w1 = War1("Max")
        w2 = War2("Peter")
        w2.set_health(5)
        war = War(w1, w2)
        # Act
        result = war.hit(w1, w2)
        # Assert
        self.assertFalse(result)


    def test_attack_person(self):
        # Бой должен кончиться смертью одного из бойцов

        # Arrange
        w1 = War1("Max")
        w2 = War2("Peter")
        # Act
        War(w1,w2).start_war()
        # Assert
        self.assertTrue(w1.get_health() <= 0 or w2.get_health() <= 0)


if __name__ == "__main__":

    cov = coverage.Coverage(source=["fight"])
    cov.start() 
    unittest.main(exit=False)
    cov.stop()
    cov.save()

    print("\nПокрытие кода:")
    cov.report(show_missing=True)





