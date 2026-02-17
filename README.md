# 🤖 Magazine Intelligence Assistant

> **Transform magazine reading from passive consumption into strategic intelligence gathering**

A customizable AI assistant that helps you **curate, categorize, and extract insights** from magazine articles. Perfect for researchers, entrepreneurs, investors, and lifelong learners who want to turn their reading into actionable knowledge.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production--ready-success.svg)

---

## ✨ Features

- 🔍 **Smart Article Categorization**: Automatically tag and prioritize articles based on your interests
- 📊 **Structured Output**: Generate both human-readable briefings and machine-readable JSON
- 🎯 **Customizable Tags**: Create your own tagging system for different topics
- 💡 **Actionable Insights**: Transform articles into shareable insights with specific action items
- 🔧 **PDF Splitter Integration**: Works seamlessly with PDF splitting tools
- ⚙️ **Setup Wizard**: Interactive configuration for personalized experience

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/reneexiaoxiao/magazine-intelligence-assistant.git
cd magazine-intelligence-assistant

# Run the setup wizard
python tools/setup_wizard.py
```

### Basic Usage

1. **Configure Your Preferences**
   ```bash
   python tools/setup_wizard.py
   ```
   This will create a `config.json` file with your:
   - Primary topics of interest
   - Custom tags and categories
   - Learning style preferences
   - Content strategy (public/private)

2. **Use with Claude/GPT**
   - Open `template/magazine_recommender_skill.md`
   - The prompt will auto-load your `config.json`
   - Paste your magazine article list
   - Get personalized recommendations

3. **Integrate with PDF Splitter**
   ```bash
   python tools/split_magazine.py \
     --input "magazine.pdf" \
     --output "articles"
   ```

---

## 📁 Project Structure

```
magazine-intelligence-assistant/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── config.example.json                # Example configuration
├── config.json                        # Your personal config (created by wizard)
│
├── tools/                             # Automation tools
│   ├── setup_wizard.py                # Interactive setup wizard
│   ├── split_magazine.py              # PDF splitter (with offset +2)
│   └── magazine_utils.py              # Utility functions
│
├── template/                          # AI Prompts
│   ├── magazine_recommender_skill.md  # Main skill for Claude/GPT
│   └── customization_guide.md         # Advanced customization
│
└── docs/                              # Documentation
    ├── USER_GUIDE.md                  # Detailed user guide
    ├── API_REFERENCE.md               # Configuration API
    └── CONTRIBUTING.md                # Contribution guidelines
```

---

## 🎯 Use Cases

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

## 🔧 Configuration

### Quick Setup (Recommended)

```bash
python tools/setup_wizard.py
```

### Manual Configuration

Copy `config.example.json` to `config.json` and edit:

```json
{
  "user_name": "Your Name",
  "role": "Entrepreneur",
  "primary_topics": [
    "AI & Machine Learning",
    "Startups",
    "Productivity"
  ],
  "tags": {
    "🤖 AI :: Research": {
      "description": "AI research papers and breakthroughs",
      "action": "Summarize key findings and implications"
    },
    "💼 Business :: Case_Study": {
      "description": "Startup and business case studies",
      "action": "Extract business model and lessons learned"
    }
  }
}
```

---

## 📝 Example Output

### Input: Magazine Article List

```
1. "The Future of AI in Healthcare" (p.24-29)
2. "How One Startup Disrupted Logistics" (p.45-50)
3. "Productivity Tips from Top CEOs" (p.67-70)
```

### Output: Personalized Briefing

```markdown
### 📄 Article #1: The Future of AI in Healthcare

> **🏷️ Tag:** `🤖 AI :: Research`
> **📢 Public Title:** 为什么AI医疗的下一个十年比前十年更值得期待
> **💡 Shareable Insight:**
> "This article reveals that AI diagnostics have reached 95% accuracy,
> surpassing human doctors in 3 key areas. For healthcare startups,
> this means the opportunity is no longer in algorithms but in
> integration and workflow. Worth exploring as a startup thesis."
> **📍 Page Range:** p.24-29
> **📊 Tier:** 1
```

### Output: Machine-Readable JSON

```json
[
  {
    "article_id": 1,
    "title_en": "The Future of AI in Healthcare",
    "filename_tag": "🤖[AI]_Healthcare_Future",
    "tag": "🤖 AI :: Research",
    "tier": 1,
    "public_title": "为什么AI医疗的下一个十年比前十年更值得期待",
    "shareable_insight": "This article reveals..."
  }
]
```

---

## 🎨 Customization

### Create Custom Tags

Edit your `config.json`:

```json
{
  "tags": {
    "🎯 [Your_Topic] :: [Action_Type]": {
      "description": "What this tag means",
      "action": "What to do with these articles"
    }
  }
}
```

### Define Action Templates

```json
{
  "action_templates": {
    "research": "Create research brief with 3 questions",
    "business": "Analyze business model canvas",
    "content": "Turn into tweet thread"
  }
}
```

---

## 🔌 Integration with PDF Splitter

This project includes a PDF splitter that handles magazine page offsets:

```bash
# Split magazine with automatic page offset detection
python tools/split_magazine.py \
  --input "magazine.pdf" \
  --config "config.json" \
  --output "articles"
```

**Features:**
- ✅ Automatic page offset calculation (+2 default)
- ✅ Article boundary detection
- ✅ Batch processing
- ✅ Custom filename generation with tags

---

## 📚 Advanced Usage

### Mode 1: Quick Scan

Add `[QUICK_SCAN]` to your prompt for rapid analysis:
- Only Tier 1 articles
- 50-word insights
- Bullet-point summaries

### Mode 2: Deep Research

Add `[DEEP_RESEARCH]` for comprehensive analysis:
- All Tier 1 + Tier 2 articles
- 150-word insights
- Further reading suggestions
- Relevance scores

### Mode 3: Custom Focus

Add `[FOCUS: Specific_Topic]` to prioritize:
- Topic-specific filtering
- Related article recommendations
- Custom action items

---

## 🤝 Contributing

Contributions are welcome! Please see `docs/CONTRIBUTING.md` for guidelines.

**Areas for contribution:**
- Additional language support
- New tagging templates
- Integration with other AI platforms
- Enhanced PDF processing
- Web interface

---

## 📖 Documentation

- [User Guide](docs/USER_GUIDE.md) - Detailed usage instructions
- [API Reference](docs/API_REFERENCE.md) - Configuration options
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues

---

## 🐛 Known Issues

1. **PDF Page Offsets**: Some magazines use different page numbering systems
   - **Solution**: Manually verify and adjust `PAGE_OFFSET` in `split_magazine.py`

2. **Multi-page Articles**: Articles spanning multiple sections may be split incorrectly
   - **Solution**: Edit `page_end` in config to extend range

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- Original concept inspired by Rene's magazine reading workflow
- Built with Claude (Anthropic) and PyPDF2
- Community contributions and feedback

---

## 📞 Support

- **GitHub Issues**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/issues
- **Discussions**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/discussions
- **Email**: your-email@example.com

---

## 🔮 Roadmap

- [ ] Web-based configuration UI
- [ ] Support for more AI platforms (ChatGPT, Jasper, etc.)
- [ ] Automatic article summarization
- [ ] Integration with note-taking apps (Notion, Obsidian)
- [ ] Mobile app prototype
- [ ] Multi-language support

---

**Made with ❤️ by curious minds, for curious minds**

⭐ **Star this repo if you find it useful!**
