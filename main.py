import discord
import json
import requests

# Discordボットのトークン
TOKEN = ''
# GeyserMC APIのURL
GEYSER_API_URL = 'https://api.geysermc.org/v2/xbox/xuid/'

# Intentsの設定
intents = discord.Intents.default()
intents.messages = True  # メッセージのインテントを有効にする
intents.message_content = True  # メッセージの内容を取得するためのインテントを有効にする
# Discordクライアントの作成
client = discord.Client(intents=intents)
# ホワイトリストファイルのパス
WHITELIST_FILE = 'allowlist.json'

def load_whitelist():
    with open(WHITELIST_FILE, 'r') as file:
        return json.load(file)

def save_whitelist(data):
    with open(WHITELIST_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_to_whitelist(name, xuid):
    data = load_whitelist()
    data.append({
        "ignoresPlayerLimit": False,
        "name": name,
        "xuid": xuid
    })
    save_whitelist(data)

def remove_from_whitelist(name):
    data = load_whitelist()
    updated_data = [entry for entry in data if entry["name"] != name]
    save_whitelist(updated_data)

def get_whitelist():
    data = load_whitelist()
    return data

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user and not message.author == "508440240848109589":
        return
    # ヘルプコマンド
    if message.content.startswith('!help'):
        help_message = (
            
       
"利用可能なコマンド:\n"
            "`!whitelist <MCID>` - 指定したMCIDをホワイトリストに追加します。\n"
            "`!whitelist list` - 現在のホワイトリストを表示します。\n"
            "`!remove <プレイヤー名>` - 指定したプレイヤー名をホワイトリストから削除します。\n"
        )
        await message.channel.send(help_message)
        return

    # コマンドのチェック
    if message.content.startswith('!whitelist'):
        command = message.content.split(' ')
        if len(command) < 2:
            await message.channel.send('使用法: !whitelist <MCID> または !whitelist list')
            return

        action = command[1]
        
        if action.lower() == 'list':
            whitelist = get_whitelist()
            if not whitelist:
                await message.channel.send('ホワイトリストは空です。')
            else:
                response = "ホワイトリスト:\n" + "\n".join([f"{entry['name']} (XUID: {entry['xuid']})" for entry in whitelist])
                await message.channel.send(response)

        else:
            mcid = action  # コマンドの後にMCIDを指定
            response = requests.get(GEYSER_API_URL + mcid)
            
            if response.status_code == 200:
                xuid = response.json().get('xuid')
                if xuid:
                    add_to_whitelist(mcid, xuid)
                    await message.channel.send(f'{mcid}がホワイトリストに追加されました。')
                else:
                    await message.channel.send('XUIDを取得できませんでした。')
            else:
                await message.channel.send('APIからの応答にエラーがありました。')

    # ホワイトリスト削除
    elif message.content.startswith('!remove'):
        player_name = message.content.split(' ')[1]  # コマンドの後にプレイヤー名を指定
        remove_from_whitelist(player_name)
        await message.channel.send(f'{player_name}がホワイトリストから削除されました。')

# ボットをぶんぶん走らせる
client.run(TOKEN)
