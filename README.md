# Animated Lectures - AL

## Overview

**Animated Lectures - AL** is a Python program that generates engaging animated videos for engineering subjects. Leveraging AI models for text generation and image synthesis, it creates a complete lecture video with voiceover and visuals based on user-defined topics.

## Features

- **Interactive Script Generation**: Generate a detailed and engaging lecture script using OpenAI's GPT API.
- **Dynamic Visuals**: Create animations related to the topic using Stable Diffusion to keep the audience engaged.
- **Multilingual Voiceovers**: Generate voiceovers in English or Malayalam using TTS (Text-to-Speech).
- **High-Quality Video Output**: Compile everything into a smooth animated video at 60 FPS.

## Requirements

Make sure you have the following installed before running the program:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    Bash
     ```
     git clone https://github.com/arktrek/AL.git
     cd AL
     ```
   
2. Install the required packages:
     Python
     ``` 
     pip install openai diffusers moviepy TTS
     ```
3. Provide necessary inputs as shown.
4. The program will generate an animated video based on your inputs, saving the final output as "Lecture.mp4" in the output directory

## Directory Structure:
AnimatedLectures-AL/
├── main.py             # Main script to run the program

├── images/             # Directory to store generated images

├── audio/              # Directory to store generated audio files

└── output/             # Directory to store the final video output

