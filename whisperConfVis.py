#!/usr/bin/env python3

from datetime import timedelta
import json, argparse

# Convert probability into color value
# (Higher prob => lighter background => more legible text)
def getStyle(prob):
	vals = '13579bdf'
	decCol = int(8*prob)
	hexCol = vals[decCol]*3
	return f'background-color: #{hexCol}'

# Parse command-line argument
description = 'Given a word-level JSON output file from OpenAI\'s Whisper CLI,'
description+= 'create an HTML file in same dir w/ confidence shown as bg color'
parser = argparse.ArgumentParser(
	prog='WhisperConfidenceVisualizer',
	description=description
	)
parser.add_argument('jsonFile', help='path of the JSON file to use as input')
args = parser.parse_args()
jsonFile = args.jsonFile

# Read data from JSON file
with open(jsonFile) as f:
	data = json.load(f)

# Convert values in JSON to HTML
# TODO: Use an HTML parser like Beautiful Soup instead of just winging it
text = ''
for seg in data['segments']:
	start = int(seg["start"])
	start = str(timedelta(seconds=start))
	text += f'<p><span class="timestamp">[{start}]</span>\t'
	for word in seg['words']:
		prob = word["probability"]
		text += f'<span data-prob="{prob}" class="word" style="{getStyle(prob)}">'
		text += f'{word["word"]}</span> '
	text+= '</p>\n'

# Wrap text with appropriate tags to create a valid HTML file
prol = f'<!DOCTYPE html>\n<html lang="{data["language"]}">\n<head></head>\n'
prol += '<body>\n'
html = prol + text + '</body></html>'

# Write the HTML to a file
htmlFile = jsonFile[:-4] + "html"

with open(htmlFile, 'w') as f:
	f.write(html)
