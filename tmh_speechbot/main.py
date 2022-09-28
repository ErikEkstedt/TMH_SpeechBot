from retico import run, stop
from retico.modules import (
    CallbackModule,
    MicrophoneModule,
    SpeakerModule,
    TextDispatcherModule,
    Wav2VecASRModule,
)


def callback(update_msg):
    for x, ut in update_msg:
        print(f"{ut}: {x.text} ({x.stability}) - {x.final}")


m1 = MicrophoneModule()
m2 = Wav2VecASRModule()
m3 = TextDispatcherModule()
# m4 = GoogleTTSModule("en-US", "en-US-Wavenet-A")
# m5 = SpeakerModule()
clb = CallbackModule(callback)

m1.subscribe(m2)
m2.subscribe(m3)
m2.subscribe(clb)
# m3.subscribe(m4)
# m4.subscribe(m5)

run(m1)
input()
stop(m1)
