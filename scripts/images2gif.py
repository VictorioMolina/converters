import os
import imageio.v3 as iio

def get_image_files(input_dir):
    return [
        os.path.join(input_dir, filename)
        for filename in sorted(os.listdir(input_dir))
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
    ]

def images_to_gif(input_imgs_dir, output_gif):
    if not os.path.exists(input_imgs_dir):
        return

    image_files = get_image_files(input_imgs_dir)

    if not image_files:
        return

    images = [iio.imread(filename) for filename in image_files]
    iio.imwrite(output_gif, images)

    print("Done!")

if __name__ == "__main__":
    input_imgs_dir = input("Input images dir: ")
    output_gif = input("Output .gif path: ")
    images_to_gif(input_imgs_dir, output_gif)
