class Television:
    """
    Creates a tv instance with the default values below
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, min_volume=MIN_VOLUME, max_volume=MAX_VOLUME, min_channel=MIN_CHANNEL, max_channel=MAX_CHANNEL):
        """
        INITS the varables of the tv
        :param min_volume: Default Unless otherwise
        :param max_volume: Default unless otherwise
        :param min_channel: Default unless otherwise
        :param max_channel: Default  unless otherwise
        """
        self.__status = False
        self.__muted = False
        self.__volume = min_volume
        self.__channel = min_channel

    def power(self) -> None:
        """
        Turns the tv on or off
        :return: None
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Changes the Muted tv value to either true or false
        :return: NONE
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Raises the channel one
        :return: None
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        moves teh channel of the tv down 1
        :return: None
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_down(self) -> None:
        """
        Turns the volume of the television down
        :return: None
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def volume_up(self) -> None:
        """
        :return: None
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def __str__(self) -> str:
        """
        Prints the status of the television
        :return: Formatted string of the television
        """
        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{0 if self.__muted else self.__volume}]'
