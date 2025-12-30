from telethon import TelegramClient, events
import re

API_ID = 26039545
API_HASH = "4d7087d16018f05303b4a41db5889c7a"
SESSION = "market_session"

SOURCE_CHANNEL = "@ResellGifts1"  # channel you're forwarding from
TARGET_CHANNEL = "@nft350"
STAR_LIMIT = 351

client = TelegramClient(SESSION, API_ID, API_HASH)

def extract_price(text):
    match = re.search(r"Price\s*:?\s*(\d+)", text)
    if match:
        return int(match.group(1))
    return None

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def new_listing(event):
    msg = event.message.message
    price = extract_price(msg)
    if price is None or price >= STAR_LIMIT:
        return

    # Extract NFT name from the 3rd line
    lines = msg.split("\n")
    if len(lines) >= 5:
        nft_line = lines[4].strip()
        nft_name = nft_line.replace("🎁", "").strip()
    else:
        nft_name = "Unknown-NFT"

    # Build post in your format
    post_text = (
        "🎁 New Gift Listing 🎁\n\n"
        f"<a href='t.me/nft/{nft_name}'>🔗 {nft_name}</a>\n\n"
        f"Price : {price} ⭐️"
    )

    await client.send_message(TARGET_CHANNEL, post_text, parse_mode="html")
    print(f"Found a gift, Price : {price}")



print("Monitoring only NEW listings under 350 ⭐ ...")
client.start()
client.run_until_disconnected()
