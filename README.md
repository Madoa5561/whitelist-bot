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
- main.pyはallowlist.jsonが置いてあるディレクトリ直下に置いてください
- nohupを用いたバックグラウンド動作を推奨します

## 環境変数の設定
ボットのトークンやその他の設定は、環境変数として指定することを推奨します。以下のように設定できます。

```bash
export DISCORD_TOKEN='YOUR_DISCORD_BOT_TOKEN'
```

## ライセンス
- このプロジェクトはMITライセンスのもとで公開されています。

## 貢献
- バグ報告や機能追加の提案は、Issuesセクションでお知らせください。また、プルリクエストも歓迎します。
