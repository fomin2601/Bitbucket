import unittest
import os


class EnvVarTest(unittest.TestCase):
    def test_bot_token(self):
        self.assertIsNotNone(os.getenv('BOT_TOKEN'))

    def test_images_path(self):
        self.assertIsNotNone(os.getenv('IMAGES_PATH'))

    def test_phrases_path(self):
        self.assertIsNotNone(os.getenv('PHRASES'))

    def test_channel_to_repost(self):
        self.assertIsNotNone(os.getenv('CHANNEL_TO_REPOST'))


class FileExistingTest(unittest.TestCase):
    def test_font_file(self):
        self.assertTrue(os.path.isfile('Lobster-Regular.ttf'))

    def test_phrases_file(self):
        self.assertTrue(os.path.isfile(os.getenv('PHRASES')))

    def test_requirements_file(self):
        self.assertTrue(os.path.isfile('requirements.txt'))

    def test_images_dir(self):
        self.assertTrue(os.path.isdir(os.getenv('IMAGES_PATH')))


if __name__ == '__main__':
    unittest.main()
