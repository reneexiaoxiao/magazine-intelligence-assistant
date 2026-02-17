# 🤖 Magazine Intelligence Assistant - Claude Code Skill

> **Transform magazine reading into strategic intelligence with this Claude Code skill**

Transform magazine reading from passive consumption into strategic intelligence gathering. This skill automatically splits magazine PDFs into articles, categorizes them based on your interests, and extracts actionable insights.

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-purple.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ What It Does

- 🔍 **Automatic PDF Splitting**: Splits magazine PDFs into individual articles with correct page offsets
- 🏷️ **Smart Categorization**: Tags articles based on your personalized interests and topics
- 💡 **Insight Generation**: Creates shareable insights with actionable takeaways
- 📊 **Tier-Based Prioritization**: Automatically identifies must-read articles vs reference material
- 🎯 **Customizable Workflows**: Adapts to your research style and content strategy

---

## 🚀 Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Python 3.8+ with PyPDF2 (`pip install PyPDF2`)

### Installation

```bash
# Clone the repository
git clone https://github.com/reneexiaoxiao/magazine-intelligence-assistant.git
cd magazine-intelligence-assistant/magazine-intelligence-skill

# Run the installation script
bash scripts/install.sh

# Configure your preferences
python3 ~/.claude/skills/magazine-intelligence-assistant/scripts/setup_wizard.py
```

### Usage in Claude Code

Once installed, you can use natural language commands:

```
> I have a new magazine: ~/Downloads/Wired_March_2026.pdf
> Please split it into articles and give me:
> 1. Tier 1 articles (must-read)
> 2. Categorized with my interests
> 3. Shareable insights for each
> 4. JSON output for my notes
```

The skill will:
1. ✅ Scan the PDF for articles
2. ✅ Split into individual PDF files
3. ✅ Categorize based on your config
4. ✅ Generate insights with public titles
5. ✅ Output both markdown and JSON

---

## 📁 Project Structure

```
magazine-intelligence-assistant/
├── magazine-intelligence-skill/       # Claude Code skill package
│   ├── SKILL.md                       # Skill definition and usage
│   ├── reference.md                   # Detailed documentation
│   ├── LICENSE.txt
│   ├── magazine_processor.py          # Core processing logic
│   └── scripts/
│       ├── install.sh                 # Installation script
│       ├── setup_wizard.py            # Configuration wizard
│       └── split_pdf.py               # PDF splitting tool
│
└── README.md                          # This file
```

### How It Works

```
┌─────────────────────────────────────────┐
│ 1. Install as Claude Code Skill         │
│    bash scripts/install.sh              │
└─────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────┐
│ 2. Configure Your Preferences           │
│    python scripts/setup_wizard.py       │
│    ↓                                     │
│  Creates ~/Desktop/杂志精读/config.json │
│  - Your topics                          │
│  - Your custom tags                     │
│  - Your learning style                  │
└─────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────┐
│ 3. Use in Claude Code                   │
│    > Split this magazine and categorize │
│    ↓                                     │
│  Skill automatically:                   │
│  - Detects articles from TOC            │
│  - Splits PDF with page offsets         │
│  - Tags by your interests               │
│  - Generates insights                   │
└─────────────────────────────────────────┘
```

---

## 🎯 Example Output

### Human-Readable Briefing

```markdown
### 📄 Article #1: WHY ROBOTS ARE BECOMING YOUR NEW COWORKERS

> **🏷️ Tag:** `🎯 [AI] :: Analysis`
> **📢 Public Title:** Why Robots Are Becoming Your New Coworkers
> **💡 Shareable Insight:**
>
> The article reveals a fundamental shift in robotics from pre-programmed
> arms to AI-powered systems that learn by watching humans. This mirrors
> the same breakthrough that made ChatGPT possible—scaling up with more
> data and compute. Key insight: physical AI is now following the same
> exponential curve as digital AI, making 2026 a tipping point for
> human-robot collaboration in everyday workplaces.
>
> **📍 Page Range:** p.16 - p.19
> **📊 Tier:** 1 (Must-read)
> **🎯 Action:** Deep analysis with 3 follow-up questions
```

### Machine-Readable JSON

