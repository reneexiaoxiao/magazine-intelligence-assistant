#!/usr/bin/env python3
"""
Split magazine PDF into individual articles
Usage: python scripts/split_pdf.py <pdf_path> <output_dir>
"""

import sys
import os

# Add parent directory to path to import from workspace
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tools.magazine_processor import process_magazine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/split_pdf.py <pdf_path> [output_dir]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "articles"

    # Process the magazine
    result = process_magazine(pdf_path, output_dir)

    if result['success']:
        print(f"\n✅ Successfully processed {result['total_articles']} articles")
        print(f"📁 Output: {output_dir}/")
        print(f"\nArticles:")
        for i, article in enumerate(result['articles'], 1):
            print(f"  {i}. {article['title_en'][:50]}... (p.{article['magazine_page_start']}-{article['magazine_page_end']})")
    else:
        print(f"\n❌ Error: {result.get('error')}")
        sys.exit(1)
