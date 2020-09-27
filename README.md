# gpt2-experiments

So I fine-tuned GPT-2 on a bunch of psychedelic reports on Erowid 

(Ideally I'd have this running on the cloud somewhere but the GPT-2 is so large and compute-hungry and I haven't found a fast and cheap way to do this)

## Acknowledgements 

* Max Woolf for his simplified GPT-2 fine-tuning package, [aitextgen](https://github.com/minimaxir/aitextgen)
* Matti Vuorre for compiling this wonderful [dataset](https://mvuorre.github.io/tmasc/articles/erowid/erowid.html) of Erowid reports
* Slightly unrelated but also wanted to mention this BEAUTIFUL [visualization](https://chemicalyouth.org/visualising-erowid/) of Matti's dataset

## How to Run

### Python 3 Requirements
* transformers==2.9.1
* pytorch-lightning==0.8.4
* aitextgen 
* flask

### Steps 
* Download [`pytorch_model.bin`](https://drive.google.com/file/d/1wMf6qgIWTOxx2e4F9wjQv5UUYSLkjJqp/view?usp=sharing) into the `model` folder
* Run `python3 app.py` in the command line to start Flask app and see generated texts!

## Nexts Steps?

Exploring Fabrice Bellard's [Text Synth](https://bellard.org/textsynth/), which is quite fast at GPT-2 inference without GPUs
