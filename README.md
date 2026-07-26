# WhatsApp Chat Analyzer

A web-based analytics application built with **Python** and **Streamlit** that extracts meaningful insights from exported WhatsApp chat files. The application processes chat data and presents interactive visualizations, helping users analyze messaging patterns, activity trends, emoji usage, and communication statistics.

---

## Features

- Upload WhatsApp chat (.txt) files
- Generate overall chat statistics
- View monthly and daily messaging timelines
- Analyze user-wise activity
- Identify the most active participants
- Generate word clouds
- Display most frequently used words
- Analyze emoji usage
- Visualize weekly activity heatmaps
- Count shared media and links

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.7+ |
| Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Matplotlib, Seaborn |
| NLP Utilities | WordCloud, Emoji |
| URL Detection | URLExtract |
| Parsing | Regular Expressions |

---

## Project Structure

```
whatsapp-chat-analyzer/
│
├── app.py
├── helper.py
├── preprocessor.py
├── stop_hinglish.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/akashpradhan23/whatsapp-chat-analyzer.git
```

### Navigate to the project

```bash
cd whatsapp-chat-analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Export a WhatsApp chat (**Without Media**).
2. Launch the application.
3. Upload the exported `.txt` file.
4. Explore chat analytics through interactive visualizations.

---

## Sample Analytics

- Overall Messages
- Total Words
- Media Shared
- Links Shared
- Monthly Timeline
- Daily Timeline
- Activity Heatmap
- Most Active Users
- Word Cloud
- Most Common Words
- Emoji Distribution

---

## Future Enhancements

- Sentiment Analysis
- AI-powered Chat Summary
- Multi-language Support
- PDF Report Export
- Chat Comparison
- Interactive Dashboard Filters

---

## Live Demo

**Coming Soon**

---

## Author

**Akash Pradhan**

GitHub: https://github.com/akashpradhan23

LinkedIn: *(Add your LinkedIn profile here)*

---

## License

This project is developed for educational and portfolio purposes.
