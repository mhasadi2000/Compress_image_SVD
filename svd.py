import matplotlib.image as mpimg
# from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os
# ------------------
from ipywidgets import interact, interactive, interact_manual
import ipywidgets as widgets
from IPython.display import display


plt.rcParams['figure.figsize']=[16,8]

A=mpimg.imread('C:\\Users\\idasa\\Desktop\\svd\\1.bmp')
image_name ='Cow'

r=A[:,:,0]
g=A[:,:,1]
b=A[:,:,2]


print("compressing...")
ur,sr,vr = np.linalg.svd(r, full_matrices=False)
ug,sg,vg = np.linalg.svd(g, full_matrices=False)
ub,sb,vb = np.linalg.svd(b, full_matrices=False)

j=0
for k in (10,50,150,250):
 
    rr = np.dot(ur[:,:k],np.dot(np.diag(sr[:k]), vr[:k,:]))
    rg = np.dot(ug[:,:k],np.dot(np.diag(sg[:k]), vg[:k,:]))
    rb = np.dot(ub[:,:k],np.dot(np.diag(sb[:k]), vb[:k,:]))
        
    print("arranging...")
    rimg = np.zeros(A.shape)
    rimg[:,:,0] = rr
    rimg[:,:,1] = rg
    rimg[:,:,2] = rb
    
    for ind1, row in enumerate(rimg):
        for ind2, col in enumerate(row):
            for ind3, value in enumerate(col):
                if value < 0:
                    rimg[ind1,ind2,ind3] = abs(value)
                if value > 255:
                    rimg[ind1,ind2,ind3] = 255

    compressed_image = rimg.astype(np.uint8)
    plt.figure(j+1)
    j+=1
    plt.title('k='+str(k))
    plt.imshow(compressed_image)
    plt.axis('off')
    plt.show()
   

print("finish")