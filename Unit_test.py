from main import getwiki
from unittest import TestCase


class TestProjectBot(TestCase):
    def test_getwiki(self) -> None:
        """This test checks whether input from a user equals output from API"""

        cases = [
            ("Вы́хухоль, или русская выхухоль, или хоху́ля (лат. Desmana moschata),"
             " — вид млекопитающих отряда насекомоядных из трибы Desmanini подсемейства Talpinae семейства кротовых. "
             "Один из двух видов трибы; вторым видом является пиренейская выхухоль (Galemys pyrenaicus)."
             , "Выхухоль"),
            ("В энциклопедии нет информации об этом", "Дом")
            # .... чем больше кортежей, тем лучше
        ]

        for k, v in cases:
            with self.subTest(k):
                self.assertEqual(k, getwiki(v))
