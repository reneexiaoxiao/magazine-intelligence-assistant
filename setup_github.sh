#!/bin/bash
# GitHub自动化设置脚本
# 运行这个脚本后，以后只需要说"帮我更新GitHub"就可以了

set -e

echo "=========================================="
echo "  GitHub 自动化设置向导"
echo "=========================================="
echo ""

# 检查是否已安装 gh
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI 已安装"
    gh --version
else
    echo "📦 正在安装 GitHub CLI..."

    # 检查操作系统
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install gh
        else
            echo "❌ 请先安装 Homebrew: https://brew.sh"
            exit 1
        fi
    else
        echo "请手动安装 GitHub CLI:"
        echo "  Ubuntu/Debian: sudo apt install gh"
        echo "  或访问: https://cli.github.com/"
        exit 1
    fi

    echo "✅ GitHub CLI 安装完成"
fi

echo ""
echo "=========================================="
echo "  步骤 1: GitHub 登录认证"
echo "=========================================="
echo ""

# 检查是否已认证
if gh auth status &> /dev/null; then
    echo "✅ 已登录 GitHub"
    gh auth status
else
    echo "🔐 需要登录 GitHub"
    echo ""
    echo "请运行以下命令（会弹出浏览器）:"
    echo "  gh auth login"
    echo ""
    echo "或者使用设备码:"
    echo "  gh auth login -h github.com -s"
    echo ""

    read -p "按回车键开始登录..."
    gh auth login

    if gh auth status &> /dev/null; then
        echo "✅ 登录成功！"
    else
        echo "❌ 登录失败，请重试"
        exit 1
    fi
fi

echo ""
echo "=========================================="
echo "  步骤 2: 创建 GitHub 仓库"
echo "=========================================="
echo ""

REPO_NAME="magazine-intelligence-assistant"
USERNAME="reneexiaoxiao"

echo "仓库名称: $REPO_NAME"
echo "GitHub用户: $USERNAME"
echo ""

# 检查仓库是否已存在
if gh repo view $USERNAME/$REPO_NAME &> /dev/null; then
    echo "✅ 仓库已存在: github.com/$USERNAME/$REPO_NAME"
else
    echo "📝 正在创建仓库..."

    gh repo create $REPO_NAME \
        --public \
        --description "Transform magazine reading into strategic intelligence gathering" \
        --source=. \
        --remote=origin \
        --push

    echo "✅ 仓库创建成功！"
    echo "   https://github.com/$USERNAME/$REPO_NAME"
fi

echo ""
echo "=========================================="
echo "  🎉 设置完成！"
echo "=========================================="
echo ""
echo "以后你只需要说："
echo "  '帮我更新GitHub'"
echo ""
echo "我就会自动："
echo "  1. 添加所有修改"
echo "  2. 提交变更"
echo "  3. 推送到GitHub"
echo ""
echo "仓库地址:"
echo "  https://github.com/$USERNAME/$REPO_NAME"
echo ""
