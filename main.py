import webvtt
import os
import tkinter as tk
from tkinter import filedialog

def vtt_to_srt_time(vtt_time):
    """Convert VTT time format to SRT time format."""
    return vtt_time.replace('.', ',')

def main():
    # Create a Tkinter root window, but keep it hidden
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to select the target directory
    target_directory = filedialog.askdirectory(title="Select the Target Directory")
    
    if not target_directory:
        print("No directory selected. Exiting.")
        return

    # Loop through all .vtt files in the selected directory
    for filename in os.listdir(target_directory):
        if filename.endswith('.vtt'):
            input_file_vtt = os.path.join(target_directory, filename)
            output_file_srt = os.path.splitext(input_file_vtt)[0] + '.srt'  # Change extension to .srt
            
            # Convert .vtt to .srt
            try:
                # Load the .vtt file
                vtt = webvtt.read(input_file_vtt)
                
                # Write .srt file
                with open(output_file_srt, 'w') as srt_file:
                    for index, caption in enumerate(vtt):
                        start_time = vtt_to_srt_time(caption.start)
                        end_time = vtt_to_srt_time(caption.end)
                        srt_file.write(f"{index + 1}\n")
                        srt_file.write(f"{start_time} --> {end_time}\n")
                        srt_file.write(f"{caption.text}\n\n")
                
                print(f"Converted: {input_file_vtt} to {output_file_srt}")

            except Exception as e:
                print(f"An error occurred while converting {input_file_vtt}: {e}")

if __name__ == "__main__":
    main()
