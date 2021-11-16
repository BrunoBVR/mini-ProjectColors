import streamlit as st
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

st.title("Color Quantization")

st.write('''
Color quantization of given image. Read about it [here](https://en.wikipedia.org/wiki/Color_quantization).
''')

def quant_img(image_as_array, k):
    '''
    Given an image, quantize that image in k colors based on KMeans clustering.
    '''
    # image_as_array = mpimg.imread(path)
    
    (h,w,c) = image_as_array.shape
    
    image_as_array2d = image_as_array.reshape(h*w,c)
    
    model = KMeans(n_clusters = k)
    
    labels = model.fit_predict(image_as_array2d)
    
    rgb_codes = model.cluster_centers_.round(0).astype(int)
    
    quantized_image = np.reshape(rgb_codes[labels], (h,w,c))

    fig, axs = plt.subplots(1, 2, figsize=(10,4),dpi=200)

    axs[0].imshow(image_as_array)
    axs[0].axis('off')
    axs[0].set_title('Original image')
    axs[1].imshow(quantized_image)
    axs[1].axis('off')
    axs[1].set_title('Color quantized image with '+str(k)+' distinct colors')
    
    return fig

def full_analysis(clusters = 5):

    uploaded_file = st.file_uploader("Upload an image to quantize:", type=["jpg","png","jpeg"])

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # st.image(image)

        return quant_img(image, clusters)

k = st.slider('Number of distinct colors in final image:', 1, 10, 5)

figure = full_analysis(k)

# st.write('''
# # Add download option!!
# ''')

if figure is not None:

    st.pyplot(figure, dpi=300)
