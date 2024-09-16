# Korean Quiz Simulator

The Korean Quiz Simulator utilizes Google's Text-to-Speech API to create an interactive quiz that reads out a list of Korean words and provides their definitions. This is a terminal-based application, so ensure you have a Python environment set up, such as Anaconda, to use the required libraries.

## Features

- **Text-to-Speech**: Reads out Korean vocabulary words using Google's Text-to-Speech API.
- **Definitions**: Provides definitions of the words after they are read.
- **Terminal-Based**: Operates via the terminal, making it easy to run and use.

## Sample Vocab List

To test the simulator, use a vocab list in the following format:
아메리카노 Americano 오늘 today 카페라떼 Cafe Latte 주다 to give 그러세요 Please do so 그럼 then 다음에 next time 마실래요? would you like to drink? 먹을래요? would you like to eat? 아녜요 no 그제 the day before yesterday 어제 yesterday 모레 the day after tomorrow 노래방 karaoke 중국 식당 Chinese restaurant 샐러드 salad 맥도날드 McDonald’s 볼펜 ballpoint pen

## Getting Started

1. **Install Dependencies**: Ensure you have Python installed. Install the required libraries using pip:

    ```bash
    pip install gtts
    ```

    You may also need to install `playsound` for audio playback:

    ```bash
    pip install playsound
    ```

2. **Run the Simulator**: In your terminal, navigate to the directory containing the `korean_quiz_simulator.py` file and run:

    ```bash
    python korean_quiz_simulator.py
    ```

3. **Follow Instructions**: Follow the instructions displayed in the terminal. You will be prompted to input a vocab list or use the sample list provided.

## Usage

Simply run the `korean_quiz_simulator()` function in your terminal, follow the instructions displayed, and copy and paste the vocab list if you want to test the simulator. Enjoy!
