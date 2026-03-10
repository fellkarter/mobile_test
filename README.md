# Focus Breeze

This lightweight mobile-style experience uses Kivy to deliver a calming focus dashboard. The entry screen highlights a randomized status, a prompt, and a check-in card that updates every time you tap **Refresh focus**.

## Run

1. Create or activate a Python virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the app:
   ```
   python main.py
   ```

The layout is responsive to portrait-sized windows, so you can test it in desktop mode or deploy the same code to Kivy-friendly mobile targets.

## Build an Android APK via GitHub Actions

1. Push this repo to GitHub (public repositories get unlimited free minutes for Actions).
2. Ensure `buildozer.spec` stays next to `main.py` (already included) and then either push to `main` or run the **Build Android APK** workflow manually from the GitHub UI.
3. After the workflow finishes, download `focusbreeze-apk` from the workflow’s artifacts; it contains the generated `.apk`.
