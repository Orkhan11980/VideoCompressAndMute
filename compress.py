import os
import subprocess

input_folder = "/Path/to/videos"  # Replace with the path to your input folder
output_folder = "/Path/to/videos"  # Replace with the path to your output folder
video_codec = "libx264"  # Video codec for compression
crf = 30  # Constant Rate Factor for video quality

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all video files in the input folder
video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

for video_file in video_files:
    input_path = os.path.join(input_folder, video_file)
    output_path = os.path.join(output_folder, f"compressed_{video_file}")

    # Build the FFmpeg command to compress the video and remove audio
    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", video_codec,
        "-crf", str(crf), #Constant Rate Factor. A lower CRF value results in higher video quality but larger file sizes
        "-an",  # Remove audio
        output_path
    ]

    # Run the FFmpeg command using subprocess
    subprocess.run(cmd)

print("Video compression and muting completed.")
