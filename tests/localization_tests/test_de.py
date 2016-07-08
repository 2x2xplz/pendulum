# -*- coding: utf-8 -*-

from pendulum import Pendulum

from .. import AbstractTestCase
from . import AbstractLocalizationTestCase



class DeTest(AbstractLocalizationTestCase, AbstractTestCase):

    locale = 'de'

    def diff_for_humans(self):
        with self.wrap_with_test_now():
            d = Pendulum.now().sub(seconds=1)
            self.assertEqual('vor 1 Sekunde', d.diff_for_humans())

            d = Pendulum.now().sub(seconds=2)
            self.assertEqual('vor 2 Sekunden', d.diff_for_humans())

            d = Pendulum.now().sub(minutes=1)
            self.assertEqual('vor 1 Minute', d.diff_for_humans())

            d = Pendulum.now().sub(minutes=2)
            self.assertEqual('vor 2 Minuten', d.diff_for_humans())

            d = Pendulum.now().sub(hours=1)
            self.assertEqual('vor 1 Stunde', d.diff_for_humans())

            d = Pendulum.now().sub(hours=2)
            self.assertEqual('vor 2 Stunden', d.diff_for_humans())

            d = Pendulum.now().sub(days=1)
            self.assertEqual('vor 1 Tag', d.diff_for_humans())

            d = Pendulum.now().sub(days=2)
            self.assertEqual('vor 2 Tagen', d.diff_for_humans())

            d = Pendulum.now().sub(weeks=1)
            self.assertEqual('vor 1 Woche', d.diff_for_humans())

            d = Pendulum.now().sub(weeks=2)
            self.assertEqual('vor 2 Wochen', d.diff_for_humans())

            d = Pendulum.now().sub(months=1)
            self.assertEqual('vor 1 Monat', d.diff_for_humans())

            d = Pendulum.now().sub(months=2)
            self.assertEqual('vor 2 Monaten', d.diff_for_humans())

            d = Pendulum.now().sub(years=1)
            self.assertEqual('vor 1 Jahr', d.diff_for_humans())

            d = Pendulum.now().sub(years=2)
            self.assertEqual('vor 2 Jahren', d.diff_for_humans())

            d = Pendulum.now().add(seconds=1)
            self.assertEqual('in 1 Sekunde', d.diff_for_humans())

            d = Pendulum.now().add(seconds=1)
            d2 = Pendulum.now()
            self.assertEqual('1 Sekunde später', d.diff_for_humans(d2))
            self.assertEqual('1 Sekunde zuvor', d2.diff_for_humans(d))

            self.assertEqual('1 Sekunde', d.diff_for_humans(d2, True))
            self.assertEqual('2 Sekunden', d2.diff_for_humans(d.add(seconds=1), True))
