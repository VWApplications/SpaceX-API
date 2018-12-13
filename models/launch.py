class Launch(object):
    """
    SpaceX Launch
    """

    def __init__(self, flight_number, mission_name, rocket,
                 rocket_type, is_tentative, launch_success,
                 launch_date):
        """
        Constructor
        """

        self.__flight_number = flight_number
        self.__mission_name = mission_name
        self.__launch_date = launch_date
        self.__rocket = rocket
        self.__rocket_type = rocket_type
        self.__is_tentative = is_tentative
        self.__launch_success = launch_success

    def __str__(self):
        """
        Give a object a string representation

        :return: string representation of object
        """

        if self.is_tentative:
            return "Tentativa de lançamento do foguete {0} com número de voo {1} será lançado em {2} na missão {3}".format(
                self.rocket, self.flight_number,
                self.launch_date, self.mission_name
            )

        if self.__launch_success:
            return "Lançamento do foguete {0} com número de voo {1} lançado em {2} na missão {3} com sucesso!".format(
                self.rocket, self.flight_number,
                self.launch_date, self.mission_name
            )

        return "Lançamento do foguete {0} com número de voo {1} lançado em {2} na missão {3} falhou!".format(
            self.rocket, self.flight_number,
            self.launch_date, self.mission_name
        )

    @property
    def flight_number(self):
        """
        Get the flight number of launch.

        :return: flight number
        """

        return "Número do Voo: {0}".format(self.__flight_number)

    @property
    def mission_name(self):
        """
        Get the mission name

        :return: mission name
        """

        return "Missão: {0}".format(self.__mission_name)

    @property
    def launch_date(self):
        """
        Get the lauch date in dd/mm/yyyy às hh:mm

        :return: lauch date
        """

        return "Data de Lançamento (UTC): {0}".format(self.__launch_date)

    @property
    def lauch_year(self):
        """
        Get the launch year

        :return: launch year
        """

        return "Ano de Lançamento: {0}".format(self.__launch_date)

    @property
    def rocket(self):
        """
        Get the rocket

        :return: rocket
        """

        return "Rocket {0} ({1})".format(self.__rocket, self.__rocket_type)

    @property
    def launch_success(self):
        """
        Verify if the launch happened successfully!

        :return: True if happened successfully and False otherwise
        """

        if self.__launch_success:
            return "Lançamento realizado com sucesso!"

        return "Lançamento falhou!"

    @property
    def is_tentative(self):
        """
        Verify if the launch is a tentative or is real

        :return: True if is tentative and False otherwise
        """

        return self.__is_tentative