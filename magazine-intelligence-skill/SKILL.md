# Magazine Intelligence Assistant

An intelligent magazine reading assistant that automatically splits PDFs into articles, categorizes them based on your interests, and extracts actionable insights.

## Capabilities

- **PDF Splitting**: Automatically splits magazine PDF into individual articles with correct page offsets
- **Smart Categorization**: Tags articles based on your personalized topics and interests
- **Insight Generation**: Creates shareable insights with actionable takeaways
- **Multi-Format Output**: Generates both human-readable briefings and machine-readable JSON

## Quick Start

### First-Time Setup

1. **Configure your interests** (one-time setup):
   ```bash
   python scripts/setup_wizard.py
   ```
   This creates `~/Desktop/杂志精读/config.json` with your personalized settings.

### Regular Use

**To process a new magazine:**

> I have a new magazine: ~/Downloads/Wired_March_2026.pdf
>
> Please split it into articles and give me:
> 1. Tier 1 articles (must-read)
> 2. Categorized with my interests
> 3. Shareable insights for each
> 4. JSON output for my notes

The skill will:
1. ✅ Scan the PDF for articles
2. ✅ Split into individual PDF files
3. ✅ Categorize based on your config
4. ✅ Generate insights with public titles
5. ✅ Output both markdown and JSON

## Configuration

Your personalized settings are stored in:
```
~/Desktop/杂志精读/config.json
```

This includes:
- **Primary topics**: Your main areas of interest
- **Secondary topics**: Additional interests
- **Learning style**: deep_dive / quick_scan / balanced
- **Content strategy**: public_sharing / private_notes / both
- **Custom tags**: Your personalized tag system

## Tools Available

- `scripts/split_pdf.py` - Split magazine PDF into articles
- `scripts/setup_wizard.py` - Interactive configuration wizard
- `tools/magazine_processor.py` - Core processing logic

## Output Formats

### Human-Readable Briefing
```markdown
### 📄 Article #1: [Article Title]

> **🏷️ Tag:** `[Your Custom Tag]`
> **📢 Public Title:** [Engaging title for social media]
> **💡 Shareable Insight:** [50-150 word actionable insight]
> **📍 Page Range:** p.X - p.Y
> **📊 Tier:** 1 (Must-read)
```

### Machine-Readable JSON
```json
[{
  "article_id": 1,
  "title_en": "Article Title",
  "filename_tag": "🎯[Topic]_Article",
  "page_start": 3,
  "page_end": 7,
  "tier": 1,
  "public_title": "Engaging title",
  "shareable_insight": "..."
}]
```

## Page Offset Handling

The skill automatically detects page offsets:
- **Default**: +2 (magazine page 16 = PDF page 18)
- **Detection**: Scans PDF for page numbers to calculate offset
- **Manual override**: Can specify custom offset if needed

## Use Cases

### For Researchers
- Tag articles by research domain
- Generate literature review summaries
- Identify emerging trends

### For Entrepreneurs
- Spot business opportunities
- Analyze case studies and business models
- Extract actionable insights

### For Investors
- Track industry developments
- Identify investment themes
- Generate investment memos

### For Content Creators
- Turn articles into social media content
- Create curated newsletters
- Build thought leadership

## Examples

**Example 1: Quick Scan**
> Scan this magazine and give me only the top 3 articles about AI and startups

**Example 2: Deep Dive**
> Process this magazine with deep research mode. I want detailed analysis of all Tier 1 and Tier 2 articles with 3 follow-up questions each.

**Example 3: Custom Topic**
> Focus on articles about "climate tech" and "sustainability" from this magazine. Create a summary for my newsletter.

## Requirements

- Claude Code installed
- Python 3.8+
- PyPDF2 >= 3.0.0 (`pip install PyPDF2`)

## Notes

- All split articles are saved to: `~/Desktop/杂志精读/[Magazine_Name]/articles/`
- Configuration can be updated anytime by re-running the setup wizard
- The skill learns your preferences over time through config.json

---

**Version**: 1.0
**Last Updated**: 2026-02-17
**License**: MIT
**GitHub**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant
