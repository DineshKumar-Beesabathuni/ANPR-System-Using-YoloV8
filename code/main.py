import os

def run_detect_images():
    os.system('python detect_images.py')

def run_detect_video():
    os.system('python detect_video.py')

def run_detect_camera():
    os.system('python detect_camera.py')

def main():
    while True:
        print("Select an option to run:")
        print("1. Detect Images")
        print("2. Detect Video")
        print("3. Detect Camera")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            run_detect_images()
        elif choice == '2':
            run_detect_video()
        elif choice == '3':
            run_detect_camera()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()