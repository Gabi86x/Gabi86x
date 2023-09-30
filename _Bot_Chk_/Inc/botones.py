from pyrogram.types import *

botoncmd = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "𝙏𝙊𝙊𝙇𝙎",
                            callback_data="tools"
                        ),
                        InlineKeyboardButton(
                            "𝘽𝙄𝙉𝙎",
                            callback_data="bins"
                        ),
                    ],
                    [
                        InlineKeyboardButton( 
                            "𝙃𝙄𝙏𝙎",
                           callback_data="SilverBullet"),
                    ],
                ]
            )

atrasboton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "𝘼𝙩𝙧𝙖𝙨",
                    callback_data="home"
                ),
                InlineKeyboardButton(
                    "𝘾𝙚𝙧𝙧𝙖𝙧",
                    callback_data="exit"
                ),
        ]
        ]
    )

regene = InlineKeyboardMarkup([[InlineKeyboardButton("𝙍𝙚𝙜𝙚𝙣𝙚𝙧𝙖𝙧!",callback_data="regen")]])

ExtraRegen = InlineKeyboardMarkup([[InlineKeyboardButton("Extras Re Gen ",callback_data="extras")]])

