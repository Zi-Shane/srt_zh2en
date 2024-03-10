# SRT file translation tool

## Overview

Base on: [opus-mt-zh-en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en?text=%E8%BC%89%E6%88%91%E5%88%B0%E7%8F%BE%E5%9C%A8%E6%88%91%E4%BD%8F%E7%9A%84%E9%80%99%E8%A3%A1)

Python: 3.10.8

## Install

1. Clone this repo
2. Install dependencies
   - pip install transformers sentencepiece
3. Move .srt file to `validation_data` folder
4. Modify `path = "./validation_data/sukhothai_captions.srt"` in `parse_srt.py`
5. Run `pyhton parse_srt.py`
6. Finished. ouput will appear in `validation_data` folder
