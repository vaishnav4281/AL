import openai
from diffusers import StableDiffusionPipeline
from moviepy.editor import ImageSequenceClip, AudioFileClip
from TTS.api import TTS
import os

# Step 1: Set up directories
def setup_directories():
    os.makedirs("images", exist_ok=True)
    os.makedirs("audio", exist_ok=True)
    os.makedirs("output", exist_ok=True)

# Step 2: Ask for user input (Main topic and language preference)
def get_user_input():
    # Get the engineering subject and main topic from the user
    subject = input("Provide subject: ")
    topic = input(f"Provide the main topic of {subject} to build the animation upon: ")
    
    # Get the preferred voiceover language from the user
    print("Choose a voiceover language:")
    print("1: English")
    print("2: Malayalam")
    lnc = input("Enter the number (1 or 2): ")
    
    if lnc == '2':
        language = "Malayalam"
        tts_model_name = "tts_models/ml/malayalam/tacotron2-DDC"  # Example Malayalam TTS model
    else:
        language = "English"
        tts_model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    
    return subject, topic, tts_model_name, language

# Step 3: Generate Script focusing on the Main Topic
def generate_script(subject, topic):
    prompt = f"Generate a detailed and engaging animated video script on the main topic '{topic}' within the subject '{subject}'. Explain the key concepts and provide examples. Make it cartoonically engaging. Even little kids should be able to understand the concepts through this. Also make it specifically centered for an animated video, so include funny schemes, plots, concepts in between to keep the audience engaged. Also include professional elements as well."
    openai.api_key = "api-key"  # Add your OpenAI API key here
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Step 4: Generate Animated Visuals for the Main Topic
def generate_animated_images_for_topic(topic):
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")
    prompt = f"Create an generic animation for the topic '{topic}' showcasing the key concepts visually. If possible do include various references as well to keep the audience engaged. Make the references scientifically accurate as well."
    
    images = []
    for i in range(30):  # Generate a few frames to animate key concepts
        image = pipe(prompt).images[0]
        images.append(image)
        image.save(f"images/scene_{i+1}.png")  # Save each frame
    return images

# Step 5: Generate Voiceover (based on language)
def generate_voiceover(script, tts_model_name):
    tts = TTS(model_name=tts_model_name, progress_bar=False)
    audio_file = "audio/voiceover.wav"
    tts.tts_to_file(text=script, file_path=audio_file)
    return audio_file

# Step 6: Create Animated Video
def create_animated_video(images, audio_file):
    clip = ImageSequenceClip([f"images/scene_{i+1}.png" for i in range(len(images))], fps=60)  # Slower animation speed
    audio = AudioFileClip(audio_file)
    final_clip = clip.set_audio(audio)
    final_clip.write_videofile("output/final_video.mp4", codec="libx264")

# Main function to run the entire pipeline
def main():
    setup_directories()
    
    # Step 1: Get user inputs for subject, main topic, and language
    subject, topic, tts_model_name, language = get_user_input()
    
    print(f"Generating a detailed script on {subject} with focus on the topic: {topic} in the {language} language...")
    
    # Step 2: Generate script for the lecture
    script = generate_script(subject, topic)
    print("Script Generated:\n", script)
    
    # Step 3: Generate animated visuals for the main topic
    print(f"Generating visuals for the topic: {topic}...")
    images = generate_animated_images_for_topic(topic)
    
    # Step 4: Generate voiceover based on the script
    print(f"Generating {language} voiceover...")
    audio_file = generate_voiceover(script, tts_model_name)
    
    # Step 5: Create the final animated video
    print("Creating video...")
    create_animated_video(images, audio_file)
    
    print("Animated video created successfully!")

if __name__ == "__main__":
    main()
