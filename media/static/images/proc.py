import cv2
import numpy as np

def vconcat_resize(img_list, interpolation = cv2.INTER_CUBIC):
    # take minimum width
    w_min = min(img.shape[1] for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img, (w_min, img.shape[0] * w_min // img.shape[1]), interpolation = interpolation) for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)

img = cv2.imread('recursion.png', )

height, width, channels = img.shape
print(width, height, channels)

required_height = 267
to_add = (required_height-height)//2

add_top_bottom = np.ones((to_add, width))

print(add_top_bottom.shape)

cv2.imshow('will be added', add_top_bottom)

# final_img = vconcat_resize([add_top_bottom, img, add_top_bottom])

# cv2.imshow('pic', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()