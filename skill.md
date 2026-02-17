# Skill: Magazine Intelligence Assistant
# Version: 1.0
# Description: Transform magazine reading into strategic intelligence - split PDFs, categorize articles, extract insights

**Magazine Intelligence Assistant** - A comprehensive skill for automatically splitting magazine PDFs and extracting actionable insights.

## What It Does

1. **Split PDF**: Automatically splits magazine PDF into individual articles with correct page offsets
2. **Categorize**: Tags articles based on your personalized interests
3. **Extract Insights**: Generates shareable insights with actionable takeaways
4. **Organize**: Creates structured JSON for further processing

## Quick Start

### First Time Setup

1. **Configure your preferences** (one-time):
   ```
   Please run setup wizard to configure your interests

   This will create a personalized config with your topics and tags
   ```

### Regular Use

**To process a new magazine:**
```
I have a new magazine PDF at: [path/to/magazine.pdf

Please:
1. Split it into articles
2. Categorize based on my interests
3. Generate recommendations
```

## Configuration

The skill uses `~/Desktop/杂志精读/config.json` for your personalized settings:
- Primary topics of interest
- Custom tags and categories
- Learning style preferences
- Content strategy (public/private)

## Capabilities

- PDF splitting with automatic page offset detection
- Article categorization with custom tags
- Insight generation
- JSON output for automation

## Requirements

- PyPDF2 for PDF processing
- Python 3.8+

## Example Usage

```
Help me process the latest WIRED magazine at ~/Downloads/Wired.pdf

Split it into articles and give me:
1. Tier 1 articles I must read
2. Shareable insights for each
3. JSON output for my notes
```

## Output

### Part 1: Human-Readable Briefing
```markdown
### 📄 Article #1: [Title]

> **🏷️ Tag:** [Your_Tag]
> **📢 Public Title:** [Engaging title]
> **💡 Shareable Insight:** [Actionable insight]
> **📍 Page Range:** p.X - p.Y
> **📊 Tier:** 1
```

### Part 2: Machine-Readable JSON
```json
[{
  "title_en": "Article Title",
  "filename_tag": "🎯[Topic]_Article",
  "page_start": 3,
  "page_end": 7,
  "tier": 1,
  "public_title": "Engaging title",
  "shareable_insight": "..."
}]
```

## Notes

- Page offset is automatically detected (default +2 for most magazines)
- All configuration is stored locally in your workspace
- Works with any magazine format that has table of contents

---

**For:** Researchers, Entrepreneurs, Investors, Content Creators
**License:** MIT
**GitHub:** https://github.com/reneexiaoxiao/magazine-intelligence-assistant