```json
[{
  "article_id": 1,
  "title_en": "WHY ROBOTS ARE BECOMING YOUR NEW COWORKERS",
  "filename_tag": "📄[AI]_WHY_ROBOTS_ARE",
  "magazine_page_start": 16,
  "magazine_page_end": 19,
  "pdf_page_start": 18,
  "pdf_page_end": 21,
  "tier": 1,
  "tag": "🎯 [AI] :: Analysis",
  "public_title": "Why Robots Are Becoming Your New Coworkers",
  "shareable_insight": "The article reveals a fundamental shift...",
  "recommended_action": "Deep analysis with 3 follow-up questions"
}]
```

---

## ⚙️ Configuration

Your personalized settings are stored in:
```
~/Desktop/杂志精读/config.json
```

### Configuration Structure

```json
{
  "user_name": "Your Name",
  "role": "Knowledge Worker",
  "primary_topics": ["Technology", "Business", "Innovation"],
  "secondary_topics": ["Design", "Marketing"],
  "learning_style": "balanced",
  "content_strategy": "public_sharing",
  "tags": {
    "🎯 [Technology] :: Analysis": {
      "description": "Deep analysis of tech trends",
      "action": "Create detailed breakdown"
    }
  }
}
```

### Learning Styles

- **deep_dive**: Extensive analysis with multiple perspectives
- **quick_scan**: Brief summaries focusing on key insights
- **balanced**: Mix of summary and analysis (default)

### Content Strategies

- **public_sharing**: Generate public-friendly titles and insights
- **private_notes**: Personal notes with internal context
- **both**: Both public and private versions

---

## 🔧 Features

### Automatic Page Offset Detection

The skill automatically detects the difference between magazine page numbers and PDF page numbers:

- **Default**: +2 (magazine page 16 = PDF page 18)
- **Detection**: Scans PDF for page numbers to calculate offset
- **Manual override**: Can specify custom offset if needed

### Smart Article Detection

- Scans first 15-20 pages for table of contents
- Extracts article titles and page ranges
- Estimates article lengths
- Handles multi-page articles correctly

### Personalized Tagging

- Keyword matching against your interests
- Automatic tier assignment (1-3)
- Custom tag generation based on topics
- Filename generation with tags

---

## 📖 Use Cases

### For Researchers
- Tag articles by research domain
- Generate literature review summaries
- Identify emerging trends and signals

### For Entrepreneurs
- Spot business opportunities
- Analyze case studies and business models
- Extract actionable market insights

### For Investors
- Track industry developments
- Identify investment themes
- Generate investment memos

### For Content Creators
- Turn articles into social media content
- Create curated newsletters
- Build thought leadership

---

## 🔍 Troubleshooting

### Issue: Wrong Page Offset

**Symptoms**: Articles start or end at wrong pages

**Solution**:
1. Open the PDF and find a known article
2. Note the magazine page number and PDF page number
3. Calculate: `offset = pdf_page - magazine_page`
4. Update `DEFAULT_PAGE_OFFSET` in `magazine_processor.py`

### Issue: Articles Not Detected

**Symptoms**: "Found 0 articles"

**Solutions**:
1. Check if PDF has text layer (not scanned images)
2. Adjust scan range in `create_article_list_from_toc()`
3. Manually create article list in JSON format

---

## 📚 Documentation

- [Skill Reference](magazine-intelligence-skill/reference.md) - Detailed API documentation
- [Skill Definition](magazine-intelligence-skill/SKILL.md) - Usage examples and capabilities

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

**Areas for contribution:**
- Enhanced PDF processing algorithms
- Support for more magazine formats
- Integration with note-taking apps (Notion, Obsidian)
- Multi-language support
- Web-based configuration UI

---

## 📄 License

MIT License - see [LICENSE.txt](magazine-intelligence-skill/LICENSE.txt) for details

---

## 🙏 Acknowledgments

- Built with [Claude Code](https://claude.com/claude-code)
- Uses [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing
- Inspired by real-world magazine reading workflows

---

## 📞 Support

- **GitHub Issues**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/issues
- **Documentation**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant

---

⭐ **Star this repo if you find it useful!**

**Made with ❤️ for curious minds who read strategically**
