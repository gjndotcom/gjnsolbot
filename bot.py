import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '8034735329:AAE8U2E1Jso6PBppVkLcMgc4crGp5eHvXwM'

# ✅ Bot với default parse_mode
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✨ Buy & Sell", callback_data="buy_sell"),
         InlineKeyboardButton(text="🎯 Token Sniper", callback_data="token_sniper")],
        [InlineKeyboardButton(text="📍 Sniper Pumpfun", callback_data="sniper_pumpfun"),
         InlineKeyboardButton(text="📍 Sniper Moonshot", callback_data="sniper_moonshot")],
        [InlineKeyboardButton(text="✏️ Limit Orders", callback_data="limit_orders"),
         InlineKeyboardButton(text="📉 DCA Orders", callback_data="dca_orders")],
        [InlineKeyboardButton(text="🙈 Profile", callback_data="profile"),
         InlineKeyboardButton(text="👛 Wallets", callback_data="wallets")],
        [InlineKeyboardButton(text="🎮 Trades", callback_data="trades"),
         InlineKeyboardButton(text="🎮 Copy Trades", callback_data="copy_trades")],
        [InlineKeyboardButton(text="🔗 Referral System", callback_data="referral_system"),
         InlineKeyboardButton(text="📊 Ranking Top Vol", callback_data="ranking_topvol")],
        [InlineKeyboardButton(text="🏆 Claim Top Vol", callback_data="claim_topvol"),
         InlineKeyboardButton(text="🔄 Transfer SOL", callback_data="transfer_sol")],
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings"),
         InlineKeyboardButton(text="🔥 Our STBOT Tools", callback_data="stbot_tools")],
        [InlineKeyboardButton(text="🤖 Market Maker Bot", callback_data="market_maker"),
         InlineKeyboardButton(text="🇺🇸 🇷🇺 🇻🇳", callback_data="language")],
        [InlineKeyboardButton(text="📦 Backup Bots", callback_data="backup_bots"),
         InlineKeyboardButton(text="🛡️ Security", callback_data="security")],
        [InlineKeyboardButton(text="📘 Help", callback_data="help"),
         InlineKeyboardButton(text="🎓 Tutorials", callback_data="tutorials")],
        [InlineKeyboardButton(text="❌ Close", callback_data="close")]
    ])
    await message.answer("🔻 *Main Menu*", reply_markup=keyboard)

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    await callback.answer(f"You clicked: {callback.data}", show_alert=True)

# ✅ Định nghĩa đúng main()
async def main():
    await dp.start_polling(bot)

# ✅ Gọi đúng main()
if __name__ == "__main__":
    asyncio.run(main())
