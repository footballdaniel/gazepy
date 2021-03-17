from unittest.mock import MagicMock, PropertyMock

from gazeclassify.serializer.pupil_serializer import PupilDataDeserializer


class Test_PupilDataSerializer:
    def test_instantiate_datarecords(self) -> None:
        # https://docs.python.org/3/library/unittest.mock.html#patch
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock

        pupilDataLoader = MagicMock()
        p = PropertyMock(return_value=[0])
        type(pupilDataLoader).world_timestamps = p

        serializer = PupilDataDeserializer()
        print("WARNING WRITE TEST")
        assert pupilDataLoader.world_timestamps == [0]

    def test_serialization_video_to_numpy_array(self) -> None:
        pass
