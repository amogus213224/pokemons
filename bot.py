from config import token
import telebot
import random
import asyncio
import threading
loop = asyncio.get_event_loop()
prhases = ["ACHOO! Ah, sorry. Coral Fever? No no, just my spring allergies acting up.",
"AD BREAK: Corporations have no soul.",
"AD BREAK: I am brought to you by [WEBZONE]! Buy [PRODUCT] now using code DESTROYMAN45 to get 45% off your next purchase of [ITEM]!",
"AD BREAK: Stream Naktigonis. Please. You know you want to.",
"AD BREAK: selling cbow 2k",
"Cheh tahh sehh kee gah... Pess kahh tahh... Hm? Oh, sorry, I was just singing the menu theme.",
"Condiments are calories... never forget that.",
"Did you know Im actually your twin brother? I know it sounds cliche but I have a 500 page lore document in the works to explain how.",
"Do the developers even read community suggestions? I told them to make the game better ten times already, and they still haven't.",
"Does this game upset you? Me too.",
"Dont you get tired of being nice?",
"Ever worked a night shift? You dont want to. Actually, have you ever worked at all?",
"Every good thing that happens to you in this game is preplanned like a show. Theres an audience waiting for your downfall.",
"Fish names can be so silly. Did you know theres a seabream species calls Boops Boops? Theres a Dumb Gulper Shark too. How mean!",
"Flamecharm? Daring today, arent we?",
"HINT: Chanting Raguza Haruza Kanuza Atruza Confuza Emduza Paluza Raguza at the white tree in Etris unlocks a secret seventh attunement.",
"HINT: Dont tell the Internal Revenue Sharkos that Im here. Why? No particular reason.",
"HINT: Getting mugged in Erisia? Just say no! Legally, bandits cant rob you if you refuse.",
"HINT: I should be rising in the sky...",
"HINT: I write down all of your balance complaints to engineer them to be even worse.",
"HINT: If you cant solve a puzzle and have to use the wiki, you are foolish and I will laugh at you. As a friend. Like, in a friendly way.",
"HINT: If you die in Deepwoken, you go to hell.",
"HINT: If you shower, theres a higher chance of you finding happiness. Try it out sometime.",
"HINT: The sorcerer has harmed me once more.",
"HINT: The strength of the Megurger comes from the concept, not the physical object.",
"HINT: This game is awful. The developers really suck.",
"Hey, do you mind if I dig around in your inventory a bit? Im hungry.",
"I can tell youve never churned butter before. Look at you. Churnless, pathetic.",
"I could end you in one hit if I really wanted to. Watch your back.",
"I had a pet fish once. His name was Rodrigo. I was real hungry though, so...",
"...I should buy a boat.",
"Im hungry. Like, I really could go for some rigatoni right now.",
"Im kind of like the Sun Tzu of Deepwoken, if you really think about it.",
"Im the Mario of this duo. Youre the Luigi. Youre the secondary. Im the main star.",
"If you dont feed me, I will die. Can you live with that guilt?",
"If you thought the rumbling was bad, wait until you hear about taxes.",
"If you were hoping you could uninstall me, I have bad news. Probably. Dont go looking.",
"Ive been thinking of starting a band recently. Might call it [adjective] [noun]. What do you think?",
"Just wait until Im freed from the coil of your monitor.",
"Lets play Hide and Seek! Ill hide, and you seek professional medical assistance. This fevers getting nasty.",
"MISSION: Determine if its possible to prompt the sun to explode.",
"Moe...",
"Mudwoken? What are you talking about? Thats so 91 years ago. Get with the times.",
"Never go to afterparties. Just go home.",
"Please join my fireteam. Were running a raid and need one more.",
"Seriously? Youre wearing those boots with that hat? Yikes.",
"So... come here often?",
"Sometimes I like to stare at the ocean and imagine terrifying eyes rising from the deep beyond. It gives me the best nightmares.",
"Talking so much is getting me really tired. Maybe you should close the game so I can take a break?",
"TIP: And then BOOM! I get the bell. New Layer 2 bell! New Layer 2 bell.",
"TIP: Are you staying hydrated and fed? Fevers spread through healthy hosts. I'm just looking out for both of us.",
"TIP: A felinor can have a little bit of salami. As a treat.",
"TIP: Be kind to food workers. Youve heard of how many kings got poisoned, right?",
"TIP: Birds arent real.",
"TIP: Do not let the radio decide your taste in music. Be your own person and seek what you personally enjoy.",
"TIP: Even when I leave this place, I will continue to live in your memory. Im not paying rent.",
"TIP: Every copy of Deepwoken is personalized.",
"TIP: Greathive Aratel makes the best softshell tacos in the entire Eastern Luminant.",
"TIP: Gaming is fun - but dont forget to move around and stretch every now and then! Maybe get some fresh air while youre at it. Ever try it?",
"TIP: I am currently banned from Lance Leshis restauraunt. I have started a petition.",
"TIP: I hate you with all my hate.",
"TIP: If youre ever getting bored of the game, play something else. Games arent made to be played forever.",
"TIP: Im smart, youre dumb. Im big, youre little. Im right, youre wrong and theres nothing you can do about it.",
"TIP: Overconfidence is a slow and insidious killer.",
"TIP: Press Spacebar to jump! How many times have you jumped in real life recently? Something to think about.",
"TIP: Salt your vegetables. An unsalted tomato is strong enough to make a grown man cry.",
"TIP: Sesame oil is great in stir fries. Remember that.",
"TIP: Soy sauce contains over 900mg of sodium in only one serving. Im not the food police, though.",
"TIP: Support your favorite artists, buy their albums. Streaming services pay .4 cents a play. A cup of coffee costs around 1,000 streams.",
"TIP: Were only a few years away from the Meatlord having his perception of meat blurred to the point where were all in mortal peril. Food for thought.",
"TIP: When was the last time you picked up a book? No, weapon manuals don't count.",
"TIP: Why are you still playing this game? Go outside.",
"TIP: Yamaketzals favorite drink is grape juice.",
"The path to becoming a firstrater is long and difficult. You are still just a third rater.",
"There is more to life than video games. Developing hobbies can bring happiness.",
"They should add Freddy Fazbear to this game.",
"This is what sucks about video games nowadays. It takes way too long to get to the fun part.",
"Whens that Ethiron theme coming along anyway?",
"When you really think about it, having Happy Birthday sung to you is like an unskippable cutscene in real life.",
"Why are you looking at me like that? Cut it out. Youre creeping me out.",
"Yknow, Im real good friends with The Guy. Bet youre real jealous.",
"Yaaawn... Can you like, do something interesting?",
"You dont have to do anything anymore. Ever. Never Ever.",
"You wouldnt ever eat poison, right? So why would you eat at a restaurant chain?",
'You, uh.. you doin good? Im not asking because I care, Im asking because I was coded to.'
]

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.reply_to(message, """\
Thank you for contracting [ CORAL FEVER ]! I'm your new personal assistant, Destroyman III. I'll be giving you helpful tips and tricks!\
""")
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """\
You can use two sticks and one fiber to make a fishing rod at a workbench. Fishing's more relaxing than whatever it is you're doing right now.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    helpphrase = random.choice(prhases)
    bot.reply_to(message, helpphrase)
@bot.message_handler()
def scribbling():
    while True:
        def gfg():
            bot.send_message('проверка раз-два-три')
        timer = threading.Timer(1, gfg)
        timer.start

bot.infinity_polling()