import cv2
from simple_facerec import SimpleFacerec
import os

# def face_recognition():
#     print("Recognizing faces and generating results")
#     sfr = SimpleFacerec()
#     sfr.load_encoding_images("face_library/")
#     # cap = cv2.VideoCapture(0)
#     for file in os.listdir("HR"):
#         print("HR/"+file)
#         img = cv2.imread("HR/"+file)
#         face_locations, face_names = sfr.detect_known_faces(img)
#         for face_loc, name in zip(face_locations, face_names):
#             y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
#             cv2.putText(img, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 200), 4)
#         cv2.imwrite("results/"+file+"_face.png",img)
#         cv2.destroyAllWindows()
print("Recognizing faces and generating results")
sfr = SimpleFacerec()
sfr.load_encoding_images("face_library/")
# cap = cv2.VideoCapture(0)
# print("HR/"+file)
img = cv2.imread("jeff_side_face.png")
face_locations, face_names = sfr.detect_known_faces(img)
for face_loc, name in zip(face_locations, face_names):
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    cv2.putText(img, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 200), 4)
cv2.imwrite("results/jeff_face.png",img)
cv2.destroyAllWindows()

