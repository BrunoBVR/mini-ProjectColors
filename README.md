# Mini-project: Color analyzer with streamlit

This fun and quick project is an application based on [this](https://towardsdatascience.com/building-an-image-color-analyzer-using-python-12de6b0acf74) great article.

According to the post author:
> In this post, I will show you how to create a program that can detect colors and then calculate the weights of the colors in an image. (...)we will use Scikit-learn and OpenCV as our main modules. Especially, graphic designers and web designers will find this program very helpful. Not only detecting the colors but also seeing their volume levels in an image is a super neat feature.

## My (small) contribution

The notebook `projectColors.ipynb` has the implementation from the article with very small modifications to the author's declared functions. The main idea is to put everything into a single function that takes the number of clusters to divide the image into.

## Building the app

Inside the `streamlit-app` folder there is a script for building a streamlit app to let the user upload an image and have it analyzed. The app lets users, beside uploading their own image (in formats `jpg`, `jpeg` and `png`), choose the number of clusters with a simple slider bar.

## Shared app

[Here](https://share.streamlit.io/brunobvr/mini-projectcolors/main/streamlit-app/color-app.py)

# Mini-project: Color quantizer with streamlit

This one is even more fun! We can create cool visuals using color quantization: Read about it [here](https://en.wikipedia.org/wiki/Color_quantization).

The notebook [colorQuantization](colorQuantization.ipynb) has the idea as a function using KMeans and some basic matplotlib.

Inside the `streamlit-app` folder there is a script for building a streamlit app to let the user upload an image and have it quantized ([qunat-app.py](qunat-app.py)). The app lets users, beside uploading their own image (in formats `jpg`, `jpeg` and `png`), choose the number of distinct colors with a simple slider bar.

## Shared app

[Here](https://share.streamlit.io/brunobvr/mini-projectcolors/main/streamlit-app/quant-app.py)