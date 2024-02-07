import cv2
"""There is unfortunately no way in order to make the openCv window with the image bigger, so a code is needed 
to show only a zoomed part in the image """


def zoom_at(img, zoom=1, angle=0, coord=None):
    cy, cx = [ i/2 for i in img.shape[:-1] ] if coord is None else coord[::-1]

    rot_mat = cv2.getRotationMatrix2D((cx,cy), angle, zoom)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result
    
# Read the image 
image = cv2.imread(r"C:\Users\issam.hammadi\OneDrive - IRT M2P\Bureau\Stage IRT M2P\code\images_echantillon_321\smallest image.jpg")


facteur_zoom = 2
largeur = int(image.shape[1] * facteur_zoom)
hauteur = int(image.shape[0] * facteur_zoom)
dimension = (largeur, hauteur)

image_agrandie  = cv2.resize(image, dimension, interpolation = cv2.INTER_LINEAR)

#Display the bigger image 
cv2.imshow('bigger image', image_agrandie)
cv2.imshow("image réelle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
