from moviepy.editor import *

def gif_to_mp4(input_gif, output_mp4):
    if not input_gif.endswith('.gif'):
        return

    clip = VideoFileClip(input_gif)
    clip.write_videofile(output_mp4, codec='libx264')
    print("Done!")

if __name__ == "__main__":
    input_gif = input("Input .gif path: ")
    output_mp4 = input("Output .mp4 path: ")

    gif_to_mp4(input_gif, output_mp4)
