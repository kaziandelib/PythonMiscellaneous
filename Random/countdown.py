import winsound  # For playing beep sounds on Windows
import time      # For time-related functions like sleep

def alarms():
    # Play a beep sequence 4 times:
    # Beep at 2000 Hz for 500 ms, then at 4000 Hz for 250 ms
    for repeats in range(4):
        winsound.Beep(2000, 500)
        winsound.Beep(4000, 250)

def countdown_timer():
    # Ask the user for the countdown duration in seconds
    timer_duration = int(input("Enter duration in seconds: "))
    
    # Initialize time counters
    hours, minutes, seconds = 0, 0, 0

    # Loop once per second for the total timer duration
    for i in range(timer_duration):
        print('\n' * 120)  # Clear console by printing many new lines

        # Increment seconds counter
        seconds += 1
        
        # Convert seconds to minutes and minutes to hours accordingly
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0

        # Display the current elapsed time in HH:MM:SS format
        print(f"{hours} : {minutes} : {seconds}")
        
        # Wait for 1 second before continuing the loop
        time.sleep(1)
    
    # Once countdown ends, play alarm sounds
    alarms()

if __name__ == '__main__':
    # Run the countdown timer if this script is executed directly
    countdown_timer()
