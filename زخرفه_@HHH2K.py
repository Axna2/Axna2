import random
import telebot
token = input("ENTER TOKEN BOT : ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def f(message):
	bot.send_message(message.chat.id,f"• ارسل اسمك الان  - @HHH2K")
@bot.message_handler(func=lambda m:True)
def f(message):
	name = message.text
	if "a" in name or "b" in name or "c" in name or "d" in name or "e" in name or "f" in name or "g" in name or "h" in name or "i" in name or "j" in name or "k" in name or "l" in name or "m" in name or "n" in name or "o" in name or "p" in name or "q" in name or "r" in name or "s" in name or "t" in name or "u" in name or "v" in name or "w" in name or "x" in name or "y" in name or "z" in name:
		za = name.replace("a","🅰︎").replace("b","🅱︎").replace("c","🅲︎").replace("d","🅾︎").replace("e","🅴︎").replace("f","🅵︎").replace("g","🅶︎").replace("h","🅷︎").replace("i","🅸︎").replace("j","🅹︎").replace("k","🅺︎").replace("l","🅻︎").replace("m","🅼︎").replace("n","🅽︎").replace("o","🅾︎").replace("p","🅿︎").replace("q","🆀︎").replace("r","🆁︎").replace("s","🆂︎").replace("t","🆃︎").replace("u","🆄︎").replace("v","🆅︎").replace("w","🆆︎").replace("x","🆇︎").replace("y","🆈︎").replace("z","🆉︎")
		za2 = name.replace("a","ᴀ").replace("b","ʙ").replace("c","ᴄ").replace("d","ᴅ").replace("e","ᴇ").replace("f","ғ").replace("g","ɢ").replace("h","ʜ").replace("i","ɪ").replace("j","ᴊ").replace("k","ᴋ").replace("k","ᴋ").replace("l","ʟ").replace("m","ᴍ").replace("n","ɴ").replace("o","ᴏ").replace("p","ᴘ").replace("q","ǫ").replace("r","ʀ").replace("s","s").replace("t","ᴛ").replace("u","ᴜ").replace("v","ᴠ").replace("w","ᴡ").replace("x","x").replace("y","ʏ").replace("z","ᴢ")
		za3 = name.replace("a","ᗩ").replace("b","ᗷ").replace("c","ᑕ").replace("d","ᗪ").replace("e","ᗴ").replace("f","ᖴ").replace("g","ᘜ").replace("h","ᕼ").replace("i","I").replace("j","ᒍ").replace("k","K").replace("l","ᒪ").replace("m","ᗰ").replace("n","ᑎ").replace("o","O").replace("p","ᑭ").replace("q","ᑫ").replace("r","ᖇ").replace("s","Տ").replace("t","T").replace("u","ᑌ").replace("v","ᐯ").replace("w","ᗯ").replace("x","᙭").replace("y","Y").replace("z","ᘔ")
		za4 = name.replace("a","🇦 ").replace("b","🇧 ").replace("c","🇨 ").replace("d","🇩 ").replace("e","🇪 ").replace("f","🇫 ").replace("g","🇬 ").replace("h","🇭 ").replace("i","🇮 ").replace("j","🇯 ").replace("k","🇰 ").replace("l","🇱 ").replace("m","🇲 ").replace("n","🇳 ").replace("o","🇴 ").replace("p","🇵 ").replace("q","🇶 ").replace("r","🇷 ").replace("s","🇸 ").replace("t","🇹 ").replace("u","🇺 ").replace("v","🇻 ").replace("w","🇼 ").replace("x","🇽 ").replace("y","🇾 ").replace("z","🇿 ")
		za5 = name.replace("a","卂").replace("b","乃").replace("c","匚").replace("d","ᗪ").replace("e","乇").replace("f","千").replace("g","ᘜ").replace("h","卄").replace("i","|").replace("j","ﾌ").replace("k","Ҝ").replace("l","ㄥ").replace("m","爪").replace("n","几").replace("o","ㄖ").replace("p","卩").replace("q","Ҩ").replace("r","尺").replace("s","丂").replace("t","ㄒ").replace("u","ㄩ").replace("v","ᐯ").replace("w","山").replace("x","乂").replace("y","ㄚ").replace("z","乙")
		za6 = name.replace("a","a͜͡").replace("b","b͜͡").replace("c","c͜͡").replace("d","d͜͡").replace("e","e͜͡").replace("f","f͜͡").replace("g","g͜͡").replace("h","h͜͡").replace("i","i͜͡").replace("j","j͜͡").replace("k","k͜͡").replace("l","l͜͡").replace("m","m͜͡").replace("n","n͜͡").replace("o","o͜͡").replace("p","p͜͡").replace("q","q͜͡").replace("r","r͜͡").replace("s","s͜͡").replace("t","t͜͡").replace("u","u͜͡").replace("v","v͜͡").replace("w","w͜͡").replace("x","x͜͡").replace("y","y͜͡").replace("z","z͜͡")
		za7 = name.replace("a","ɐ").replace("b","q").replace("c","ɔ").replace("d","p").replace("e","ǝ").replace("f","ɟ").replace("g","ƃ").replace("h","ɥ").replace("i","ᴉ").replace("j","ɾ").replace("k","ʞ").replace("l","l").replace("m","ɯ").replace("n","u").replace("o","o").replace("p","d").replace("q","b").replace("r","ɹ").replace("s","s").replace("t","ʇ").replace("u","n").replace("v","ʌ").replace("w","ʍ").replace("x","x").replace("y","ʎ").replace("z","z")
		za8 = name.replace("a","ል").replace("b","ጌ").replace("c","ር").replace("d","ዕ").replace("e","ቿ").replace("f","ቻ").replace("g","ኗ").replace("h","ዘ").replace("i","ጎ").replace("j","ጋ").replace("k","").replace("l","ረ").replace("m","ጠ").replace("n","ክ").replace("o","ዐ").replace("p","የ").replace("q","ዒ").replace("r","ዪ").replace("s","ነ").replace("t","ፕ").replace("u","ሁ").replace("v","ሀ").replace("w","ሠ").replace("x","ሸ").replace("y","ሃ").replace("z","ጊ")
		za9 = name.replace("a","ᵃ").replace("b","ᵇ").replace("c","ᶜ").replace("d","ᵈ").replace("e","ᵉ").replace("f","ᶠ").replace("g","ᵍ").replace("h","ʰ").replace("i","ⁱ").replace("j","ʲ").replace("k","ᵏ").replace("l","ˡ").replace("m","ᵐ").replace("n","ⁿ").replace("o","ᵒ").replace("p","ᵖ").replace("q","ᵠ").replace("r","ʳ").replace("s","ˢ").replace("t","ᵗ").replace("u","ᵘ").replace("v","ᵛ").replace("w","ʷ").replace("x","ˣ").replace("y","ʸ").replace("z","ᶻ")
		za10 = name.replace("a","ꍏ").replace("b","ꌃ").replace("c","ꏳ").replace("d","ꀷ").replace("e","ꏂ").replace("f","ꎇ").replace("g","ꁅ").replace("h","ꀍ").replace("i","ꀤ").replace("j","꒻").replace("k","ꀘ").replace("l","꒒").replace("m","ꎭ").replace("n","ꈤ").replace("o","ꂦ").replace("p","ᖘ").replace("q","ꆰ").replace("r","ꋪ").replace("s","ꌚ").replace("t","꓄").replace("u","ꀎ").replace("v","꒦").replace("w","ꅐ").replace("x","ꉧ").replace("y","ꌩ").replace("z","ꁴ")
		za11=name.replace("a","a҉").replace("b","b҉").replace("c","c҉").replace("d","d҉").replace("e","e҉").replace("f","f҉").replace("g","g҉").replace("h","h҉").replace("i","i҉").replace("j","j҉").replace("k","k҉").replace("l","l҉").replace("m","m҉").replace("n","n҉").replace("o","o҉").replace("p","p҉").replace("q","q҉").replace("r","r҉").replace("s","s҉").replace("t","t҉").replace("u","u҉").replace("v","v҉").replace("w","w҉").replace("x","x҉").replace("y","y҉").replace("z","z҉")
		za12 = name.replace("a","𝐀").replace("b","𝐁").replace("c","𝐂").replace("d","𝐃").replace("e","𝐄").replace("f","𝐅").replace("g","𝐆").replace("h","𝐇").replace("i","𝐈").replace("j","𝐉").replace("k","𝐊").replace("l","𝐈").replace("m","𝐌").replace("n","𝐍").replace("o","𝐎").replace("p","𝐏").replace("q","𝐐").replace("r","𝐑").replace("s","𝐒").replace("t","𝐓").replace("u","𝐔").replace("v","𝐕").replace("w","𝐖").replace("x","𝐗").replace("y","𝐘").replace("z","𝐙")
		za13=name.replace("a","𝔸").replace("b","𝔹").replace("c","ℂ").replace("d","𝔻").replace("e","𝔼").replace("f","𝔽").replace("g","𝔾").replace("h","ℍ").replace("i","𝕀").replace("j","𝕁").replace("k","𝐊").replace("l","𝕃").replace("m","𝕄").replace("n","ℕ").replace("o","𝕆").replace("p","ℙ").replace("q","ℚ").replace("r","ℝ").replace("s","𝕊").replace("t","𝕋").replace("u","𝕌").replace("v","𝕍").replace("w","𝕎").replace("x","𝕏").replace("y","𝕐").replace("z","ℤ")
		bot.send_message(message.chat.id,za)
		bot.send_message(message.chat.id,za2)
		bot.send_message(message.chat.id,za3)
		bot.send_message(message.chat.id,za4)
		bot.send_message(message.chat.id,za5)
		bot.send_message(message.chat.id,za6)
		bot.send_message(message.chat.id,za7)
		bot.send_message(message.chat.id,za8)
		bot.send_message(message.chat.id,za9)
		bot.send_message(message.chat.id,za10)
		bot.send_message(message.chat.id,za11)
		bot.send_message(message.chat.id,za12)
		bot.send_message(message.chat.id,za13)
	if "ا"  in name or "ب"  in name or "ت" in name or "ث" in name or "ج" in name or "ح" in name or "خ" in name or "د" in name or "ذ" in name or "ر" in name or "ز" in name or "س" in name or "ش" in name or "ص" in name or "ض" in name or "ط" in name or "ظ" in name or "ع" in name or "غ" in name or "ف" in name or "ق" in name or "ك" in name or "ل" in name or "م" in name or "ن" in name or "ه" in name or "و" in name or "ي" in name:
		za = name.replace("ا","اﺂ").replace("ب","ﺑـ").replace("ت","ﺗـ").replace("ث","ﺛـ").replace("ج","ﺟـ").replace("ح","ﺣَـ").replace("خ","ﺧـ").replace("د","د").replace("ذ","ذ").replace("ر","ࢪ").replace("ز","ز").replace("س","ﺳـ").replace("ش","ﺷـ").replace("ص","ﺻَـ").replace("ض","ﺿـ").replace("ط","ﻃـ").replace("ظ","ظـ").replace("ع","ﻋـ").replace("غ","ﻏـ").replace("ف","ﻓـ").replace("ق","ﻗـ").replace("ك","ڪـ").replace("ل","ݪـ").replace("م","ﻣـ").replace("ن","ﻧـ").replace("ه","هـ").replace("و","و٘").replace("ي","ﯾـ")
		za2=name.replace("ا","آِإَ").replace("ب","بٰٖ").replace("ت","تِٰ").replace("ث","ث").replace("ج","جُٖ").replace("ح","حٰٖ").replace("خ","ڂِٰ").replace("د","د").replace("ذ","ڎ").replace("ر","ࢪٖ").replace("ز","ز").replace("س","سُ").replace("ش","ڜ").replace("ص","صُ").replace("ض","ضٖٚ").replace("ط","ط").replace("ظ","ظ").replace("ع","عٰٖ").replace("غ","غِٰ").replace("ف","فَِ").replace("ق","قٰٖ").replace("ك","ڪِٰ").replace("ل","ل").replace("م","مَِٰ").replace("ن","نَٖ").replace("ه","ُه").replace("و","وَٖ").replace("ي","ي")
		za3= name.replace("ا","ﺈَﭑِ").replace("ب","ﺑِ").replace("ت","ﺗِ").replace("ث","ﺛِ").replace("ج","ﺟَ").replace("ح","ﺣَ").replace("خ","ﺧِ").replace("د","دِ").replace("ذ","ذِ").replace("ر","ࢪ").replace("ز","ژِ").replace("س","ﺳَ").replace("ش","ﺷِ").replace("ص","ﺻۧ").replace("ض","ﺿَِ").replace("ط","ﻃِ").replace("ظ","ﻈِ").replace("ع","ﻋِ").replace("غ","ﻏِ").replace("ف","ﻓِ").replace("ق","ﻗِ").replace("ك","ڪَِ").replace("ل","ﻟ").replace("م","ﻣَ").replace("ن","טּ").replace("ه","هہ").replace("و","ꪆ").replace("ي","ﯾَ")
		za4= name.replace("ا","ﺂﺂ").replace("ب","ﺑبـ").replace("ت","ﺗتـ").replace("ث","ﺛثـ").replace("ج","ﺟجـ").replace("ح","ﺣحـ").replace("خ","ﺧخـ").replace("د","د").replace("ذ","ذ").replace("ر","ࢪ").replace("ز","زﺰ").replace("س","ﺳسـ").replace("ش","ﺷشـ").replace("ص","ﺻصـ").replace("ض","ﺿضـ").replace("ط","ﻃطـ").replace("ظ","ﻈظـ").replace("ع","ﻋعـ").replace("غ","ﻏغـ").replace("ف","ﻓفـ").replace("ق","ﻗقـ").replace("ك","ڪ").replace("ل","ﻟلـ").replace("م","ﻣمـ").replace("ن","ﻧنـ").replace("ه","ﮪهـ").replace("و","وٰ٘").replace("ي","ﯾيـ")
		za5=name.replace("ا","آإ").replace("ب","ﺑـ").replace("ت","ﺗـ").replace("ث","ﺛـ").replace("ج","ﺟَﺟـ").replace("ح","ﺣَﺣَـ").replace("خ","ﺧِﺧـ").replace("د","ډ").replace("ذ","ذ").replace("ر","رـر").replace("ز","ز").replace("س","ﺳِﺳـ").replace("ش","ﺷِﺷـ").replace("ص","ﺻَﺻَـ").replace("ض","ﺿِﺿـ").replace("ط","ﻃـ").replace("ظ","ظـ").replace("ع","ﻋِﻋـ").replace("غ","ﻏِﻏـ").replace("ف","ﻓـ").replace("ق","ﻗـ").replace("ك","ڪ").replace("ل","ݪـ").replace("م","ﻣﻣـ").replace("ن","ﻧـ").replace("ه","هـ").replace("و","ووَ").replace("ي","ﯾـ")
		za6=name.replace("ا","a").replace("ب","b").replace("ت","t").replace("ث","th").replace("ج","j").replace("ح","7").replace("خ","5").replace("د","d").replace("ذ","4").replace("ر","r").replace("ز","z").replace("س","s").replace("ش","sh").replace("ص","9").replace("ض","9'").replace("ط","6").replace("ظ","6'").replace("ع","3").replace("غ","3''").replace("ف","f").replace("ق","8").replace("ك","k").replace("ل","l").replace("م","m").replace("ن","n").replace("ه","h").replace("و","w").replace("ي","y")
		bot.send_message(message.chat.id,za)
		bot.send_message(message.chat.id,za2)
		bot.send_message(message.chat.id,za3)
		bot.send_message(message.chat.id,za4)
		bot.send_message(message.chat.id,za5)
		bot.send_message(message.chat.id,za6)
bot.polling()