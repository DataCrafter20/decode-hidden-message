# 🔐 Decoding a Secret Message from a Google Doc

This project solves a coding exercise where the goal is to decode a visual message hidden in a grid of Unicode characters and coordinates retrieved from a Google Docs URL.

## 🧩 Problem Description

You are provided with a Google Doc containing lines that each specify:
- A Unicode character,
- Its `x` and `y` grid coordinates.

Your task is to write a Python function that:
1. Downloads and parses the data,
2. Builds a character grid based on the coordinates,
3. Prints out the message formed when the grid is rendered in a fixed-width font.

Empty grid positions are filled with spaces. The grid size is determined dynamically based on the largest `x` and `y` coordinates.

### 📝 Assumptions
- All characters follow the format: `<CHARACTER><X><Y>`, such as `A23`.
- Coordinates start from (0, 0).
- The document format remains consistent.

---

## 🚀 How It Works

### Main Function: `message_decoder(url)`
1. Downloads the text content from the provided URL using the `requests` library.
2. Uses regular expressions to extract all matching character-coordinate patterns.
3. Determines the grid size based on the maximum `x` and `y` values.
4. Initializes an empty 2D grid filled with spaces.
5. Populates the grid with characters at their respective coordinates.
6. Converts the grid into a printable message.

### Optional Helper: `clean_message(decoded_msg)`
This helper extracts and prints only **uppercase letters** from the decoded grid to highlight the hidden message.

---

## 🧪 Example Usage

```bash
$ python message_decoder.py
Enter or copy and paste the URL: https://docs.google.com/document/d/your-example-id
decoded message:
F    
F    
FFF  
F    
F    

F
F
F
F
F
````

## 📂 Files

- `message_decoder.py`: Contains the complete Python code.
- `README.md`: This file.

---

## 💻 Technologies Used

- Python 3.x
- `requests` library
- `re` module (regular expressions)

---

## 📦 Installation

```bash
Download the python script and open it into your prefered compiler or notebook but colab is recommended because the script was coded on it

````

### Install dependencies if using offline compiler

```bash
pip install requests
```

### Run the script

```bash
python message_decoder.py
```

---

## 🔧 Sample Code Snippet

```python
patterns = re.findall(r"([^\s\d])(\d)(\d)", url_from_response)
```

This extracts patterns like `A23`, where:

* `A` is the character
* `2` is the x-coordinate
* `3` is the y-coordinate

---

## 👤 Author

**NDIVHUWO MUNYAI**
- 📧 [nmunyai11@gmail.com](mailto:your.email@example.com)
- 🔗 [https://github.com/DataCrafter20](https://github.com/yourusername)
- 🔗 [https://linkedin.com/in/ndivhuwo-munyai-390a58337](https://linkedin.com/in/yourusername)

---

## 📄 License

This project is licensed under the MIT License.
