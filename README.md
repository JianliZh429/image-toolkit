# image-toolkit
Tools to process images, implemented by opencv

## Content
### [License photo processing](./cli/license_photo.py)
To extract the person area from the given image and output the license photo with specified size and three background color
- to show the help information
    ```shell
    python cli/license_photo.py --help 
    ```
- process the given image and output the license format photo to $output_dir with three backgroud colors, blue, red, white, and in the default size of 1 inch
    ```shell
    python cli/license_photo.py --image_file $file_path --out_dir $output_dir
    ```