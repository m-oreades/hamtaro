import unittest
import hamtaro

hamtaro = hamtaro.Hamster(100,100,100)

class TestHamsterDeath(unittest.TestCase):
    
    def test_hunger(self):
        print("testing death by hunger")
        TestHamsterDeath.reset()
        hamtaro.hunger = 0
        hamtaro.update()
        result = hamtaro.alive
        self.assertFalse(result)

    def test_thirst(self):
        print("testing death by thirst")
        TestHamsterDeath.reset()
        hamtaro.thirst = 0
        hamtaro.update()
        result = hamtaro.alive
        self.assertFalse(result)

        
    def test_love(self):
        print("testing death by lack of love")
        TestHamsterDeath.reset()
        hamtaro.love = 0
        hamtaro.update()
        result = hamtaro.alive
        self.assertFalse(result)

        
    def test_kill(self):
        print("testing kill")
        TestHamsterDeath.reset()
        hamtaro.kill()
        hamtaro.update()
        result = hamtaro.alive
        self.assertFalse(result)


    def reset():
        hamtaro.hunger = 100
        hamtaro.thirst = 100
        hamtaro.love = 100
        hamtaro.alive = True
        hamtaro.euthanize = False


class TestHamsterRestore(unittest.TestCase):
    
    def test_hunger(self):
        print("testing restore hunger")
        TestHamsterRestore.reset()
        hamtaro.feed()
        hamtaro.update()
        result = hamtaro.hunger
        self.assertEqual(result, 100)
        print(hamtaro.hunger)

    def test_thirst(self):
        print("testing restore thirst")
        TestHamsterRestore.reset()
        hamtaro.water()
        hamtaro.update()
        result = hamtaro.thirst
        self.assertEqual(result, 100)
        print(hamtaro.thirst)

        
    def test_love(self):
        print("testing restore love")
        TestHamsterRestore.reset()
        hamtaro.care()
        hamtaro.update()
        result = hamtaro.love
        self.assertEqual(result, 100)
        print(hamtaro.love)


    def reset():
        hamtaro.hunger = 50
        hamtaro.thirst = 50
        hamtaro.love = 50
        hamtaro.alive = True
        hamtaro.euthanize = False


if __name__ == '__main__':
    unittest.main()
