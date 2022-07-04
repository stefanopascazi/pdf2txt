# TEXTRACTOR
Convert a lot of files extensions into text

## How to use

Build image:
```bash
$ docker pull stedotdev/textractor
```
Create an alias command
```bash
$ alias textractor='docker run --rm -ti -v $(pwd)/local_file:/files stedotdev/textractor'
```

Execute conversion
```bash
$ textractor -i your-file.extension > sample.txt
```

## Currently extension supporting
textractor supports a growing list of file types for text extraction.

- .csv
- .doc
- .docx
- .eml
- .epub
- .gif
- .jpg and .jpeg
- .json
- .html and .htm
- .mp3
- .msg
- .odt
- .ogg
- .pdf
- .png
- .pptx
- .rtf
- .tiff
- .txt
- .wav
- .xlsx
- .xls
