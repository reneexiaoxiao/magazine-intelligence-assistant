#!/usr/bin/env python3
"""
Magazine Intelligence Assistant - Setup Wizard
Guides users through initial configuration
"""

import json
import os
from pathlib import Path


class SetupWizard:
    def __init__(self):
        self.config = {
            "user_name": "",
            "role": "",
            "primary_topics": [],
            "secondary_topics": [],
            "learning_style": "",
            "content_strategy": "",
            "tags": {},
            "relevance_threshold": "medium",
            "action_templates": {}
        }

    def print_header(self, title):
        print("\n" + "="*70)
        print(f"  {title}")
        print("="*70)

    def get_input(self, prompt, default="", required=True):
        """Get user input with default value"""
        if default:
            full_prompt = f"{prompt} [{default}]: "
        else:
            full_prompt = f"{prompt}: "

        value = input(full_prompt).strip()

        if not value and default:
            return default
        elif not value and required:
            return self.get_input(prompt, default, required)
        else:
            return value

    def step1_basic_info(self):
        """Step 1: Basic user information"""
        self.print_header("STEP 1: Basic Information")

        print("\n👋 Welcome to Magazine Intelligence Assistant!")
        print("Let's set up your personalized reading experience.\n")

        self.config["user_name"] = self.get_input("Your name")
        self.config["role"] = self.get_input(
            "Your role (e.g., Entrepreneur, Researcher, Investor, Student)",
            "Knowledge Worker"
        )

    def step2_topics(self):
        """Step 2: Topics of interest"""
        self.print_header("STEP 2: Topics of Interest")

        print("\n🎯 What topics are you most interested in?")
        print("Enter 3-5 topics, one per line (press Enter twice to finish):\n")

        while True:
            topic = input(f"Primary topic {len(self.config['primary_topics']) + 1}: ").strip()
            if not topic:
                if len(self.config["primary_topics"]) >= 3:
                    break
                else:
                    print("Please enter at least 3 primary topics.")
                    continue
            self.config["primary_topics"].append(topic)

        print("\n💡 Any secondary interests? (optional, press Enter to skip)")
        while len(self.config["secondary_topics"]) < 5:
            topic = input(f"Secondary topic {len(self.config['secondary_topics']) + 1}: ").strip()
            if not topic:
                break
            self.config["secondary_topics"].append(topic)

    def step3_preferences(self):
        """Step 3: Learning and content preferences"""
        self.print_header("STEP 3: Preferences")

        print("\n📚 How do you prefer to consume content?")
        print("1. deep_dive    - Comprehensive analysis, detailed notes")
        print("2. quick_scan   - Key takeaways, bullet points")
        print("3. balanced     - Mix of both\n")

        style_choice = self.get_input("Your preference (1-3)", "3")
        styles = {"1": "deep_dive", "2": "quick_scan", "3": "balanced"}
        self.config["learning_style"] = styles[style_choice]

        print("\n📢 What's your content strategy?")
        print("1. public_sharing  - Share insights publicly (blog, Twitter, etc.)")
        print("2. private_notes   - Personal notes only")
        print("3. both           - Mix of public and private\n")

        strategy_choice = self.get_input("Your strategy (1-3)", "1")
        strategies = {"1": "public_sharing", "2": "private_notes", "3": "both"}
        self.config["content_strategy"] = strategies[strategy_choice]

    def step4_tags(self):
        """Step 4: Custom tags"""
        self.print_header("STEP 4: Custom Tags")

        print("\n🏷️  Create custom tags for your topics")
        print("These will be used to categorize articles")
        print("Format: Emoji + Domain + Action")
        print("Example: 🦾 Embodied_AI :: Market_Map\n")

        # Generate suggested tags from primary topics
        print(f"Based on your primary topics, here are some suggestions:")
        emoji_suggestions = ["🎯", "💡", "🔬", "💼", "🚀", "⚡", "🔧", "📊", "🌐", "🎓"]

        for i, topic in enumerate(self.config["primary_topics"][:3]):
            emoji = emoji_suggestions[i % len(emoji_suggestions)]
            domain = topic.replace(" ", "_")
            action = "Deep_Dive" if self.config["learning_style"] == "deep_dive" else "Quick_Scan"

            tag_name = f"{emoji} {domain} :: {action}"
            description = input(f"\nTag for '{topic}' [{tag_name}]: ").strip()
            if not description:
                description = tag_name
                tag_name = tag_name

            action_desc = input(f"What do you want to do with these articles? [Analyze and create notes]: ").strip()
            if not action_desc:
                action_desc = "Analyze and create notes"

            self.config["tags"][tag_name] = {
                "description": f"Articles about {topic}",
                "action": action_desc
            }

        print("\n✅ Tags created! You can add more later by editing config.json")

    def step5_relevance(self):
        """Step 5: Relevance threshold"""
        self.print_header("STEP 5: Relevance Settings")

        print("\n🔍 How strict should article filtering be?")
        print("1. high    - Only highly relevant articles")
        print("2. medium  - Mix of highly and moderately relevant")
        print("3. low     - Include potentially interesting articles\n")

        relevance_choice = self.get_input("Your preference (1-3)", "2")
        relevances = {"1": "high", "2": "medium", "3": "low"}
        self.config["relevance_threshold"] = relevances[relevance_choice]

    def step6_review(self):
        """Step 6: Review and save"""
        self.print_header("STEP 6: Review & Save")

        print("\n📋 Your Configuration:")
        print(f"  Name: {self.config['user_name']}")
        print(f"  Role: {self.config['role']}")
        print(f"  Primary Topics: {', '.join(self.config['primary_topics'][:3])}")
        print(f"  Learning Style: {self.config['learning_style']}")
        print(f"  Content Strategy: {self.config['content_strategy']}")
        print(f"  Tags: {len(self.config['tags'])} custom tags")

        print("\n" + "-"*70)
        confirm = input("\nSave this configuration? (y/n): ").strip().lower()

        if confirm == 'y':
            self.save_config()
            print("\n✅ Configuration saved to config.json")
            print("\n🎉 Setup complete! You can now use Magazine Intelligence Assistant.")
        else:
            print("\n❌ Setup cancelled. Run this wizard again to restart.")

    def save_config(self):
        """Save configuration to file"""
        config_path = Path(__file__).parent.parent / "config.json"

        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

        # Also create a backup
        backup_path = config_path.with_suffix('.json.backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def run(self):
        """Run the complete setup wizard"""
        print("\n" + "="*70)
        print("  🤖 Magazine Intelligence Assistant - Setup Wizard")
        print("="*70)

        try:
            self.step1_basic_info()
            self.step2_topics()
            self.step3_preferences()
            self.step4_tags()
            self.step5_relevance()
            self.step6_review()
        except KeyboardInterrupt:
            print("\n\n❌ Setup cancelled by user.")
            return

        print("\n" + "="*70)
        print("  For support, visit: https://github.com/yourusername/magazine-intelligence-assistant")
        print("="*70 + "\n")


def main():
    wizard = SetupWizard()
    wizard.run()


if __name__ == "__main__":
    main()
