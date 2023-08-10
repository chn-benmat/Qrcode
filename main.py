import cv2
from pyzbar.pyzbar import decode

# Load image from path
image_path = 'image/All_Qr8.jpg'
image = cv2.imread(image_path)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a list of QR code names and corresponding data
qr_names = ['Qr A', 'Qr B', 'Qr C']
qr_data_list = ['data_for_Qr_A', 'data_for_Qr_B', 'data_for_Qr_C']

# Detect and decode QR codes in the image
decoded_objects = decode(gray_image)

for obj in decoded_objects:
    qr_data = obj.data.decode('utf-8')  # Extract QR code data
    qr_name = qr_names[0]  # Default QR name
    
    # Iterate through each QR code name to check for a match
    for i in range(len(qr_names)):
        if qr_data == qr_data_list[i]:
            qr_name = qr_names[i]
            break   
    
    # Draw bounding box around the QR code on the image with green color (RGB format)
    qr_points = obj.polygon
    for j in range(4):
        cv2.line(image, tuple(qr_points[j]), tuple(qr_points[(j+1) % 4]), (0, 255, 0), 3)  # Change color to green
    
    # Print the decoded content from the QR code along with the QR name
    print(f"QR Code content: {qr_data}")
    print(f"QR Code name: {qr_name}")
    
    # Draw the QR code name as text on the image
    text_x = qr_points[0].x  # X-coordinate of the text
    text_y = qr_points[3].y + 20  # Y-coordinate of the text (below the QR code)
    cv2.putText(image, qr_name, (int(text_x), int(text_y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with bounding boxes and QR code names
cv2.imshow("Detected QR Codes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()