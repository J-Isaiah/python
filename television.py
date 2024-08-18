class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, min_volume=MIN_VOLUME, max_volume=MAX_VOLUME, min_channel=MIN_CHANNEL,
                 max_channel=MAX_CHANNEL) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = min_volume
        self.__channel = min_channel

    def power(self) -> None:
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_down(self) -> None:
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
        if self.__muted and self.__status:
            self.__muted = False
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def __str__(self) -> str:
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}'
