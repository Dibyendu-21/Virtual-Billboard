# Virtual Billboard
This repo gives a demonstration of creating a virtual billboard using Homogarphy matrix.ROI is extracted from the target image where we want to superimpose our virtual billboard.The virtual image goes through a perspective transformation so that it can be warped along the same plane as the target image. 

##Design pipeline
The pipeline is demonstrated as follows:
* Extract the ROI from the target image(building) using a mouse click event.
* Extract the coordinates of the corners points from the virtual image(potrait).
* calculate the homography matrix using the cv2.findHomography() function.
* Perform a perspective transformation on the virtual image so that it will be along the same plane as the target image.
* Create a black mask using np.zeros() of the size of the target image.
* Fill the part of the mask, correspoing to the ROI extracted earlier, with white area using cv2.fillConvexPoly() function. 
* Invert the obtained mask using cv2.bitwise_not() function.
* Apply this mask on the target image using cv2.bitwise_and() function to fill the ROI with zeroes and the rest of the image can reatin their original pixel intensities.
* Use cv2.bitwise_or() function to superimpose the virtual image on the ROI of the target image.
