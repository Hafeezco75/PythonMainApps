import unittest

from queues import MyQueue

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.q1 = MyQueue()
        self.q1.add_to_queue("Microsoft Africa")
        self.q1.add_to_queue("Trilogy Software Corporation")
        self.q1.add_to_queue("Grazac Nigeria")
        self.q1.add_to_queue("Open AI source company")
        self.q1.add_to_queue("Parenthesis")

    def test_queue_can_add_elements(self):
        self.assertEqual(len(self.q1.queue),5)  # add assertion here

    def test_queue_can_remove_elements(self):
        self.assertEqual(self.q1.queue[3], "Open AI source company")

    def test_queue_can_remove_all_elements(self):
        self.assertEqual(self.q1.queue[0], "Microsoft Africa")
        self.assertEqual(self.q1.queue[1], "Trilogy Software Corporation")
        self.assertEqual(self.q1.queue[2], "Grazac Nigeria")
        self.assertEqual(self.q1.queue[3], "Open AI source company")
        self.assertEqual(self.q1.queue[4], "Parenthesis")

    def test_queue_can_get_elements(self):
        self.assertEqual(self.q1.queue,["Microsoft Africa", "Trilogy Software Corporation", "Grazac Nigeria", "Open AI source company", "Parenthesis"])

    def test_queue_can_return_elements(self):
        self.assertEqual(self.q1.queue[1:3], ["Trilogy Software Corporation", "Grazac Nigeria"])
        self.assertEqual(self.q1.queue[2:], ["Grazac Nigeria", "Open AI source company", "Parenthesis"])


if __name__ == '__main__':
    unittest.main()
