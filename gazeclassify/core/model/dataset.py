from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Metadata:
    recording_name: str
    world_video_file: Path
    world_video_width: int
    world_video_height: int
    world_video_frame_number: int
    world_video_frame_rate: int


@dataclass
class Dataset(ABC):
    records: List[DataRecord]
    metadata: Metadata


@dataclass
class DataRecord:
    world_timestamp: float
    video: VideoFrame
    gaze: GazeData


@dataclass
class VideoFrame:
    frame_index: int


@dataclass
class GazeData:
    x: float
    y: float
