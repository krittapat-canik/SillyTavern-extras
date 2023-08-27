import subprocess

secure = True
use_cpu = True
use_sd_cpu = True
extras_enable_captioning = True
Captions_Model = "Salesforce/blip-image-captioning-large"
extras_enable_emotions = True
Emotions_Model = "joeddav/distilbert-base-uncased-go-emotions-student"
extras_enable_memory = True
Memory_Model = "Qiliang/bart-large-cnn-samsum-ElectrifAi_v10"
extras_enable_silero_tts = True
extras_enable_edge_tts = True
extras_enable_sd = True
SD_Model = "ckpt/anything-v4.5-vae-swapped"
extras_enable_chromadb = True

params = []
if use_cpu:
    params.append('--cpu')
if use_sd_cpu:
    params.append('--sd-cpu')
if secure:
    params.append('--secure')
params.append('--share')
ExtrasModules = []

if extras_enable_captioning:
    ExtrasModules.append('caption')
if extras_enable_memory:
    ExtrasModules.append('summarize')
if extras_enable_emotions:
    ExtrasModules.append('classify')
if extras_enable_sd:
    ExtrasModules.append('sd')
if extras_enable_silero_tts:
    ExtrasModules.append('silero-tts')
if extras_enable_edge_tts:
    ExtrasModules.append('edge-tts')
if extras_enable_chromadb:
    ExtrasModules.append('chromadb')

params.append(f'--classification-model={Emotions_Model}')
params.append(f'--summarization-model={Memory_Model}')
params.append(f'--captioning-model={Captions_Model}')
params.append(f'--sd-model={SD_Model}')
params.append(f'--enable-modules={",".join(ExtrasModules)}')

cmd = ["python", "server.py"] + params
print(" ".join(cmd))
extras_process = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd='/SillyTavern-extras')
print('processId:', extras_process.pid)
while True:
    line = extras_process.stdout.readline().decode().strip()
    if line != '' and line is not None:
        print(line)
