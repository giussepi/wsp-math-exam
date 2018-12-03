# -*- coding: utf-8-*-
""" assessments's constants """


class QuestionDifficulty:
    """ Holds questions difficulty levels """

    EASY = '0'
    MEDIUM = '1'
    HARD = '2'

    CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )


class PassFail:
    """ Holds pass/fail statuses """

    FAILED = '0'
    PASSED = '1'

    CHOICES = (
        (FAILED, 'Failed'),
        (PASSED, 'Passed'),
    )
