# Magazine Intelligence Assistant - Quick Start Guide

## 5-Minute Setup

### Step 1: Install (1 minute)

```bash
# Clone or download
git clone https://github.com/reneexiaoxiao/magazine-intelligence-assistant.git
cd magazine-intelligence-assistant

# Run install script
chmod +x install.sh
./install.sh
```

Or manually:
```bash
pip3 install PyPDF2
python3 tools/setup_wizard.py
```

### Step 2: Configure (2 minutes)

The setup wizard will ask you:
1. Your name and role
2. Primary topics (3-5)
3. Secondary interests (optional)
4. Learning style (deep dive vs quick scan)
5. Content strategy (public sharing vs private)
6. Custom tags

**Example:**
```
Name: Rene
Role: Entrepreneur
Primary Topics:
  1. Embodied AI
  2. Solopreneurship
  3. Investment Analysis
Learning Style: balanced
Content Strategy: public_sharing
```

This creates `config.json` with your preferences.

### Step 3: Use with Claude/GPT (2 minutes)

1. Open `template/magazine_recommender_skill.md`
2. Copy the entire prompt
3. Paste into Claude or ChatGPT
4. Paste your magazine article list
5. Get personalized recommendations!

**Example Input:**
```
Here are the articles from this month's WIRED:

1. "Meet the Fleet of Robot Workers" (p.16-19)
2. "Inside the Crystal Capital" (p.6-11)
3. "China's AI Ecosystem" (p.24-29)
...
```

**Example Output:**
```markdown
### 📄 Article #1: Meet the Fleet of Robot Workers

> **🏷️ Tag:** `🦾 Embodied_AI :: Market_Map`
> **📢 Public Title:** 第一批走进人类社会的机器人，几乎肯定是中国的
> **💡 Shareable Insight:**
> "Unitree G1人形机器人43个电机，价格是Tesla Optimus的1/10。
> 中国供应链优势让具身智能的爆发提前到来。对于一人公司来说，
> 可以从两个维度思考：1) 机器人SaaS工具的机会窗口；2) 个人品牌
> 在'人机协作'时代的话语权。"
> **📍 Page Range:** p.16-19
> **📊 Tier:** 1
```

---

## Common Use Cases

### Use Case 1: Monthly Magazine Review

**Goal:** Quickly identify must-read articles

**Workflow:**
1. Run setup wizard with your interests
2. Paste magazine TOC into Claude with the skill
3. Get Tier 1 recommendations
4. Read only the top 3-5 articles

**Time Saved:** 2-3 hours per magazine

### Use Case 2: Research for Content Creation

**Goal:** Turn articles into social media content

**Workflow:**
1. Configure content_strategy as "public_sharing"
2. Use skill to generate public titles and insights
3. Copy insights directly to Twitter/Newsletter
4. Batch process multiple articles

**Time Saved:** 1-2 hours per week

### Use Case 3: Investment Research

**Goal:** Track industry trends

**Workflow:**
1. Set primary topics to your investment focus
2. Create custom tags like "💹 Pre-Seed" "📈 Series A"
3. Use skill to categorize and tag articles
4. Generate investment memos

**Time Saved:** 5+ hours per month

---

## Customization Examples

### Example 1: Venture Capitalist

```json
{
  "user_name": "Sarah Chen",
  "role": "VC Partner",
  "primary_topics": [
    "Deep Tech",
    "B2B SaaS",
    "Climate Tech"
  ],
  "tags": {
    "💹 Deep_Tech :: Investment_Thesis": {
      "description": "Deep tech investment opportunities",
      "action": "Create investment memo with TAM and team analysis"
    },
    "📊 SaaS :: Metrics": {
      "description": "SaaS metrics and benchmarks",
      "action": "Extract key metrics, compare to portfolio"
    }
  }
}
```

### Example 2: Tech Journalist

```json
{
  "user_name": "Marcus Lee",
  "role": "Tech Journalist",
  "primary_topics": [
    "AI Ethics",
    "Privacy",
    "Platform Governance"
  ],
  "tags": {
    "🔍 Ethics :: Case_Study": {
      "description": "AI ethics case studies",
      "action": "Extract key dilemmas, stakeholder perspectives"
    },
    "📰 Breaking :: News": {
      "description": "Breaking news stories",
      "action": "Fact-check, identify sources, draft article outline"
    }
  }
}
```

### Example 3: Product Manager

```json
{
  "user_name": "Alex Kim",
  "role": "Product Manager",
  "primary_topics": [
    "Product Strategy",
    "User Research",
    "Growth Hacking"
  ],
  "tags": {
    "🚀 Product :: Framework": {
      "description": "Product frameworks and models",
      "action": "Extract framework, create one-pager for team"
    },
    "📈 Growth :: Experiment": {
      "description": "Growth experiments and case studies",
      "action": "Identify key tactics, create test plan"
    }
  }
}
```

---

## Troubleshooting

### Issue: Tags don't match my interests

**Solution:**
1. Edit `config.json`
2. Add/remove tags under "tags" section
3. Restart Claude/GPT with updated prompt

### Issue: Too many articles categorized as Tier 1

**Solution:**
1. Edit `config.json`
2. Change `"relevance_threshold": "medium"` to `"high"`
3. Re-run categorization

### Issue: Insights not detailed enough

**Solution:**
1. Edit `config.json`
2. Change `"learning_style": "quick_scan"` to `"deep_dive"`
3. Add custom action templates

### Issue: Want to process PDFs automatically

**Solution:**
1. Use the PDF splitter tool:
   ```bash
   python tools/split_magazine.py \
     --input "magazine.pdf" \
     --output "articles"
   ```
2. This will split PDF into individual articles
3. Use article list with skill for categorization

---

## Advanced Tips

### Tip 1: Create Topic-Specific Prompts

Copy `template/magazine_recommender_skill.md` and modify:
- Add topic-specific keywords
- Customize output format
- Add domain-specific questions

### Tip 2: Batch Process Multiple Magazines

```bash
# Create config for each magazine
cp config.json economist_config.json
cp config.json wired_config.json

# Edit each config with magazine-specific tags

# Process with different configs
python tools/split_magazine.py \
  --input "economist.pdf" \
  --config "economist_config.json"
```

### Tip 3: Integrate with Note-Taking Apps

After getting insights:
1. Copy JSON output
2. Use script to convert to Markdown
3. Import into Notion/Obsidian
4. Add to your knowledge base

### Tip 4: Create Reading Pipeline

```
Magazine PDF → Splitter → Article List → Skill → Insights → Notes → Content
```

Automate each step with scripts!

---

## Getting Help

- **Documentation**: See `docs/` folder
- **Issues**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/issues
- **Discussions**: https://github.com/reneexiaoxiao/magazine-intelligence-assistant/discussions

---

**Happy Reading! 📚✨**
