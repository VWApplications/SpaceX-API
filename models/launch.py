from datetime import datetime


class Launch(object):
    """
    SpaceX Launch
    """

    def __init__(self, flight_number, mission_name, rocket,
                 rocket_type, launch_success,
                 launch_year, launch_date):
        """
        Constructor
        """

        self.__flight_number = flight_number
        self.__mission_name = mission_name
        self.__launch_date = launch_date
        self.__launch_year = launch_year
        self.__rocket = rocket
        self.__rocket_type = rocket_type
        self.__launch_success = launch_success

    def __str__(self):
        """
        Give a object a string representation

        :return: string representation of object
        """

        if self.__launch_success is not None:
            return "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n".format(
                self.flight_number, self.mission_name, self.rocket,
                self.launch_year, self.launch_date, self.launch_success
            )

        return "{0}\n{1}\n{2}\n{3}\n{4}\n".format(
            self.flight_number, self.mission_name, self.rocket,
            self.launch_year, self.launch_date
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

        date = datetime.strptime(self.__launch_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        return "Data de Lançamento (UTC): {0}".format(date.strftime("%d/%m/%Y às %H:%M"))

    @property
    def launch_year(self):
        """
        Get the launch year

        :return: launch year
        """

        return "Ano de Lançamento: {0}".format(self.__launch_year)

    @property
    def rocket(self):
        """
        Get the rocket

        :return: rocket
        """

        return "Foguete: {0} ({1})".format(self.__rocket, self.__rocket_type)

    @property
    def launch_success(self):
        """
        Verify if the launch happened successfully!

        :return: Success message or Fail message.
        """

        if self.__launch_success:
            return "Lançamento realizado com sucesso!"

        return "Lançamento falhou!"
