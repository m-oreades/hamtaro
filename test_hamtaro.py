import unittest
import json
from hamtaro import Hamster as Hamster

#test hamster death causes
class TestHamsterDeath(unittest.TestCase):
    # setup
    def setUp(self):
        self.hamster = Hamster(100,100,100)

    # hunger
    def test_hunger(self):
        self.hamster.hunger = 0
        self.hamster.update()
        result = self.hamster.alive
        self.assertFalse(result)

    # thirst
    def test_thirst(self):
        self.hamster.thirst = 0
        self.hamster.update()
        result = self.hamster.alive
        self.assertFalse(result)

    # love
    def test_love(self):
        self.hamster.love = 0
        self.hamster.update()
        result = self.hamster.alive
        self.assertFalse(result)

    # kill
    def test_kill(self):
        self.hamster.kill()
        self.hamster.update()
        result = self.hamster.alive
        self.assertFalse(result)

# test hamster attribute increase
class TestHamsterRestore(unittest.TestCase):
    # setup
    def setUp(self):
        self.hamster = Hamster(50,50,50)

    # hunger
    def test_hunger(self):
        self.hamster.feed()
        self.hamster.update()
        result = self.hamster.hunger
        self.assertEqual(result, 100)

    # thirst
    def test_thirst(self):
        self.hamster.water()
        self.hamster.update()
        result = self.hamster.thirst
        self.assertEqual(result, 100)

    # love-kiss
    def test_love_kiss(self):
        self.hamster.care("kiss")
        self.hamster.update()
        result = self.hamster.love
        self.assertEqual(result, 100)
        
    # love-cuddle
    def test_love_cuddle(self):
        self.hamster.care("cuddle")
        self.hamster.update()
        result = self.hamster.love
        self.assertEqual(result, 100)

# test hamster attribute increase won't surpass 100
class TestHamsterRestoreFull(unittest.TestCase):
    # setup
    def setUp(self):
        self.hamster = Hamster(100,100,100)

    # hunger
    def test_full_hunger(self):
        self.hamster.feed()
        self.hamster.update()
        result = self.hamster.hunger
        self.assertEqual(result, 100)

    # thirst
    def test_full_thirst(self):
        self.hamster.water()
        self.hamster.update()
        result = self.hamster.thirst
        self.assertEqual(result, 100)

    # love-kiss
    def test_full_love_kiss(self):
        self.hamster.care("kiss")
        self.hamster.update()
        result = self.hamster.love
        self.assertEqual(result, 100)
        
    # love-cuddle
    def test_full_love_cuddle(self):
        self.hamster.care("cuddle")
        self.hamster.update()
        result = self.hamster.love
        self.assertEqual(result, 100)

class TestTimePass(unittest.TestCase):
    #setup
    def setUp(self):
        self.hamster = Hamster()

    def test_time_pass(self):
        self.hamster.last_checked += 1
        result = self.hamster.last_checked - self.hamster.birthday
        self.assertEqual(result, 1)
        
    def test_time_death(self):
        self.hamster.last_checked -= 100
        self.hamster.update()
        result = self.hamster.alive
        self.assertFalse(result)

# test json load/save
class TestJsonLoadSave(unittest.TestCase):
    # setup
    def setUp(self):
        #set json file to an empty dict
        with open('data.json', 'w') as f:
            json.dump({}, f)

        self.hamster = Hamster()
    
    # write to json
    def test_write_to_json(self):
        self.hamster.update()
        with open('data.json') as f:
            result = json.load(f)
        self.assertEqual(result,vars(self.hamster))

    # erase
    def test_erase(self):
        self.hamster.update()
        self.hamster.kill()
        with open('data.json') as f:
            result = json.load(f)
        self.assertEqual(result, {})

# zero limit
class TestZeroLimit(unittest.TestCase):
    
    def test_zero_limit(self):
        self.hamster = Hamster()
        result = self.hamster.zero_limit(-40)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
