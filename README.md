# LibreVine

![Logo](https://github.com/blackletum/LibreVine/blob/main/images/template-removebg-preview.png?raw=true)

Welcome to **LibreVine**, a horrific Python program designed to open multiple user-defined websites at random or static intervals. 

Within this repository, you’ll find three folders:

- **code**: Contains the `.py` file for LibreVine. Feel free to review or modify the source code instead of running the executable.
- **images**: Includes the original image files for the program icon and the `.ico` file used in the executable.
- **program**: Contains all the files required to run the program, including the compiled `.exe`.

## How to Use

The LibreVine executable is located in the **`program`** folder. Inside the **`input`** folder, you’ll find three important configuration files:  

- **`browser.txt`**: Define the full path to the browser you want to use.

  Example:  

  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

- **`randominterval.txt`**: Specify up to 5 whole numbers (one per line) representing the intervals (in seconds) for opening websites. If no numbers are specified, the program defaults to a random interval between 5–10 seconds.

  Example:  

  - 5
  - 10
  - 15

- **`websites.txt`**: List the websites to be opened, one per line. Use the format `github.com` instead of including the protocol (`https://` or `www.`).

  Example:  

  - github.com
  - example.com
  - stackoverflow.com


## Special Thanks

A big shout-out to the following tools, inspirations, and resources that helped bring LibreVine to life:  

- **[DeepAI](https://deepai.org/)**: Used to create the program's icon.  
- **[Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe)**: Made it easy to convert the Python code into an executable file.  
- **[Spam Website Opener](https://github.com/shankypedia/Spam-Website-Opener)**: Served as inspiration and a starting point for this project.  
- **[ChatGPT](https://chatgpt.com/)**: Provided valuable assistance during development.  
- **[Phind](https://www.phind.com/)**: Helped troubleshoot and refine the code.  
- **[CloudConvert](https://cloudconvert.com/)**: Used to convert the program icon from `.png` to `.ico`.  
- **[Remove BG](https://www.remove.bg/)**: Removed the background from the program's icon file.  

Enjoy using LibreVine! Feel free to contribute or suggest improvements.
