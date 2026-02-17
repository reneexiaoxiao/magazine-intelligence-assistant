#!/bin/bash
# GitHub CLI 一键安装脚本
# 请在终端运行此脚本

echo "=========================================="
echo "  GitHub CLI 自动安装"
echo "=========================================="
echo ""

# 检查是否已安装
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI 已安装"
    gh --version
    echo ""
    echo "正在登录..."
    gh auth login
    echo ""
    echo "✅ 完成！现在告诉我 '继续'"
    exit 0
fi

# 检查 Homebrew
if ! command -v brew &> /dev/null; then
    echo "📦 正在安装 Homebrew..."
    echo "⚠️  需要输入管理员密码"

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # 添加 Homebrew 到 PATH
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/usr/local/bin/brew shellenv)"
    fi

    echo "✅ Homebrew 安装完成"
fi

echo ""
echo "📦 正在安装 GitHub CLI..."
brew install gh

echo ""
echo "=========================================="
echo "  登录 GitHub"
echo "=========================================="
echo ""
echo "请运行以下命令登录:"
echo "  gh auth login"
echo ""
echo "或使用设备码:"
echo "  gh auth login -h github.com -s"
echo ""
