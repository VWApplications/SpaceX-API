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
            print("5) Sair\n")

            try:
                option = int(input("Insira uma opção: "))
            except ValueError:
                print("Você deve inserir somente números inteiros de preferencia de 1 a 5")
                option = 0


            if option < 1 or option > 5:
                print("Essa opção não existe, por favor insira uma opção válida.\n")
                cls.__clean(3)
            elif option == 5:
                cls.__close()
                break
            else:
                cls.__show_result(option)

                answer = input("Deseja sair da aplicação? (S/N): ")

                if answer.lower().startswith("s"):
                    cls.__close()
                    break

                cls.__clean(1)

    @classmethod
    def __show_result(cls, option):
        """
        Run a specific option inserted

        :param option: Option to visualize some datas
        """
        print()

        if option == SpaceX.NEXT_LAUNCH:
            cls.__next_launch()
        elif option == SpaceX.LATEST_LAUNCH:
            cls.__latest_launch()
        elif option == SpaceX.UPCOMING_LAUNCHES:
            cls.__upcoming_launches()
        elif option == SpaceX.PAST_LAUNCHES:
            cls.__past_launches()
        else:
            print("Opção invalida")

    @staticmethod
    def __clean(seconds):
        """
        Clean the prompt
        """

        time.sleep(seconds)

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

    @staticmethod
    def __next_launch():
        """
        Returns the next launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/next")

        print(connection.result)

    @staticmethod
    def __upcoming_launches():
        """
        Returns the closest upcoming launches
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/upcoming")

        for result in connection.result:
            print(result)
            print("----------------------------------------------------------\n")

    @staticmethod
    def __latest_launch():
        """
        Returns the latest launch
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/latest")

        print(connection.result)

    @staticmethod
    def __past_launches():
        """
        Returns the past launches
        """

        connection = Connect("https://api.spacexdata.com/v3/launches/past")

        for result in connection.result:
            print(result)
            print("----------------------------------------------------------\n")

