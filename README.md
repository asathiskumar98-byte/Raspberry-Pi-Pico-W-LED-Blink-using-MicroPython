# 💡 Raspberry Pi Pico W – LED Blink using MicroPython

A simple MicroPython project that blinks the onboard or external LED on the **Raspberry Pi Pico W**, created using **Thonny IDE**.

---

## 🧰 Requirements
- Raspberry Pi Pico W
- MicroPython firmware flashed
- Thonny IDE (latest version)
- USB cable (Data-enabled)

---

## ⚙️ Setup Instructions
1. Open **Thonny IDE**
2. Select interpreter:
   - `Run → Select Interpreter → MicroPython (Raspberry Pi Pico)`
3. Connect your Pico W via USB
4. Save the script as `main.py` **directly onto the Pico**
5. Run it → the onboard LED should blink every 0.1 seconds ✨

---

## 🧩 Code Breakdown
- `machine.Pin("LED", machine.Pin.OUT)` → Initializes the onboard LED pin.
- `led.toggle()` → Flips the LED state.
- `time.sleep(0.1)` → Adds a short delay (100 ms).

---

## 🔧 Customization
| Action | Change |
|--------|---------|
| Slow blink | `time.sleep(0.5)` |
| Fast blink | `time.sleep(0.05)` |
| External LED | Replace `"LED"` with GPIO number (e.g., `15`) |

---

## 🧱 Project Ideas to Extend
- Breathing LED using PWM brightness control  
- Wi-Fi-controlled LED (use `network` module)  
- Blink pattern to indicate Wi-Fi connection status  
