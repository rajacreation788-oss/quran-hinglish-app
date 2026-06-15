# Setup Guide - Quran Hinglish App 🕌

Complete step-by-step guide to get your Quran app running with the complete Quran data.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser
- Kaggle account (free)

## Installation Steps

### Step 1: Setup Kaggle API 🔑

1. Go to https://www.kaggle.com/settings/api
2. Click **"Create New API Token"**
3. This downloads `kaggle.json`
4. Place it in your home directory:
   - **Windows**: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
   - **Mac/Linux**: `~/.kaggle/kaggle.json`
5. Set permissions (Linux/Mac only):
   ```bash
   chmod 600 ~/.kaggle/kaggle.json
   ```

### Step 2: Clone Repository

```bash
git clone https://github.com/rajacreation788-oss/quran-hinglish-app.git
cd quran-hinglish-app
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**OR manually:**
```bash
pip install kagglehub pandas requests
```

### Step 5: Generate Quran Data

Run the data fetching script:

```bash
python fetch_quran_data.py
```

**Expected output:**
```
Downloading Quran dataset from Kaggle...
Path to dataset files: /Users/.../.cache/kagglehub/datasets/imrankhan197/the-quran-dataset/versions/1

Files in dataset:
  - quran.csv
  - chapters.csv

Dataset shape: (6236, 8)
Columns: ['Surah', 'Ayah', 'Text_Arabic', 'Text_English', ...]

First few rows:
    Surah  Ayah                     Text_Arabic              Text_English
0      1     1       بِسْمِ اللَّهِ الرَّحْمَنِ...    In the name of Allah, ...
1      1     2       الْحَمْدُ لِلَّهِ رَبِّ الْعَا...    All praise is due to Allah, ...

✅ Successfully created quran_data.json
Total Surahs: 114
Sample: {
  "surahName": "Surah Al-Fatihah",
  "surahNumber": 1,
  "ayats": [
    {
      "id": 1,
      "h": "In the name of Allah, the Most Gracious...",
      "a": "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"
    }
  ]
}...
```

### Step 6: Start Local Server

Choose one method:

**Option A: Python (Recommended)**
```bash
python -m http.server 8000
```

**Option B: Node.js**
```bash
npx http-server
```

**Option C: PHP**
```bash
php -S localhost:8000
```

### Step 7: Open in Browser

Navigate to: **http://localhost:8000**

Select the `QURAN` file to open the app.

## 📁 File Verification

After running the script, verify these files exist:

```
quran-hinglish-app/
├── QURAN                          ✅ Main HTML file
├── fetch_quran_data.py            ✅ Data fetching script
├── quran_data.json                ✅ Generated Quran data (6236 verses, 114 Surahs)
├── README.md                      ✅ Project documentation
├── SETUP.md                       ✅ This file
├── requirements.txt               ✅ Python dependencies
└── .gitignore                     ✅ Git ignore rules
```

## 🎯 Quick Test

1. Open browser to `http://localhost:8000`
2. Click "Bismillah" button
3. Click "Start Reading"
4. Select any Surah from dropdown
5. Scroll through verses
6. Use Previous/Next buttons to navigate

✅ If all works → Success! 🎉

## 🐛 Troubleshooting

### Error: "kagglehub module not found"
```bash
pip install kagglehub
```

### Error: "kaggle.json not found"
1. Verify file exists: `~/.kaggle/kaggle.json`
2. Check file permissions: `ls -la ~/.kaggle/kaggle.json`
3. Recreate from Kaggle settings

### Error: "quran_data.json not found"
1. Ensure `fetch_quran_data.py` ran without errors
2. Check current directory: `ls -la quran_data.json`
3. Verify JSON is valid: Use https://jsonlint.com/

### Browser shows "Loading..." forever
1. Open browser console (F12)
2. Check for CORS or 404 errors
3. Ensure running on local server (not file://)
4. Verify `quran_data.json` exists in same directory

### CSV columns not recognized
1. Check Kaggle dataset structure at: https://www.kaggle.com/datasets/imrankhan197/the-quran-dataset
2. Update column names in `fetch_quran_data.py` if needed
3. Look for: `Text_Arabic`, `Text_English`, `Surah`, `Ayah` columns

## 📊 Data Statistics

After successful setup, you'll have:
- **114 Surahs** (Chapters)
- **6,236 Verses** (Ayats)
- **2 Languages**: Arabic + English/Hinglish
- **File Size**: ~1-2 MB JSON

## 🔄 Updating Data

To refresh the Quran data from Kaggle:

```bash
# Delete old data
rm quran_data.json

# Run script again
python fetch_quran_data.py

# Refresh browser
```

## 📱 Mobile Testing

Test responsive design:
1. Open DevTools (F12)
2. Click device icon (mobile view)
3. Try different screen sizes
4. Test on actual phone: Use your computer's IP
   ```bash
   # Get IP
   ipconfig getifaddr en0  # Mac
   ipconfig              # Windows
   
   # Access from phone: http://<YOUR_IP>:8000
   ```

## 🚀 Deployment

### Deploy to GitHub Pages

1. Ensure `quran_data.json` is committed
2. Enable Pages in repository settings
3. App will be live at: `https://rajacreation788-oss.github.io/quran-hinglish-app/`

### Deploy to Netlify

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir .
```

### Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

## ✅ Verification Checklist

- [ ] Python 3.7+ installed
- [ ] Kaggle API configured
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Script ran successfully (`python fetch_quran_data.py`)
- [ ] `quran_data.json` created (114 Surahs)
- [ ] Local server running
- [ ] Browser opens to http://localhost:8000
- [ ] Can select and view Surahs
- [ ] Navigation buttons work
- [ ] Mobile view looks good

## 📞 Need Help?

1. **Check logs** - Look at terminal output for errors
2. **Browser console** - F12 → Console tab for JavaScript errors
3. **GitHub Issues** - Create an issue with error details
4. **Kaggle Dataset** - Verify dataset hasn't changed

## 🎓 Learning Resources

- [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web/Guide/)
- [Kaggle Datasets](https://www.kaggle.com/learn/datasets)
- [JSON Format](https://www.json.org/)
- [Web Servers](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)

## 📝 Next Steps

After setup:
1. ✅ Test all Surahs load correctly
2. 🎨 Customize colors and fonts
3. 🔍 Add search functionality
4. 🎵 Integrate audio recitations
5. 📱 Deploy to production

---

**Happy Reading!** 🕌✨

Made with ❤️ for the Ummah

Last Updated: June 2026
