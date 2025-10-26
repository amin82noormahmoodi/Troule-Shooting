#!/usr/bin/env python3
"""
Sample data script for Board Troubleshooting Platform
Run this script to populate the database with sample data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Board, Problem, Solution

# Database configuration
DATABASE_URL = "postgresql://postgres:amin1382@localhost/saffar"

def create_sample_data():
    # Create database engine
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create session
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(Solution).delete()
        db.query(Problem).delete()
        db.query(Board).delete()
        db.commit()
        
        # Create sample boards
        boards_data = [
            {"name": "Arduino Uno"},
            {"name": "Raspberry Pi 4"},
            {"name": "ESP32 Development Board"},
            {"name": "STM32 Nucleo"},
            {"name": "Arduino Mega"},
        ]
        
        boards = []
        for board_data in boards_data:
            board = Board(**board_data)
            db.add(board)
            boards.append(board)
        
        db.commit()
        
        # Create sample problems for each board
        problems_data = [
            # Arduino Uno problems
            {"board_id": 1, "problem_text": "Board not detected by computer"},
            {"board_id": 1, "problem_text": "LED not blinking in basic blink program"},
            {"board_id": 1, "problem_text": "Serial communication not working"},
            {"board_id": 1, "problem_text": "Power supply issues - board not turning on"},
            
            # Raspberry Pi 4 problems
            {"board_id": 2, "problem_text": "Pi not booting - red LED only"},
            {"board_id": 2, "problem_text": "WiFi connection issues"},
            {"board_id": 2, "problem_text": "GPIO pins not responding"},
            {"board_id": 2, "problem_text": "Overheating and thermal throttling"},
            
            # ESP32 problems
            {"board_id": 3, "problem_text": "WiFi connection drops frequently"},
            {"board_id": 3, "problem_text": "Bluetooth not working"},
            {"board_id": 3, "problem_text": "Deep sleep mode not functioning"},
            {"board_id": 3, "problem_text": "ADC readings inaccurate"},
            
            # STM32 problems
            {"board_id": 4, "problem_text": "Debugger connection issues"},
            {"board_id": 4, "problem_text": "Clock configuration problems"},
            {"board_id": 4, "problem_text": "UART communication errors"},
            {"board_id": 4, "problem_text": "ADC calibration issues"},
            
            # Arduino Mega problems
            {"board_id": 5, "problem_text": "Multiple serial ports not working"},
            {"board_id": 5, "problem_text": "Memory issues with large programs"},
            {"board_id": 5, "problem_text": "PWM output problems"},
            {"board_id": 5, "problem_text": "Interrupt handling issues"},
        ]
        
        problems = []
        for problem_data in problems_data:
            problem = Problem(**problem_data)
            db.add(problem)
            problems.append(problem)
        
        db.commit()
        
        # Create sample solutions for each problem
        solutions_data = [
            # Solutions for Arduino Uno problems
            {"problem_id": 1, "solution_text": "Check USB cable connection and try a different USB port. Install proper drivers for your operating system."},
            {"problem_id": 1, "solution_text": "Verify the board is selected correctly in Arduino IDE (Tools > Board > Arduino Uno)."},
            {"problem_id": 1, "solution_text": "Try pressing the reset button on the board while connecting to computer."},
            
            {"problem_id": 2, "solution_text": "Verify the LED is connected to pin 13 and ground. Check the LED polarity."},
            {"problem_id": 2, "solution_text": "Upload the basic blink example from File > Examples > 01.Basics > Blink."},
            {"problem_id": 2, "solution_text": "Check if the board is properly powered and the program uploaded successfully."},
            
            {"problem_id": 3, "solution_text": "Verify the correct COM port is selected in Arduino IDE."},
            {"problem_id": 3, "solution_text": "Check baud rate settings - ensure both code and Serial Monitor use same baud rate."},
            {"problem_id": 3, "solution_text": "Try different USB cable or USB port. Some cables are charge-only."},
            
            {"problem_id": 4, "solution_text": "Check power supply voltage - should be 5V for Arduino Uno."},
            {"problem_id": 4, "solution_text": "Verify the power LED is on. If not, check power connections."},
            {"problem_id": 4, "solution_text": "Try powering via USB and external power supply simultaneously."},
            
            # Solutions for Raspberry Pi 4 problems
            {"problem_id": 5, "solution_text": "Check SD card - ensure it's properly inserted and not corrupted."},
            {"problem_id": 5, "solution_text": "Try flashing a fresh OS image to the SD card."},
            {"problem_id": 5, "solution_text": "Verify power supply provides adequate current (3A recommended for Pi 4)."},
            
            {"problem_id": 6, "solution_text": "Check WiFi credentials and network availability."},
            {"problem_id": 6, "solution_text": "Try connecting via Ethernet cable first to verify internet connectivity."},
            {"problem_id": 6, "solution_text": "Update system packages: sudo apt update && sudo apt upgrade"},
            
            {"problem_id": 7, "solution_text": "Enable GPIO in raspi-config: sudo raspi-config > Interface Options > GPIO."},
            {"problem_id": 7, "solution_text": "Check pin numbering - use BCM numbering in your code."},
            {"problem_id": 7, "solution_text": "Verify proper pull-up/pull-down resistor configuration."},
            
            {"problem_id": 8, "solution_text": "Install heatsink and fan for active cooling."},
            {"problem_id": 8, "solution_text": "Check CPU temperature: vcgencmd measure_temp"},
            {"problem_id": 8, "solution_text": "Reduce CPU frequency or disable unnecessary services."},
            
            # Solutions for ESP32 problems
            {"problem_id": 9, "solution_text": "Check WiFi signal strength and move closer to router."},
            {"problem_id": 9, "solution_text": "Update ESP32 firmware to latest version."},
            {"problem_id": 9, "solution_text": "Implement WiFi reconnection logic in your code."},
            
            {"problem_id": 10, "solution_text": "Enable Bluetooth in ESP32 configuration."},
            {"problem_id": 10, "solution_text": "Check Bluetooth library compatibility with your ESP32 board."},
            {"problem_id": 10, "solution_text": "Verify Bluetooth antenna is not blocked by metal components."},
            
            {"problem_id": 11, "solution_text": "Configure deep sleep properly with wake-up sources."},
            {"problem_id": 11, "solution_text": "Check power consumption during sleep mode."},
            {"problem_id": 11, "solution_text": "Verify RTC is working correctly for wake-up timing."},
            
            {"problem_id": 12, "solution_text": "Calibrate ADC reference voltage."},
            {"problem_id": 12, "solution_text": "Use external voltage reference for better accuracy."},
            {"problem_id": 12, "solution_text": "Check for electrical noise in analog input circuit."},
            
            # Solutions for STM32 problems
            {"problem_id": 13, "solution_text": "Install ST-Link drivers and software."},
            {"problem_id": 13, "solution_text": "Check debugger connection cables and pins."},
            {"problem_id": 13, "solution_text": "Verify debugger settings in IDE (SWD mode, correct target)."},
            
            {"problem_id": 14, "solution_text": "Configure system clock using STM32CubeMX."},
            {"problem_id": 14, "solution_text": "Check crystal oscillator connections and values."},
            {"problem_id": 14, "solution_text": "Verify PLL settings for desired clock frequency."},
            
            {"problem_id": 15, "solution_text": "Check UART pin configuration and baud rate settings."},
            {"problem_id": 15, "solution_text": "Verify UART peripheral is enabled in clock configuration."},
            {"problem_id": 15, "solution_text": "Check for pin conflicts with other peripherals."},
            
            {"problem_id": 16, "solution_text": "Perform ADC calibration sequence on startup."},
            {"problem_id": 16, "solution_text": "Check reference voltage stability and filtering."},
            {"problem_id": 16, "solution_text": "Use oversampling for improved ADC accuracy."},
            
            # Solutions for Arduino Mega problems
            {"problem_id": 17, "solution_text": "Use Serial1, Serial2, Serial3 for additional UART ports."},
            {"problem_id": 17, "solution_text": "Check baud rate configuration for each serial port."},
            {"problem_id": 17, "solution_text": "Verify proper pin connections for each UART."},
            
            {"problem_id": 18, "solution_text": "Optimize code to reduce memory usage."},
            {"problem_id": 18, "solution_text": "Use PROGMEM for storing constant data in flash memory."},
            {"problem_id": 18, "solution_text": "Consider using external memory modules if needed."},
            
            {"problem_id": 19, "solution_text": "Check PWM frequency settings and duty cycle calculations."},
            {"problem_id": 19, "solution_text": "Verify PWM pins are correctly configured."},
            {"problem_id": 19, "solution_text": "Use analogWrite() function for PWM output."},
            
            {"problem_id": 20, "solution_text": "Configure interrupt service routines (ISR) properly."},
            {"problem_id": 20, "solution_text": "Use attachInterrupt() function for external interrupts."},
            {"problem_id": 20, "solution_text": "Keep ISR functions short and avoid delay() calls."},
        ]
        
        for solution_data in solutions_data:
            solution = Solution(**solution_data)
            db.add(solution)
        
        db.commit()
        
        print("✅ Sample data created successfully!")
        print(f"📊 Created {len(boards)} boards, {len(problems)} problems, and {len(solutions_data)} solutions")
        
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
