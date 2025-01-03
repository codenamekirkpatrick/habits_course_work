from django.test import TestCase
from django.utils import timezone

from habits.models import Habit
from users.models import User


class HabitModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name='test1', email='test1@mail.com', password='test1')

    def test_create_habit(self):
        habit = Habit.objects.create(
            autor=self.user,
            title='Habit Test',
            place='Home',
            duration=30,
            time_action=timezone.now().time(),
            action='Do something',
            is_pleasant=False
        )
        self.assertEqual(habit.title, 'Habit Test')
        self.assertEqual(habit.autor, self.user)
        self.assertFalse(habit.is_pleasant)