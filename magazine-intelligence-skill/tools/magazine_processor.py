#!/usr/bin/env python3
"""
Magazine Intelligence Assistant - Claude Code Skill
Automatically splits magazine PDFs and extracts insights
"""

import PyPDF2
import json
import os
import re
from pathlib import Path

# Configuration paths
WORKSPACE = Path.home() / "Desktop" / "杂志精读"
CONFIG_PATH = WORKSPACE / "config.json"
DEFAULT_PAGE_OFFSET = 2

def load_config():
    """Load user configuration"""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "user_name": "User",
            "primary_topics": ["Technology", "Business", "Innovation"],
            "learning_style": "balanced",
            "tags": {
                "🎯 Primary_Topic :: Analysis": {
                    "description": "Articles about primary topics",
                    "action": "Create detailed analysis"
                }
            }
        }

def extract_articles_from_pdf(pdf_path):
    """Extract articles from PDF using table of contents"""
    reader = PyPDF2.PdfReader(pdf_path)

    articles = []

    # Simple TOC detection - looks for page patterns
    for page_num in range(min(20, len(reader.pages))):
        try:
            text = reader.pages[page_num].extract_text()

            # Find article titles (all caps, followed by page numbers)
            pattern = r'([A-Z][A-Z\s\?\',\-]{20,})\s+(\d+)'
            matches = re.findall(pattern, text)

            for match in matches:
                title = match[0].strip()
                page_num = int(match[1])

                if len(title) > 10:
                    articles.append({
                        'title': title,
                        'magazine_page': page_num
                    })
        except:
            continue

    return articles

def split_pdf_to_articles(pdf_path, output_dir, articles_config):
    """Split PDF into individual article PDFs"""
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    reader = PyPDF2.PdfReader(pdf_path)

    results = []

    for article in articles_config:
        title = article['title_en']
        mag_start = article['page_start']
        mag_end = article['page_end']

        # Convert magazine pages to PDF pages (with offset)
        pdf_start = mag_start + DEFAULT_PAGE_OFFSET
        pdf_end = mag_end + DEFAULT_PAGE_OFFSET + 1

        # Clamp to valid range
        total_pages = len(reader.pages)
        pdf_start = max(1, min(pdf_start, total_pages))
        pdf_end = max(pdf_start, min(pdf_end, total_pages + 1))

        # Generate filename
        tier = article.get('tier', 3)
        tag = article.get('filename_tag', f"Article[{mag_start}]")
        filename = f"T{tier}_{mag_start}_{tag}.pdf"
        output_path = output_dir / filename

        # Extract pages
        try:
            writer = PyPDF2.PdfWriter()

            for page_num in range(pdf_start - 1, pdf_end - 1):
                if 0 <= page_num < len(reader.pages):
                    writer.add_page(reader.pages[page_num])

            with open(output_path, 'wb') as f:
                writer.write(f)

            size_mb = output_path.stat().st_size / 1024 / 1024

            results.append({
                'file': str(output_path),
                'filename': filename,
                'pdf_pages': f"{pdf_start}-{pdf_end}",
                'size_mb': f"{size_mb:.1f}",
                'success': True
            })

        except Exception as e:
            results.append({
                'title': title,
                'error': str(e),
                'success': False
            })

    return results

def create_article_list_from_toc(pdf_path):
    """Create a structured article list from PDF"""
    reader = PyPDF2.PdfReader(pdf_path)

    articles = []

    # Scan first 15 pages for table of contents
    for page_num in range(min(15, len(reader.pages))):
        try:
            page = reader.pages[page_num]
            text = page.extract_text()

            # Pattern: Article title followed by page number
            pattern = r'([A-Z][A-Z\s]{15,})\s+(?:\.\s+)*(\d+)'
            matches = re.findall(pattern, text)

            for match in matches:
                title = match[0].strip()
                page_num = int(match[1])

                if len(title) > 10 and page_num > 0:
                    # Estimate article length (default 4 pages)
                    articles.append({
                        'title_en': title,
                        'magazine_page_start': page_num,
                        'magazine_page_end': page_num + 3,
                        'tier': 2  # Default tier
                    })

        except Exception as e:
            continue

    return articles

def process_magazine(pdf_path, output_dir):
    """Main function to process a magazine"""
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        return {
            'success': False,
            'error': f'PDF not found: {pdf_path}'
        }

    print(f"📄 Processing magazine: {pdf_path.name}")
    print(f"📊 Total pages: {PyPDF2.PdfReader(pdf_path).pages}")

    # Extract article list from TOC
    articles = create_article_list_from_toc(pdf_path)

    print(f"✅ Found {len(articles)} articles")

    # Load user config for tagging
    config = load_config()

    # Add tags to articles based on config
    for article in articles:
        # Simple keyword matching against user's interests
        topics = config.get('primary_topics', [])

        matched_topic = None
        for topic in topics:
            if topic.lower() in article['title_en'].lower():
                matched_topic = topic
                break

        if matched_topic:
            article['tag'] = f"🎯 [{matched_topic}] :: Analysis"
            article['tier'] = 1
        else:
            article['tag'] = "📚 [General] :: Reference"
            article['tier'] = 2

    # Generate filename tags
    for article in articles:
        topic = article.get('tag', 'General').split(']')[0].strip('🎯 [')
        title_short = article['title_en'][:20].replace(' ', '_')
        article['filename_tag'] = f"📄[{topic}]_{title_short}"

    return {
        'success': True,
        'pdf_path': str(pdf_path),
        'total_articles': len(articles),
        'articles': articles,
        'config': config
    }

# For Claude Code integration
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "articles"

        result = process_magazine(pdf_path, output_dir)

        if result['success']:
            print(f"\n✅ Processing complete!")
            print(f"📁 Output directory: {output_dir}")
            print(f"📊 Articles found: {result['total_articles']}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
