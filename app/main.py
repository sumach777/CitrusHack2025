from gui import AudioApp
from audioprocessing import AudioProcessor

def main():
    app = AudioApp()
    root = app.create_window()
    
    processor = AudioProcessor(app)
    app.set_processor(processor)
    processor.process_audio()
    
    root.mainloop()

if __name__ == "__main__":
    main()