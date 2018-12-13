import os, sys, time

from connections import Connect


class SpaceX(object):
    """
    Menu to choice the consult.
    """

    NEXT_LAUNCH = 1
    LATEST_LAUNCH = 2
    UPCOMING_LAUNCHES = 3
    PAST_LAUNCHES = 4

    @classmethod
    def run(cls):
        """
        Shows the options for the user

        :return: chosen option
        """

        while(True):
            print("O que você deseja visualizar?\n")

            print("1) Próximo Lançamento")      # next_launch
            print("2) Último Lançamento")       # latest launch
            print("3) Próximos Lançamentos")    # upcoming launches
            print("4) Lançamentos Passados")    # past launches
            print("5) Sair\n")  # past launches

            option = int(input("Insira uma opção: "))

            if option < 1 or option > 5:
                print("Essa opção não existe, por favor insira uma opção válida.\n")
            elif option == 5:
                cls.__close()
                break
            else:
                cls.__show_result(option)

                answer = input("Deseja voltar ao menu? (S/N): ")

                if answer.lower().startswith("n"):
                    cls.__close()
                    break

            cls.clean()


    @staticmethod
    def clean():
        """
        Clean the prompt
        """

        time.sleep(1)

        if 'win' in sys.platform:
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def __close():
        """
        Close the program.
        """

        print("Finalizando o programa...")
        time.sleep(1)

    @classmethod
    def __show_result(cls, option):
        """
        Run a specific option inserted

        :param option: Option to visualize some datas
        """
        print("")

        if option == SpaceX.NEXT_LAUNCH:
            cls.__next_launch()
        elif option == SpaceX.LATEST_LAUNCH:
            cls.__latest_launch()
        elif option == SpaceX.UPCOMING_LAUNCHES:
            cls.__upcoming_launches()
        else:
            cls.__past_launches()

    @staticmethod
    def __next_launch():
        """
        Returns the closest upcoming launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/next")

        print(connection.result)

    @staticmethod
    def __upcoming_launches():
        """
        Returns the closest upcoming launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/upcoming")

        for result in connection.result:
            print(result)
            print("----------------------------------------------------------\n")

    @staticmethod
    def __latest_launch():
        """
        Returns the most recent launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/latest")

        print(connection.result)

    @staticmethod
    def __past_launches():
        """
        Returns the closest upcoming launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/past")

        for result in connection.result:
            print(result)
            print("----------------------------------------------------------\n")

