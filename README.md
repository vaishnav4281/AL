# 🎓 Animated Lectures - AL

## 🌟 Overview

**Animated Lectures - AL** is a Python program that generates engaging animated videos for engineering subjects. Leveraging AI models for text generation and image synthesis, it creates a complete lecture video with voiceover and visuals based on user-defined topics. 🎬✨

## ✨ Features

- **📝 Interactive Script Generation**: Generate a detailed and engaging lecture script using OpenAI's GPT API.
- **🎨 Dynamic Visuals**: Create animations related to the topic using Stable Diffusion to keep the audience engaged.
- **🌍 Multilingual Voiceovers**: Generate voiceovers in **English** or **Malayalam** using TTS (Text-to-Speech).
- **📹 High-Quality Video Output**: Compile everything into a smooth animated video at **60 FPS** for an immersive experience.

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
3. Setup OpenAI API Key: Replace [ openai.api_key="api-key" ] in the code with your actual OpenAI API key.
4. Provide necessary inputs as shown.
5. The program will generate an animated video based on your inputs, saving the final output as "Lecture.mp4" in the output directory

## Directory Structure:
AL/

├── anilect.py             # Main script to run the program

├── images/             # Directory to store generated images

├── audio/              # Directory to store generated audio files

└── output/             # Directory to store the final video output

## Code Explanation
Here's a brief breakdown of the main components in the code:

1. Setup Directories: Creates directories for storing images, audio, and final video output.

2. User Input: Asks for the subject, main topic, and preferred voiceover language.

3. Script Generation: Uses the OpenAI GPT API to generate a detailed script for the lecture, tailored to engage the audience with fun concepts and professional elements.

4. Image Generation: Utilizes Stable Diffusion to create a series of animated images based on the main topic, ensuring they are visually engaging and scientifically accurate.

5. Voiceover Generation: Creates a voiceover of the generated script using a selected TTS model in the preferred language.

6. Video Creation: Compiles the images and voiceover into a final animated video, outputting it as "Lecture.mp4".

## Acknowledgments
- **OpenAI** for utilising the GPT API for generating the video script.
- **Stable Diffusion** for creating engaging visuals.
- **MoviePy** for video editing capabilities.
- **TTS** for text-to-speech conversion in multiple languages.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions and enhancements are always welcome!!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
