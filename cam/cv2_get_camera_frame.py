import cv2

def initialize_camera():
    """Initializes the camera and sets properties."""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Camera not found!")
        exit(0)
    
    # Set frame dimensions
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
    
    return cap

def capture_loop(cap):
    """Main loop to capture video and handle user input."""
    img_count = 0

    while True:
        # Capture frame
        ret, frame = cap.read()

        # If frame not captured, exit loop
        if not ret:
            print("Error: Cannot capture image.")
            break

        # Display frame
        cv2.imshow('image_win', frame)

        # Check for user input
        key = cv2.waitKey(1)
        
        # Exit on 'q' press
        if key == ord('q'):
            print("Exiting program.")
            break
        
        # Save image on 'c' press
        elif key == ord('c'):
            img_name = f"{img_count}.png"
            cv2.imwrite(img_name, frame)
            print(f"Image saved as: {img_name}")
            img_count += 1

def main():
    # Create display window with properties
    cv2.namedWindow('image_win', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

    # Initialize the camera
    cap = initialize_camera()

    # Start capture loop
    capture_loop(cap)

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
