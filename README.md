# Virtual Billboard
This repo gives a demonstration of creating a virtual billboard using Homogarphy matrix.ROI is extracted from the target image where we want to superimpose our virtual billboard.The virtual image goes through a perspective transformation so that it can be warped along the same plane as the target image. 

## Design pipeline
The pipeline is demonstrated as follows:
* Extract the ROI from the target image(building) using a mouse click event.
![ROI Image](Intermediate%20_Output/Building_ROI_Coordinate.png?raw=true)
* Extract the coordinates of the corners points from the width and height of the virtual image(potrait).
* calculate the homography matrix using the cv2.findHomography() function.
* Perform a perspective transformation on the virtual image so that it will be along the same plane as the target image.
* Create a black mask using np.zeros() of the size of the target image.
![Black Mask](Intermediate%20_Output/Black_Mask.png?raw=true)
* Fill the part of the mask, correspoing to the ROI extracted earlier, with white area using cv2.fillConvexPoly() function. 
![Filled Mask](Intermediate%20_Output/Filled_Mask.png?raw=true)
* Invert the obtained mask using cv2.bitwise_not() function.
![Inverted Mask](Intermediate%20_Output/Inverted_Filled_Mask.png?raw=true)
* Apply this mask on the target image using cv2.bitwise_and() function to fill the ROI with zeroes and the rest of the image can reatin their original pixel intensities.
![Mask on Target Image](Intermediate%20_Output/Inverted_filled_mask_on_target_image.png?raw=true)
* Use cv2.bitwise_or() function to superimpose the virtual image on the ROI of the target image.
![Final Output](/Warped_Images/Final_Warped_Image.png?raw=true)

## Note: The perspective transformation depends upon the order of the selection of coordinates during mouse call back, which in turns impact the final orientation of the warped image. The reason being the homography is calculated based upon the two set of points from the source and target image. Any deviation from the order of points between the source and target image produces a differnt homography matrix which results in a differnt perspective. 
