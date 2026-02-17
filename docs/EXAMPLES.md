# Example Usage

## Quick Example: Processing Your First Magazine

### Step 1: Setup (One-time)

```bash
cd magazine-intelligence-assistant
python tools/setup_wizard.py
```

**Example answers:**
```
Name: Alex
Role: Product Manager
Primary Topics:
  1. Product Strategy
  2. User Research
  3. Growth Hacking

Secondary Topics:
  4. Design Systems

Learning Style: 1 (deep_dive)
Content Strategy: 1 (public_sharing)

Tags:
Topic: Product Strategy
  Tag: 🎯 Product_Strategy :: Analysis
  Action: Extract frameworks, create one-pager

Topic: User Research
  Tag: 🔬 User_Research :: Case_Study
  Action: Identify methods, summarize findings

Topic: Growth Hacking
  Tag: 📈 Growth :: Experiment
  Action: Extract tactics, create test plan
```

### Step 2: Get Articles

**Option A: From PDF**
```bash
python tools/split_magazine.py \
  --input "harvard_business_review.pdf" \
  --output "articles"
```

**Option B: Manually**
Copy article list from magazine:
```
1. "The Future of Product Management" (p.24-29)
2. "UX Research at Scale" (p.45-50)
3. "Growth Hacking Experiments" (p.67-72)
```

### Step 3: Use with Claude

1. Open `template/magazine_recommender_skill.md`
2. Copy to clipboard
3. Paste into Claude
4. Add your article list

**Full prompt:**
```
[PASTE SKILL HERE]

Here are this month's Harvard Business Review articles:

1. "The Future of Product Management" (p.24-29)
   - Discusses AI in product decisions
   - Case studies from 3 companies

2. "UX Research at Scale" (p.45-50)
   - Remote research methods
   - Tools and templates

3. "Growth Hacking Experiments" (p.67-72)
   - A/B testing frameworks
   - Case study: Instagram growth
```

### Step 4: Get Output

**Claude will return:**

```markdown
### 📄 Article #1: The Future of Product Management

> **🏷️ Tag:** `🎯 Product_Strategy :: Analysis`
> **📢 Public Title:** 为什么AI不会取代产品经理，但会改变他们的工作方式
> **💡 Shareable Insight:**
> "这篇文章揭示了一个反直觉的观点：AI不会取代产品经理，
> 而是放大他们的战略价值。文中3个案例显示，成功的PM
> 把70%时间花在用户洞察上，只有30%在执行层面。
> 对我的产品团队来说，意味着需要重新培训：1) AI工具使用；
> 2) 用户访谈技巧；3) 战略思维框架。值得在下周团队会上讨论。"
> **📍 Page Range:** p.24-29
> **📊 Tier:** 1
```

```json
[
  {
    "article_id": 1,
    "title_en": "The Future of Product Management",
    "filename_tag": "🎯[Product_Strategy]_Future_of_PM",
    "tier": 1,
    "public_title": "为什么AI不会取代产品经理，但会改变他们的工作方式",
    "shareable_insight": "这篇文章揭示了..."
  }
]
```

---

## Real-World Examples

### Example 1: Entrepreneur Reading TechCrunch

**Config:**
```json
{
  "user_name": "Sam",
  "role": "Startup Founder",
  "primary_topics": ["SaaS", "Fundraising", "Growth"],
  "tags": {
    "💼 SaaS :: Case_Study": {
      "action": "Analyze business model, extract playbook"
    }
  }
}
```

**Input:**
```
1. "How XYZ reached $1M ARR in 12 months" (p.15-20)
2. "Y Combinator's latest batch trends" (p.34-38)
```

**Output:**
- Tags articles by SaaS metrics
- Extracts growth tactics
- Creates action items for own startup

### Example 2: Researcher Reading Nature

**Config:**
```json
{
  "user_name": "Dr. Lee",
  "role": "AI Researcher",
  "primary_topics": ["Machine Learning", "Neuroscience"],
  "learning_style": "deep_dive",
  "tags": {
    "🔬 ML :: Paper": {
      "action": "Summarize methodology, identify assumptions"
    }
  }
}
```

**Input:**
```
1. "New breakthrough in transformer architecture" (p.567-572)
2. "Brain-computer interfaces progress report" (p.589-595)
```

**Output:**
- Categorizes by research domain
- Summarizes key findings
- Generates 3 research questions per article

### Example 3: VC Reading Forbes

**Config:**
```json
{
  "user_name": "Sarah",
  "role": "VC Partner",
  "primary_topics": ["Deep Tech", "Climate Tech", "B2B SaaS"],
  "tags": {
    "💹 Deep_Tech :: Investment": {
      "action": "Create investment memo: TAM, team, moat"
    }
  }
}
```

**Input:**
```
1. "10 Climate Tech Startups to Watch in 2024" (p.78-85)
2. "The State of Deep Tech Investing" (p.92-98)
```

**Output:**
- Tags by investment thesis
- Generates investment memos
- Highlights red flags/green flags

---

## Pro Tips

### Tip 1: Batch Processing

Process multiple magazines at once:
```
[ALL ARTICLES FROM JANUARY]

HBR:
1. "Article A" (p.1-5)
2. "Article B" (p.6-10)

WIRED:
1. "Article C" (p.15-20)
2. "Article D" (p.25-30)
```

Get cross-publication insights!

### Tip 2: Custom Action Templates

Add to `config.json`:
```json
{
  "action_templates": {
    "newsletter": "Turn into 300-word newsletter with 3 key takeaways",
    "thread": "Create Twitter thread with 5-8 tweets + 1 actionable tip",
    "notion": "Format as Notion page with tags, summary, and action items"
  }
}
```

### Tip 3: Create Reading Lists

After processing, create Trello boards/Notion databases:
- Column 1: To Read (Tier 1)
- Column 2: Read Later (Tier 2)
- Column 3: Reference (Tier 3)

Move cards as you read!

### Tip 4: Share Insights

Copy public titles and insights directly to:
- Twitter/X
- LinkedIn
- Newsletter
- Team Slack

Build your thought leadership!

---

## Troubleshooting Examples

### Problem: Too many Tier 1 articles

**Solution:**
```json
{
  "relevance_threshold": "high"  // Change from "medium"
}
```

### Problem: Insights too generic

**Solution:**
```json
{
  "learning_style": "deep_dive",  // Change from "quick_scan"
  "action_templates": {
    "default": "Create 3 bullet points + 1 action item + 1 question"
  }
}
```

### Problem: Tags don't match

**Solution:**
Edit tags in `config.json`:
```json
{
  "tags": {
    "Your_Custom_Tag :: Action": {
      "description": "More specific description",
      "action": "More specific action"
    }
  }
}
```

---

**Happy experimenting! 🎯**
