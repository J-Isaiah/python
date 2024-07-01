import pytest
from television import *


@pytest.fixture
def tv():
    tv = Television()
    tv.power()

    yield tv


def test_init(tv):
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'


def test_power(tv):
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'

    tv.power()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0]'


def test_mute(tv):
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [1]'
    tv.mute()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'
    tv.volume_up()
    tv.power()
    tv.mute()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [2]'
    tv.power()
    tv.mute()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'


def test_channel_up(tv):
    tv.channel_up()
    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = [False], Channel = [1], Volume = [0]'

    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = [True], Channel = [2], Volume = [0]'

    tv.channel_up()
    tv.channel_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'


def test_channel_down(tv):
    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0]'

    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = [True], Channel = [3], Volume = [0]'


def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0]'

    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [1]'

    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [2]'
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [2]'





def test_volume_down(tv):
    tv.power()
    tv.volume_down()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0]'

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [1]'

    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'
    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'
