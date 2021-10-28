"""
Author: https://github.com/jojo96/ASCIIGan
"""


import numpy as np
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.header("Generate ASCII images using GAN")
st.write("Choose any image and get corresponding ASCII art:")

uploaded_file = st.file_uploader("Choose an image...")


def asciiart(in_f, SC, GCF, out_f, bgcolor='white', color='#0000FF'):
    # The array of ascii symbols from white to black
    chars = np.asarray(list(' .,:irs?@9B&#'))

    # Load the fonts and then get the the height and width of a typical symbol
    # You can use different fonts here
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]

    WCF = letter_height / letter_width

    # open the input file
    img = Image.open(in_f)

    # Based on the desired output image size, calculate how many ascii letters are needed on the width and height
    widthByLetter = round(img.size[0] * SC * WCF)
    heightByLetter = round(img.size[1] * SC)
    S = (widthByLetter, heightByLetter)

    # Resize the image based on the symbol width and height
    img = img.resize(S)

    # Get the RGB color values of each sampled pixel point and convert them to graycolor using the average method.
    # Refer to https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/ to know about the algorithm
    img = np.sum(np.asarray(img), axis=2)

    # Normalize the results, enhance and reduce the brightness contrast.
    # Map grayscale values to bins of symbols
    img -= img.min()
    img = (1.0 - img / img.max())**GCF * (chars.size - 1)

    # Generate the ascii art symbols
    lines = ("\n".join(("".join(r) for r in chars[img.astype(int)]))).split("\n")

    # Create an image object, set its width and height
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)

    # Print symbols to image
    leftpadding = 0
    y = 0
    lineIdx = 0
    for line in lines:
        lineIdx += 1

        draw.text((leftpadding, y), line, color, font=font)
        y += letter_height

    # Save the image file
    newImg.save(out_f)


def imgGen2(img1):
    inputf = img1  # Input image file name
    SC = 0.1    # pixel sampling rate in width
    GCF = 2      # contrast adjustment
    asciiart(inputf, SC, GCF, "results.png", bgcolor='black', color="#03A062")
    img = Image.open(img1)
    img2 = Image.open('results.png').resize(img.size)
    return img2


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption='Input Image', use_column_width=True)
    im = imgGen2(uploaded_file)
    st.image(im, caption='ASCII art', use_column_width=True)
