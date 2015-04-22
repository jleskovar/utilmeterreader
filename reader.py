import cv2

image = cv2.imread('cropped.jpg')
cv2.imshow('original', image)

# dilated = cv2.dilate(image, None)
# cv2.imshow('dilated_color', dilated)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# gray_dilated = cv2.dilate(gray, None)
# cv2.imshow('gray_dilated', gray_dilated)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(gray)
print "ret %s labels %s stats %s centroid %s" % (ret, labels, stats, centroids)

marked_image = image[:]
marked_image[corners > 0.01 * corners.max()] = [0, 255, 0]
cv2.imshow('corners', marked_image)

cv2.waitKey(0)
