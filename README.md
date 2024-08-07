# ---- File Organizer Script ----

This Python script automates the organization of files in a specified directory by sorting them into predefined folders based on their file types. 
It's a simple yet effective way to keep your files tidy and easily accessible.

## Features
  - Automatically creates folders for different file types.
  - Moves files to their corresponding folders based on extensions.
  - Supports a variety of file types including images, documents, audio, video, and archives.
  - Unrecognized file types are moved to an "Others" folder.

## Folder Structure
The script organizes files into the following categories:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.pptx`
  - **Audio**: `.mp3`, `.wav`, `.aac`
  - **Videos**: `.mp4`, `.mkv`, `.mov`
  - **Archives**: `.zip`, `.tar`, `.gz`
  - **Others**: Any other file types

## Usage

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
   ```

2. **Modify the source directory**:

   Update the `source_directory` variable in the script to point to the directory you want to organize:

   ```python
   source_directory = r"C:\path\to\your\directory"
   ```

3. **Run the script**:

   Execute the script using Python:

   ```sh
   python organize_files.py
   ```

## Example

Suppose you have the following files in your `Music` directory:

- `song.mp3`
- `photo.jpg`
- `document.pdf`
- `archive.zip`
- `video.mp4`
- `unknown.xyz`

After running the script, your directory structure will look like this:

```
Music/
├── Audio/
│   └── song.mp3
├── Documents/
│   └── document.pdf
├── Images/
│   └── photo.jpg
├── Archives/
│   └── archive.zip
├── Videos/
│   └── video.mp4
└── Others/
    └── unknown.xyz
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## Contact
For any questions or inquiries, please contact Mian Hasnat Tasneem Raza at mianhasnattasneemraza@gmail.com.
