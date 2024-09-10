# Virtual Hand Gesture Calculator

This project demonstrates a virtual calculator controlled by hand gestures, utilizing a webcam to detect hand movements. It makes use of **OpenCV** for image processing and **cvzone** for hand tracking, providing an interactive and touch-free calculator experience.

## Features

- **Hand Tracking**: Detects hand gestures using the webcam and recognizes when fingers "press" buttons on the virtual calculator.
- **Basic Operations**: Supports arithmetic operations like addition, subtraction, multiplication, and division.
- **Real-time Interaction**: Displays buttons and the result of the operations dynamically on the screen.

## How It Works

- The **OpenCV** library captures frames from the webcam and flips them horizontally for a mirror effect.
- **cvzone's HandTrackingModule** is used to detect and track hand gestures. The index and middle finger positions are specifically monitored.
- A virtual keypad with numbers and operators is drawn on the screen. When the distance between the index and middle finger becomes small, it is considered a "click."
- Upon detecting a click on a button, the calculator appends the respective number or operator to the equation, or evaluates the expression when the "=" button is clicked.
  
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/virtual-hand-gesture-calculator.git
   cd virtual-hand-gesture-calculator
   ```

2. Install required dependencies:
   ```bash
   pip install opencv-python cvzone
   ```

3. Run the script:
   ```bash
   python hand_calculator.py
   ```

## Usage

- Place your hand in front of the webcam, and it will be detected automatically.
- To "press" a button, pinch your index and middle fingers together when they are over the desired button.
- Perform basic calculations and see the result in real-time.
- Press the 'C' key to clear the current equation and start over.
- Press 'Q' to quit the application.

## Requirements

- Python 3.x
- OpenCV
- cvzone (for hand tracking)

## Screenshots

![Calculator Interface](path/to/screenshot.png)

## Future Improvements

- Enhance gesture recognition for more complex operations.
- Add support for advanced mathematical functions (e.g., square root, exponentiation).
- Implement a more visually appealing UI.
