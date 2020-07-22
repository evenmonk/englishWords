from django.test import TestCase

class LevelTestCase(TestCase):
    def setUp(self):
        self.objects.create(name="Intermidiate", code="B1")
        self.objects.create(name="Advanced", code="C1")
