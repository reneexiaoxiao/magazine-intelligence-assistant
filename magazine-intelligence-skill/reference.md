# Magazine Intelligence Assistant - Reference Documentation

## Overview

This skill helps you automatically split magazine PDFs into individual articles, categorize them based on your interests, and extract actionable insights. It's designed for knowledge workers who read magazines strategically for content creation and research.

## Core Concepts

### Page Offset Handling

Magazine page numbers differ from PDF page numbers due to covers, ads, and front matter.

**Default Offset**: +2 pages
- Magazine page 16 = PDF page 18
- Magazine page 42 = PDF page 44

**Detection Method**: The skill scans the first 20 pages of the PDF to find the table of contents, then matches article titles with their magazine page numbers to calculate the offset.

### Tier System

Articles are prioritized into three tiers:

- **Tier 1**: Must-read articles matching your primary interests
- **Tier 2**: Recommended articles related to secondary interests
- **Tier 3**: Reference material for later review

### Tag Format

Tags use the format: `[Emoji] [Domain] :: [Action]`

Examples:
- `🎯 [AI] :: Analysis` - Deep analysis of AI-related content
- `📚 [Business] :: Reference` - Business cases for future reference
- `💡 [Innovation] :: Experiment` - Ideas to test or implement

## Configuration

### Config File Location

Your personalized configuration is stored at:
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

## Tools Reference

### process_magazine()

Main function to process a magazine PDF.

**Parameters**:
- `pdf_path` (str): Path to magazine PDF file
- `output_dir` (str): Directory to save split articles

**Returns**:
```python
{
    'success': True,
    'pdf_path': '/path/to/pdf',
    'total_articles': 16,
    'articles': [
        {
            'title_en': 'ARTICLE TITLE',
            'magazine_page_start': 16,
            'magazine_page_end': 19,
            'tier': 1,
            'tag': '🎯 [AI] :: Analysis',
            'filename_tag': '📄[AI]_ARTICLE_TITLE'
        }
    ],
    'config': {...}
}
```

**Usage**:
```python
from tools.magazine_processor import process_magazine

result = process_magazine('~/Downloads/magazine.pdf', 'articles')
if result['success']:
    print(f"Found {result['total_articles']} articles")
```

### create_article_list_from_toc()

Extracts article list from PDF table of contents.

**Pattern**: Matches uppercase article titles followed by page numbers.

**Detection**:
```python
pattern = r'([A-Z][A-Z\s]{15,})\s+(?:\.\s+)*(\d+)'
```

### split_pdf_to_articles()

Splits PDF into individual article files.

**Filename Format**:
```
T{tier}_{start_page}_{tag}.pdf
```

Example:
```
T1_16_📄[AI]_ROBOT_ARTICLE.pdf
```

## Output Formats

### Article Briefing (Markdown)

```markdown
### 📄 Article #1: [Article Title]

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
[
  {
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
  }
]
```

## Troubleshooting

### Issue: Wrong Page Offset

**Symptoms**: Articles start or end at wrong pages

**Solution**:
1. Open the PDF and find a known article
2. Note the magazine page number printed on the page
3. Note the PDF page number shown in your PDF reader
4. Calculate: `offset = pdf_page - magazine_page`
5. Update `DEFAULT_PAGE_OFFSET` in `magazine_processor.py`

**Example**:
```
Magazine page 017 appears on PDF page 19
offset = 19 - 17 = 2
```

### Issue: Articles Not Detected

**Symptoms**: "Found 0 articles"

**Causes**:
1. Table of contents uses different formatting
2. PDF has no text layer (scanned images)
3. TOC is beyond first 15 pages

**Solutions**:
1. Manually create article list in JSON format
2. Use OCR tool to add text layer first
3. Adjust scan range in `create_article_list_from_toc()`

### Issue: Split Files Are Empty

**Symptoms**: PDF files created but 0 KB size

**Cause**: Page range outside PDF bounds

**Solution**: The code automatically clamps page ranges to valid PDF pages. Check that `magazine_page_end` doesn't exceed total pages.

## Best Practices

### For Setup Wizard

Run the setup wizard when:
- First installing the skill
- Changing your research focus
- Starting a new project
- Wanting to update your tagging system

### For Article Categorization

1. **Start with broad topics** (Technology, Business) → refine over time
2. **Use consistent emoji** for each domain (🎯 for primary, 📚 for reference)
3. **Update tags quarterly** to reflect evolving interests
4. **Export config before changes** to rollback if needed

### For Insight Generation

1. **Focus on actionable insights** (what should reader DO?)
2. **Keep public titles under 80 characters** for social media
3. **Write insights in present tense** (not "will be", but "is")
4. **Include specific examples** from the article

### For Batch Processing

```bash
# Process multiple magazines
for pdf in ~/Downloads/*.pdf; do
    python scripts/split_pdf.py "$pdf" "articles/$(basename $pdf .pdf)"
done
```

## Integration Examples

### With Notion API

```python
import requests

def push_to_notion(article):
    headers = {"Authorization": f"Bearer {NOTION_TOKEN}", "Notion-Version": "2022-06-28"}
    data = {
        "parent": {"database_id": NOTION_DB},
        "properties": {
            "Title": {"title": [{"text": {"content": article['title_en']}}]},
            "Tier": {"select": {"name": f"Tier {article['tier']}"}},
            "Tags": {"multi_select": [{"name": article['tag']}]}
        }
    }
    requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
```

### With Obsidian

```markdown
---
title: {{article['title_en']}}
tier: {{article['tier']}}
tags: {{article['tag']}}
magazine: WIRED March 2026
page_range: {{article['magazine_page_start']}}-{{article['magazine_page_end']}}
---

## Public Title
{{article['public_title']}}

## Shareable Insight
{{article['shareable_insight']}}

## Notes
- [ ] Read full article
- [ ] Extract key quotes
- [ ] Write implementation plan
```

## Performance Notes

- **Processing time**: ~5 seconds for 100-page magazine
- **Memory usage**: ~50MB for typical magazine
- **File size**: Split articles average 500KB-2MB each

## Version History

- **1.0** (2026-02-17): Initial release
  - Automatic PDF splitting
  - Page offset detection
  - Personalized tagging
  - Insight generation

## Support

- **Issues**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/issues
- **Documentation**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/blob/main/README.md
- **License**: MIT

## Related Skills

- **pdf**: For general PDF manipulation
- **citation-management**: For academic article tracking
- **book-deep-dive**: For in-depth book analysis
