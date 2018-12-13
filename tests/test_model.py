from unittest import TestCase

from models import Launch


class LaunchTestCase(TestCase):
    """
    Unit test to launch model
    """

    def setUp(self):
        """
        Execute before each test
        """

        self.launch1 = Launch(
            flight_number=70,
            mission_name="Missão teste 1",
            rocket="Falcon 9",
            rocket_type="FT",
            launch_success=True,
            launch_year="2018",
            launch_date="2018-11-15T20:46:00.000Z"
        )

        self.launch2 = Launch(
            flight_number=75,
            mission_name="Missão teste 2",
            rocket="Falcon 6",
            rocket_type="FT",
            launch_success=False,
            launch_year="2018",
            launch_date="2018-11-19T20:46:00.000Z"
        )

        self.launch3 = Launch(
            flight_number=78,
            mission_name="Missão teste 3",
            rocket="Falcon 5",
            rocket_type="FT",
            launch_success=None,
            launch_year="2018",
            launch_date="2018-12-31T20:46:00.000Z"
        )

    def tearDown(self):
        """
        Execute after each test
        """

        del self.launch1
        del self.launch2

    def test_to_string_launch_success(self):
        """
        Test return of object by string with launch success
        """

        self.assertEqual(
            self.launch1.__str__(),
            "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n".format(
                "Número do Voo: 70", "Missão: Missão teste 1",
                "Foguete: Falcon 9 (FT)", "Ano de Lançamento: 2018",
                "Data de Lançamento (UTC): 15/11/2018 às 20:46",
                "Lançamento realizado com sucesso!"
            )
        )


    def test_to_string_launch_fail(self):
        """
        Test return of object by string with launch fail
        """

        self.assertEqual(
            self.launch2.__str__(),
            "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n".format(
                "Número do Voo: 75", "Missão: Missão teste 2",
                "Foguete: Falcon 6 (FT)", "Ano de Lançamento: 2018",
                "Data de Lançamento (UTC): 19/11/2018 às 20:46",
                "Lançamento falhou!"
            )
        )


    def test_to_string_with_no_launch(self):
        """
        Test return of object by string with no launch
        """


        self.assertEqual(
            self.launch3.__str__(),
            "{0}\n{1}\n{2}\n{3}\n{4}\n".format(
                "Número do Voo: 78", "Missão: Missão teste 3",
                "Foguete: Falcon 5 (FT)", "Ano de Lançamento: 2018",
                "Data de Lançamento (UTC): 31/12/2018 às 20:46"
            )
        )

    def test_get_flight_number(self):
        """
        Get the flight number
        """

        self.assertEqual(
            self.launch1.flight_number,
            "Número do Voo: 70"
        )

    def test_get_mission_name(self):
        """
        Get the mission name
        """

        self.assertEqual(
            self.launch1.mission_name,
            "Missão: Missão teste 1"
        )

    def test_get_launch_date(self):
        """
        Get the launch date
        """

        self.assertEqual(
            self.launch1.launch_date,
            "Data de Lançamento (UTC): 15/11/2018 às 20:46"
        )

    def test_get_launch_year(self):
        """
        Get the launch year
        """

        self.assertEqual(
            self.launch1.launch_year,
            "Ano de Lançamento: 2018"
        )

    def test_get_rocket(self):
        """
        Get the rocket
        """

        self.assertEqual(
            self.launch1.rocket,
            "Foguete: Falcon 9 (FT)"
        )

    def test_launch_success(self):
        """
        Get the launch success
        """

        self.assertEqual(
            self.launch1.launch_success,
            "Lançamento realizado com sucesso!"
        )

    def test_launch_fail(self):
        """
        Get the launch fail
        """

        self.assertEqual(
            self.launch2.launch_success,
            "Lançamento falhou!"
        )