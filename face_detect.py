import face_recognition
import sys

image = face_recognition.load_image_file(sys.argv[1])
face_locations = face_recognition.face_locations(image)

#print(sys.argv[1])
print(face_locations)