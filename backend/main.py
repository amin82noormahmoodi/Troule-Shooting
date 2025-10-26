from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Hardcoded Data
HARDCODED_DATA = {
    "boards": [
        {"id": 1, "name": "Arduino Uno"},
        {"id": 2, "name": "Raspberry Pi 4"},
        {"id": 3, "name": "ESP32 Development Board"},
        {"id": 4, "name": "STM32 Nucleo"},
        {"id": 5, "name": "Arduino Mega"},
    ],
    "problems": [
        # Arduino Uno problems
        {"id": 1, "board_id": 1, "problem_text": "Board not detected by computer"},
        {"id": 2, "board_id": 1, "problem_text": "LED not blinking in basic blink program"},
        {"id": 3, "board_id": 1, "problem_text": "Serial communication not working"},
        {"id": 4, "board_id": 1, "problem_text": "Power supply issues - board not turning on"},
        
        # Raspberry Pi 4 problems
        {"id": 5, "board_id": 2, "problem_text": "Pi not booting - red LED only"},
        {"id": 6, "board_id": 2, "problem_text": "WiFi connection issues"},
        {"id": 7, "board_id": 2, "problem_text": "GPIO pins not responding"},
        {"id": 8, "board_id": 2, "problem_text": "Overheating and thermal throttling"},
        
        # ESP32 problems
        {"id": 9, "board_id": 3, "problem_text": "WiFi connection drops frequently"},
        {"id": 10, "board_id": 3, "problem_text": "Bluetooth not working"},
        {"id": 11, "board_id": 3, "problem_text": "Deep sleep mode not functioning"},
        {"id": 12, "board_id": 3, "problem_text": "ADC readings inaccurate"},
        
        # STM32 problems
        {"id": 13, "board_id": 4, "problem_text": "Debugger connection issues"},
        {"id": 14, "board_id": 4, "problem_text": "Clock configuration problems"},
        {"id": 15, "board_id": 4, "problem_text": "UART communication errors"},
        {"id": 16, "board_id": 4, "problem_text": "ADC calibration issues"},
        
        # Arduino Mega problems
        {"id": 17, "board_id": 5, "problem_text": "Multiple serial ports not working"},
        {"id": 18, "board_id": 5, "problem_text": "Memory issues with large programs"},
        {"id": 19, "board_id": 5, "problem_text": "PWM output problems"},
        {"id": 20, "board_id": 5, "problem_text": "Interrupt handling issues"},
    ],
    "solutions": [
        # Solutions for Arduino Uno problems
        {"id": 1, "problem_id": 1, "solution_text": "Check USB cable connection and try a different USB port. Install proper drivers for your operating system."},
        {"id": 2, "problem_id": 1, "solution_text": "Verify the board is selected correctly in Arduino IDE (Tools > Board > Arduino Uno)."},
        {"id": 3, "problem_id": 1, "solution_text": "Try pressing the reset button on the board while connecting to computer."},
        
        {"id": 4, "problem_id": 2, "solution_text": "Verify the LED is connected to pin 13 and ground. Check the LED polarity."},
        {"id": 5, "problem_id": 2, "solution_text": "Upload the basic blink example from File > Examples > 01.Basics > Blink."},
        {"id": 6, "problem_id": 2, "solution_text": "Check if the board is properly powered and the program uploaded successfully."},
        
        {"id": 7, "problem_id": 3, "solution_text": "Verify the correct COM port is selected in Arduino IDE."},
        {"id": 8, "problem_id": 3, "solution_text": "Check baud rate settings - ensure both code and Serial Monitor use same baud rate."},
        {"id": 9, "problem_id": 3, "solution_text": "Try different USB cable or USB port. Some cables are charge-only."},
        
        {"id": 10, "problem_id": 4, "solution_text": "Check power supply voltage - should be 5V for Arduino Uno."},
        {"id": 11, "problem_id": 4, "solution_text": "Verify the power LED is on. If not, check power connections."},
        {"id": 12, "problem_id": 4, "solution_text": "Try powering via USB and external power supply simultaneously."},
        
        # Solutions for Raspberry Pi 4 problems
        {"id": 13, "problem_id": 5, "solution_text": "Check SD card - ensure it's properly inserted and not corrupted."},
        {"id": 14, "problem_id": 5, "solution_text": "Try flashing a fresh OS image to the SD card."},
        {"id": 15, "problem_id": 5, "solution_text": "Verify power supply provides adequate current (3A recommended for Pi 4)."},
        
        {"id": 16, "problem_id": 6, "solution_text": "Check WiFi credentials and network availability."},
        {"id": 17, "problem_id": 6, "solution_text": "Try connecting via Ethernet cable first to verify internet connectivity."},
        {"id": 18, "problem_id": 6, "solution_text": "Update system packages: sudo apt update && sudo apt upgrade"},
        
        {"id": 19, "problem_id": 7, "solution_text": "Enable GPIO in raspi-config: sudo raspi-config > Interface Options > GPIO."},
        {"id": 20, "problem_id": 7, "solution_text": "Check pin numbering - use BCM numbering in your code."},
        {"id": 21, "problem_id": 7, "solution_text": "Verify proper pull-up/pull-down resistor configuration."},
        
        {"id": 22, "problem_id": 8, "solution_text": "Install heatsink and fan for active cooling."},
        {"id": 23, "problem_id": 8, "solution_text": "Check CPU temperature: vcgencmd measure_temp"},
        {"id": 24, "problem_id": 8, "solution_text": "Reduce CPU frequency or disable unnecessary services."},
        
        # Solutions for ESP32 problems
        {"id": 25, "problem_id": 9, "solution_text": "Check WiFi signal strength and move closer to router."},
        {"id": 26, "problem_id": 9, "solution_text": "Update ESP32 firmware to latest version."},
        {"id": 27, "problem_id": 9, "solution_text": "Implement WiFi reconnection logic in your code."},
        
        {"id": 28, "problem_id": 10, "solution_text": "Enable Bluetooth in ESP32 configuration."},
        {"id": 29, "problem_id": 10, "solution_text": "Check Bluetooth library compatibility with your ESP32 board."},
        {"id": 30, "problem_id": 10, "solution_text": "Verify Bluetooth antenna is not blocked by metal components."},
        
        {"id": 31, "problem_id": 11, "solution_text": "Configure deep sleep properly with wake-up sources."},
        {"id": 32, "problem_id": 11, "solution_text": "Check power consumption during sleep mode."},
        {"id": 33, "problem_id": 11, "solution_text": "Verify RTC is working correctly for wake-up timing."},
        
        {"id": 34, "problem_id": 12, "solution_text": "Calibrate ADC reference voltage."},
        {"id": 35, "problem_id": 12, "solution_text": "Use external voltage reference for better accuracy."},
        {"id": 36, "problem_id": 12, "solution_text": "Check for electrical noise in analog input circuit."},
        
        # Solutions for STM32 problems
        {"id": 37, "problem_id": 13, "solution_text": "Install ST-Link drivers and software."},
        {"id": 38, "problem_id": 13, "solution_text": "Check debugger connection cables and pins."},
        {"id": 39, "problem_id": 13, "solution_text": "Verify debugger settings in IDE (SWD mode, correct target)."},
        
        {"id": 40, "problem_id": 14, "solution_text": "Configure system clock using STM32CubeMX."},
        {"id": 41, "problem_id": 14, "solution_text": "Check crystal oscillator connections and values."},
        {"id": 42, "problem_id": 14, "solution_text": "Verify PLL settings for desired clock frequency."},
        
        {"id": 43, "problem_id": 15, "solution_text": "Check UART pin configuration and baud rate settings."},
        {"id": 44, "problem_id": 15, "solution_text": "Verify UART peripheral is enabled in clock configuration."},
        {"id": 45, "problem_id": 15, "solution_text": "Check for pin conflicts with other peripherals."},
        
        {"id": 46, "problem_id": 16, "solution_text": "Perform ADC calibration sequence on startup."},
        {"id": 47, "problem_id": 16, "solution_text": "Check reference voltage stability and filtering."},
        {"id": 48, "problem_id": 16, "solution_text": "Use oversampling for improved ADC accuracy."},
        
        # Solutions for Arduino Mega problems
        {"id": 49, "problem_id": 17, "solution_text": "Use Serial1, Serial2, Serial3 for additional UART ports."},
        {"id": 50, "problem_id": 17, "solution_text": "Check baud rate configuration for each serial port."},
        {"id": 51, "problem_id": 17, "solution_text": "Verify proper pin connections for each UART."},
        
        {"id": 52, "problem_id": 18, "solution_text": "Optimize code to reduce memory usage."},
        {"id": 53, "problem_id": 18, "solution_text": "Use PROGMEM for storing constant data in flash memory."},
        {"id": 54, "problem_id": 18, "solution_text": "Consider using external memory modules if needed."},
        
        {"id": 55, "problem_id": 19, "solution_text": "Check PWM frequency settings and duty cycle calculations."},
        {"id": 56, "problem_id": 19, "solution_text": "Verify PWM pins are correctly configured."},
        {"id": 57, "problem_id": 19, "solution_text": "Use analogWrite() function for PWM output."},
        
        {"id": 58, "problem_id": 20, "solution_text": "Configure interrupt service routines (ISR) properly."},
        {"id": 59, "problem_id": 20, "solution_text": "Use attachInterrupt() function for external interrupts."},
        {"id": 60, "problem_id": 20, "solution_text": "Keep ISR functions short and avoid delay() calls."},
    ]
}

