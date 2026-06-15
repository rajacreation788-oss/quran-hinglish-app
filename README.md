# Quran Hinglish App 📖

A beautiful, interactive web application for reading the Quran with **Hinglish (Hindi-English) translations** and **Original Arabic text** side-by-side.

## ✨ Features

- 🕌 **Complete Quran** - All 114 Surahs with verses
- 🌐 **Hinglish Translation** - Easy-to-read Hindi-English transliteration
- 🔤 **Arabic Text** - Original Arabic text with proper styling
- 📱 **Fully Responsive** - Works on desktop, tablet, and mobile
- 🎨 **Beautiful UI** - Islamic-themed design with elegant colors
- 🔀 **Easy Navigation** - Surah selector dropdown & Previous/Next buttons
- ⚡ **Fast Loading** - Optimized performance

## 🚀 Quick Start

### Option 1: Using Kaggle Dataset (Recommended)

1. **Install dependencies:**
   ```bash
   pip install kagglehub pandas
   ```

2. **Setup Kaggle API:**
   - Go to https://www.kaggle.com/settings/api
   - Click "Create New API Token"
   - Save the `kaggle.json` file to `~/.kaggle/`

3. **Run the data script:**
   ```bash
   python fetch_quran_data.py
   ```
   This will generate `quran_data.json` with the complete Quran.

4. **Open the app:**
   ```bash
   # Open QURAN file in your browser
   # Or use a local server:
   python -m http.server 8000
   # Then visit: http://localhost:8000
   ```

### Option 2: Quick Demo

Open `QURAN` file directly in your browser to see the sample data (includes Surah Al-Fatihah & Al-Baqarah).

## 📁 Project Structure

```
quran-hinglish-app/
├── QURAN                    # Main HTML application
├── fetch_quran_data.py      # Python script to fetch & process Kaggle dataset
├── quran_data.json          # Generated Quran data (created after running script)
├── README.md                # This file
└── QURAN                    # Alternative naming
```

## 📊 Data Format

The `quran_data.json` file structure:

```json
[
  {
    "surahName": "Surah Al-Fatihah",
    "surahNumber": 1,
    "ayats": [
      {
        "id": 1,
        "h": "Allah ke naam se shuru jo bada meherbaan...",
        "a": "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"
      }
    ]
  }
]
```

## 🛠️ How It Works

1. **Data Loading** - The app tries to load `quran_data.json` on page load
2. **Fallback** - If JSON not found, displays sample data from embedded code
3. **Dynamic UI** - Populates Surah dropdown from loaded data
4. **Navigation** - Browse through Surahs using dropdown, Previous/Next buttons
5. **Responsive** - Adapts layout for mobile devices

## 🎯 Usage

### Navigation
- **Surah Selector** - Click dropdown to jump to any Surah
- **Previous/Next Buttons** - Navigate between Surahs
- **Home Button** - Return to cover page

### Features
- Read Arabic and Hinglish side-by-side
- Verse numbers displayed for reference
- Smooth scrolling between Surahs
- Mobile-friendly layout

## 🔧 Customization

### Modify Colors
Edit CSS variables in the `<style>` section:
```css
#cover-page {
    background-color: #0b3d2e;    /* Dark green */
    color: #c5a059;               /* Gold */
}
```

### Change Fonts
```css
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Poppins:wght@300;400;600&display=swap');
```

### Add More Data
Update `quran_data.json` with additional Surahs in the same format.

## 📚 Data Sources

- **Kaggle Dataset**: [The Quran Dataset](https://www.kaggle.com/datasets/imrankhan197/the-quran-dataset)
- **Format**: CSV with Arabic text and English translations
- **Script**: Automatically converts to JSON format

## ⚙️ Requirements

- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)
- **Server** (optional): For local development
  ```bash
  # Python 3
  python -m http.server 8000
  
  # Node.js
  npx http-server
  
  # PHP
  php -S localhost:8000
  ```

## 🐛 Troubleshooting

### JSON not loading?
1. Ensure `quran_data.json` is in the same directory as `QURAN`
2. Check browser console for errors (F12 → Console)
3. Run with a local server (not file://)

### Dropdown shows "Loading Surahs..."?
1. Verify `fetch_quran_data.py` was run successfully
2. Check that `quran_data.json` exists
3. Ensure JSON is valid (use online JSON validator)

### Wrong translations?
1. Check Kaggle dataset columns match the script
2. Update `fetch_quran_data.py` column names if needed

## 📖 Example Usage

**Python Script Output:**
```
Downloading Quran dataset from Kaggle...
Path to dataset files: /Users/.../quran-dataset

Found CSV files: ['quran.csv']
Dataset shape: (6236, 8)
Columns: ['Surah', 'Ayah', 'Text_Arabic', 'Text_English', ...]

✅ Successfully created quran_data.json
Total Surahs: 114
```

## 🙏 Acknowledgments

- **Quranic Text**: Original Islamic sources
- **Dataset**: Kaggle community contributor imrankhan197
- **Fonts**: Google Fonts (Amiri, Poppins)
- **Design**: Islamic aesthetic inspiration

## 📝 License

This project uses publicly available Quranic data. Ensure compliance with source licenses when distributing.

## 🤝 Contributing

To enhance this app:
1. Improve Hinglish translations
2. Add additional languages
3. Implement audio recitations
4. Add search functionality
5. Create bookmarking features

Feel free to fork and submit pull requests!

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review browser console errors
3. Open an issue on GitHub

---

**Made with ❤️ for the Ummah** 🕌

**Last Updated:** June 2026
