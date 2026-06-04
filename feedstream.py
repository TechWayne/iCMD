#File request test for Imports
import cv2

# Initialize system hardware camera feed stream
camera = cv2.VideoCapture(0)

while True:
    active, frame = camera.read()
    if not active: break

    # Convert the mirrored webcam live feed into a stylized neon-cyber wireframe
    matrix_edges = cv2.Canny(cv2.flip(frame, 1), 60, 130)
    cyber_neon_frame = cv2.merge([matrix_edges, matrix_edges, matrix_edges * 0]) # Cyan Matrix Tint

    cv2.imshow("⚡ iCMD Core — Real-Time Neon Vision Engine", cyber_neon_frame)
    if cv2.waitKey(1) == 27: break # Press 'ESC' to instantly kill the video pipeline

camera.release()
cv2.destroyAllWindows()
