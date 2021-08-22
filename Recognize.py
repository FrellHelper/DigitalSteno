from vosk import Model, KaldiRecognizer
import json
import os
import re
import wave
import subprocess
from bert_punctuation import Bert_punctuation

# Экземпляр класса
Bert_punctuation = Bert_punctuation()


def mp4_to_waw(video_path):
    if os.path.exists('protocol.wav'):
        os.remove('protocol.wav')

    # прописать абсолютный путь до ffmpg
    command = str(os.path.abspath("ffmpeg//bin//")) + "//ffmpeg -i " + video_path + " -ab 160k -ac 1 -ar 16000 -vn protocol.wav"
    subprocess.call(command, shell=True)


def recogn():
    model = Model(r"vosk-model-small-ru-0.15")

    wf = wave.open("protocol.wav", "rb")
    rec = KaldiRecognizer(model, 16000)

    result = ''
    last_n = False

    while True:
        data = wf.readframes(16000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f" {res['text']}"

    return result


def findtrigger(raw_string):
    ag = []
    dec = []

    dec_start = ([m.start() for m in re.finditer('решено начала', raw_string)])
    dec_end = ([m.start() for m in re.finditer('решено конец', raw_string)])
    ag_start = ([m.start() for m in re.finditer('повестка начала', raw_string)])
    ag_end = ([m.start() for m in re.finditer('повестка конец', raw_string)])

    for i in range(len(ag_start)):
        if ag_start[i] > ag_end[i]:
            ag.append(raw_string[ag_start[i]:ag_end[i + 1]])
        ag.append(raw_string[ag_start[i]:ag_end[i]])

    for i in range(len(dec_start)):
        if dec_start[i] > dec_end[i]:
            dec.append(raw_string[dec_start[i]:dec_end[i + 1]])
        dec.append(raw_string[dec_start[i]:dec_end[i]])


    return ag, dec

