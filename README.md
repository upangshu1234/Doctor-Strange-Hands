Here's a summary of your project for your GitHub repository:  

---

# **Doctor Strange Magic Circle Effect using OpenCV & MediaPipe**  

This project uses **OpenCV** and **MediaPipe** to create a real-time Doctor Strange-inspired magic circle effect using hand tracking. It captures hand landmarks, calculates distances between fingers, and overlays spinning magic circles when the user forms a specific hand gesture.  

## **Libraries Used**  
To run this project, install the following dependencies:  

```bash
pip install opencv-python mediapipe numpy
```

## **How It Works**  
1. **Hand Tracking:** Uses MediaPipe to track hand landmarks in real time.  
2. **Gesture Detection:** Calculates the ratio of the index fingertip and pinky fingertip distance to the wrist-index MCP distance.  
3. **Magic Effect Activation:**  
   - If the ratio is between `0.5 and 1.3`, lines are drawn between key hand points.  
   - If the ratio is greater than `1.3`, the magic circle effect appears at the middle finger MCP position.  
4. **Rotating Magic Circles:** Two transparent PNG images (clockwise and counterclockwise magic circles) are overlaid and rotated dynamically.  
5. **Camera Feed Processing:** The program captures real-time video, processes frames, and renders the augmented effect.  

## **Key Features**  
✅ **Real-time Hand Tracking** using MediaPipe  
✅ **Dynamic Gesture Recognition** to trigger effects  
✅ **Transparent Magic Circles** overlay using OpenCV  
✅ **Rotating Effects** for an animated visual  

## **How to Run**  
1. Clone the repository:  
   ```bash
   git clone (https://github.com/upangshu1234/Doctor-Strange-Hands)
   cd Doctor-Strange-Hands
   ```
2. Place `magic_circle_ccw.png` and `magic_circle_cw.png` inside a `magic_circles/` folder.  
3. Run the script:  
   ```bash
   main.py
   ```
4. Press **'q'** to exit.  
 

## **Future Improvements**  
- Improve gesture recognition for more precise control.  
- Add multi-hand support for dual magic circles.  
- Enhance visual effects with OpenCV filters.  

---

Let me know if you need any modifications! 🚀
