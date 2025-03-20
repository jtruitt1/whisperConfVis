# whisperConfVis
 
A small script to visualize the confidence of transcripts produced by OpenAI's [Whisper](https://github.com/openai/whisper/tree/main).

## Explanation
When run with the option `--word_timestamps True`, Whisper's JSON output will report a probability or confidence for each word transcribed:
```json
"segments": [
  '...',
  {
    "id": 181,
    "seek": 111812,
    "start": 1122.16,
    "end": 1122.76,
    "text": " And I will tell you.",
    '...' ,
    "words": [
      {
        "word": " And",
        "start": 1122.16,
        "end": 1122.44,
        "probability": 0.5770522356033325
      },
      {
        "word": " I",
        "start": 1122.44,
        "end": 1122.52,
        "probability": 0.9975531697273254
      },
      {
        "word": " will",
        "start": 1122.52,
        "end": 1122.66,
        "probability": 0.8680986166000366
      },
      {
        "word": " tell",
        "start": 1122.66,
        "end": 1122.76,
        "probability": 0.39947518706321716
      },
      {
        "word": " you.",
        "start": 1122.76,
        "end": 1122.76,
        "probability": 0.9782357215881348
      }
    ]
  },
  '...'
]  
 ```
This script takes the JSON output and converts it to a series of HTML paragraphs with each word as its own `<span>`. Each `<span>` background color is set based on Whisper's confidence, so that words the model is less confident in will be harder to decipher visually.

```html
<p>
	<span class="timestamp">[0:18:42]</span>	
	<span data-prob="0.5770522356033325" class="word" style="background-color: #999"> And</span> 
	<span data-prob="0.9975531697273254" class="word" style="background-color: #fff"> I</span> 
	<span data-prob="0.8680986166000366" class="word" style="background-color: #ddd"> will</span> 
	<span data-prob="0.39947518706321716" class="word" style="background-color: #666"> tell</span> 
	<span data-prob="0.9782357215881348" class="word" style="background-color: #fff"> you.</span> 
</p>
```

### Use-cases
The main use-cases envisioned for this script are: 
- allowing easy visual assessment of transcript quality before doing careful checking
- indicating where effort should be focused on checking or improving a transcript

## Usage
```shell
path/to/whisperConfVis.py output.json
```
where `path/to/whisperConfVis.py` is the location of the script file on your computer, and `output.json` is the JSON output file from running [Whisper](https://github.com/openai/whisper/tree/main).

At the moment, the script writes the output to the same directory that the input file is located in.
