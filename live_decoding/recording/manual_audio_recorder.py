from recording.audio_recorder import AudioRecorder


class ManualAudioRecorder(AudioRecorder):
    def __init__(self):
        super().__init__()

    def _on_chunk(self):
        pass

    def _on_file_saved(self):
        pass
