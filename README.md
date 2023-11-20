# c-dialect-builder
A silly, overengineered project that allows users to alter keywords and syntax to produce code that compiles 1:1 to C

Current usage:
- Install GCC, instructions can be found here: [Link](https://gcc.gnu.org/install/)
- Clone repo
- Open main.py in your preferred editor
- Edit the dictionary to swap keywords and add a custom file extension
- Write some code in your new language
- Run `python main.py your_file_name.your_file_extension`
- If you have programmed correctly, and have gcc installed, the program will compile to a `.c` file and an executable
- Run your executable by typing `./your_file_name` into your preferred terminal
