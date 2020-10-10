[![Build Status](https://travis-ci.org/whitehamster26/wh-imgsizer.svg?branch=master)](https://travis-ci.org/whitehamster26/wh-imgsizer)

[![Maintainability](https://api.codeclimate.com/v1/badges/446b11ca5cc57066c1fe/maintainability)](https://codeclimate.com/github/whitehamster26/wh-imgsizer/maintainability)
 [![Test Coverage](https://api.codeclimate.com/v1/badges/446b11ca5cc57066c1fe/test_coverage)](https://codeclimate.com/github/whitehamster26/wh-imgsizer/test_coverage)

<h2>Description</h2>
This application allows you to change the image size using only the command line. Instead of the size, you can specify the name of another file to take the size from.

<h2>Installation</h2>
> python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ wh-imgsizer

<h2>Usage</h2>

<code>wh-imgsizer FILE SIZE --name (optional)</code>

Size should be in W-H format where W is width and H is height.

<code>user@:~$ wh-imgsizer image.jpg 800-600</code><br>
<code>File image.jpg was resized to 800x600 and saved as image.jpg.</code><br>

Instead of SIZE you can enter the name of another file from which you want to take the size.

<code>user@:~$ wh-imgsizer image2.jpg image.jpg</code><br>
<code>File image2.jpg was resized to 800x600 and saved as image2.jpg.</code>

If you don't specify a name, you will overwrite the existing file.
You can choose a name of output file by entering --name NAME

<code>user@:~$ wh-imgsizer image2.jpg image.jpg --name image3.jpg</code><br>
<code>File image2.jpg was resized to 800x600 and saved as image3.jpg.</code>