# Pydantic models
class BoardResponse(BaseModel):
    id: int
    name: str

class ProblemResponse(BaseModel):
    id: int
    board_id: int
    problem_text: str

class SolutionResponse(BaseModel):
    id: int
    problem_id: int
    solution_text: str

# FastAPI app
app = FastAPI(title="Board Troubleshooting API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
@app.get("/")
async def root():
    return {"message": "Board Troubleshooting API is running"}

@app.get("/boards", response_model=List[BoardResponse])
async def get_boards():
    """Get all boards"""
    return HARDCODED_DATA["boards"]

@app.get("/problems/{board_id}", response_model=List[ProblemResponse])
async def get_problems(board_id: int):
    """Get all problems for a specific board"""
    # Check if board exists
    board_exists = any(board["id"] == board_id for board in HARDCODED_DATA["boards"])
    if not board_exists:
        raise HTTPException(status_code=404, detail="Board not found")
    
    # Filter problems by board_id
    problems = [problem for problem in HARDCODED_DATA["problems"] if problem["board_id"] == board_id]
    return problems

@app.get("/solutions/{problem_id}", response_model=List[SolutionResponse])
async def get_solutions(problem_id: int):
    """Get all solutions for a specific problem"""
    # Check if problem exists
    problem_exists = any(problem["id"] == problem_id for problem in HARDCODED_DATA["problems"])
    if not problem_exists:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    # Filter solutions by problem_id
    solutions = [solution for solution in HARDCODED_DATA["solutions"] if solution["problem_id"] == problem_id]
    return solutions

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
