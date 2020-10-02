# gpt2-experiments

So I fine-tuned GPT-2 on a bunch of psychedelic reports on Erowid 

(Ideally I'd have this running on the cloud somewhere but GPT-2 is so large and compute-hungry and I haven't found a fast and cheap way to do this)

## Acknowledgements 

* Max Woolf for his easy-to-use GPT-2 fine-tuning package, [aitextgen](https://github.com/minimaxir/aitextgen)
* Matti Vuorre for compiling this wonderful [dataset](https://mvuorre.github.io/tmasc/articles/erowid/erowid.html) of Erowid reports (also check out this BEAUTIFUL [visualization](https://chemicalyouth.org/visualising-erowid/) of Matti's dataset)

## How to Run

* Install package requirements with the command `pip install -r requirements.txt`
* Download [`pytorch_model.bin`](https://drive.google.com/file/d/1wMf6qgIWTOxx2e4F9wjQv5UUYSLkjJqp/view?usp=sharing) into the `model` folder
* Run `python app.py` and see generated texts at http://127.0.0.1:5000/

## Next Steps?

Exploring Fabrice Bellard's [Text Synth](https://bellard.org/textsynth/), which is quite fast at GPT-2 inference without GPUs
