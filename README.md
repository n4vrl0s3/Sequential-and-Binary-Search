# Sequential Search and Binary Search

This repository aims to provide a comprehensive starting point for understanding and implementing two fundamental search algorithms: Sequential Search and Binary Search. These search algorithms are implemented in Python and serve as a great introduction to search techniques for beginners and intermediate programmers.

<hr><br>

## Purpose of This Repository

The purpose of this repository is to help users understand and implement two basic search algorithms in Python. It includes detailed explanations, code examples, and usage instructions for both Sequential Search and Binary Search.

<hr><br>

## Demonstration

Here is a quick demo of how the search algorithms work:

```python
# Sequential Search Example
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search Example
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

<hr><br>

## Features

- Implementation of Sequential Search in Python
- Implementation of Binary Search in Python
- Example usage of both search algorithms
- Detailed comments and explanations

<hr><br>

## Technologies Used

- Python

<hr><br>

## Project Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/n4vrl0s3/Sequential-Search-and-Binary-Search.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Sequential-Search-and-Binary-Search
   ```

<hr><br>

## Steps to Run

To run the Python scripts, use the following commands:

1. **Run the Sequential Search script:**
   ```bash
   python program_v2.py
   ```
2. **Run the Binary Search script:**
   ```bash
   python program.py
   ```

<hr><br>

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

<hr><br>

<div align="center">
   <a href="https://www.instagram.com/n4vrl0s3/">
      <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=100:393E46,20:F7F7F7&section=footer&reversal=false&textBg=false&fontAlignY=50&descAlign=48&descAlignY=59"/>
   </a>
</div>
