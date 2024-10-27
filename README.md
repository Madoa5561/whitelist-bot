# Minecraft Bedrock Server Whitelist Discord Bot [JP]

このプロジェクトは、Discordボットを使用してMinecraft Bedrockサーバーのホワイトリストを管理するためのものです。このボットを使うことで、簡単にユーザーの追加や削除、ホワイトリストの確認ができます。

## 機能

- ホワイトリストへのユーザー追加
- ホワイトリストからユーザー削除
- 現在のホワイトリストの表示

## 必要なもの

- Python 3.x
- `discord.py`ライブラリ
- Minecraft Bedrock Server

## インストール手順

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/yourusername/discord-minecraft-whitelist-bot.git
   cd discord-minecraft-whitelist-bot
   pip install discord
   python3.x main.py
   ```
2. 注意事項
   ・main.pyはallowlist.jsonが置いてあるディレクトリ直下に置いてください
   ・nohupを用いたバックグラウンド動作を推奨します
