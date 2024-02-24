import config

class Language:
    def __init__(self):
        self.channel_username = config.channel_username
        pass

    def welcame(self, language_code, first_name, total_token):
        channel = f'<a href="https://t.me/{self.channel_username}">👇</a>'
        eng = (f"\nHello {first_name} 👋, send me a prompt to generate an image!""\n""\nI recommend sending short and simple prompts for better images.""\n"
                    "\nRemember, 1🪙 Token equals one image.""\n""\nTo get new tokens you can:""\n1️⃣ Vote for 10 images for 1 🪙""\n2️⃣ Invite a friend for 3 🪙""\n3️⃣ Win contests to get 20 🪙\n4️⃣Members of the channel https://t.me/tasu_Channel will have +2 🪙"
                    "\n🛒 Purchase Tokens""\n""\n🥇 Win the contest to get new tokens! Contests last for a week, and you can submit only one image."f"\n🪙 Tokens: {total_token}"
                    "\n@tasu_openai_result")
        if language_code == 'it':
            message = (f"\nCiao {first_name} 👋, inviami un prompt per generare un'immagine!""\n""\nTi consiglio di inviare prompt brevi e non complessi per creare immagini migliori.""\n"
                    "\nRicorda che 1🪙 Token è un'immagine.""\n""\nPer ottenere nuovi token puoi:""\n1️⃣ Votare 10 immagini per 1 🪙""\n2️⃣ Invitare un amico per 3 🪙""\n3️⃣ Vincere i concorsi per ottenere 20 🪙\n4️⃣I membri del canale https://t.me/tasu_Channel avranno + 2 🪙"
                    "\n🛒 Acquistare i Token""\n""\n🥇 Vinci il concorso per ottenere nuovi token! I concorsi durano una settimana e puoi inviare una sola immagine."f"\n🪙 Token: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = (f"नमस्ते {first_name} 👋, मुझे एक प्रॉम्प्ट भेजें ताकि मैं एक छवि उत्पन्न कर सकूं!""\n""\nबेहतर छवियों के लिए छोटे और सरल प्रॉम्प्ट भेजने की सिफारिश की जाती है।""\n"
                    "\nध्यान दें, 1🪙 टोकन एक छवि के बराबर है।""\n""\nनए टोकन प्राप्त करने के लिए आप:""\n1️⃣ 1 🪙 के लिए 10 छवियों के लिए वोट करें""\n2️⃣ 3 🪙 के लिए एक दोस्त को आमंत्रित करें""\n3️⃣ 20 🪙 प्राप्त करने के लिए प्रतियोगिताओं को जीतें\n4️⃣ https://t.me/tasu_Channel चैनल के सदस्यों को +2 🪙"
                    "\n🛒 टोकन खरीदें""\n""\n🥇 नए टोकन प्राप्त करने के लिए प्रतियोगिता जीतें! प्रतियोगिताएँ एक सप्ताह तक चलती हैं, और आप केवल एक छवि सबमिट कर सकते हैं।"f"\n🪙 टोकन: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'es':
            message = (f"Hola {first_name} 👋, ¡envíame un prompt para generar una imagen!""\n""\nTe recomiendo enviar prompts cortos y simples para obtener mejores imágenes.""\n"
                    "\nRecuerda, 1🪙 Token equivale a una imagen.""\n""\nPara obtener nuevos tokens puedes:""\n1️⃣ Votar por 10 imágenes por 1 🪙""\n2️⃣ Invitar a un amigo por 3 🪙""\n3️⃣ Ganar concursos para obtener 20 🪙\n4️⃣Los miembros del canal https://t.me/tasu_Channel tendrán +2 🪙"
                    "\n🛒 Comprar Tokens""\n""\n🥇 ¡Gana el concurso para obtener nuevos tokens! Los concursos duran una semana y solo puedes enviar una imagen."f"\n🪙 Tokens: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'fr':
            message = (f"Bonjour {first_name} 👋, envoyez-moi un prompt pour générer une image!""\n""\nJe recommande d'envoyer des prompts courts et simples pour de meilleures images.""\n"
                    "\nRappelez-vous, 1🪙 Token équivaut à une image.""\n""\nPour obtenir de nouveaux jetons, vous pouvez :""\n1️⃣ Voter pour 10 images pour 1 🪙""\n2️⃣ Inviter un ami pour 3 🪙""\n3️⃣ Gagner des concours pour obtenir 20 🪙\n4️⃣Les membres du canal https://t.me/tasu_Channel auront +2 🪙"
                    "\n🛒 Acheter des jetons""\n""\n🥇 Gagnez le concours pour obtenir de nouveaux jetons ! Les concours durent une semaine et vous ne pouvez soumettre qu'une seule image."f"\n🪙 Jetons : {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'de':
            message = (f"Hallo {first_name} 👋, sende mir einen Prompt, um ein Bild zu generieren!""\n""\nIch empfehle, kurze und einfache Prompts für bessere Bilder zu senden.""\n"
                    "\nDenke daran, 1🪙 Token entspricht einem Bild.""\n""\nUm neue Tokens zu erhalten, kannst du:""\n1️⃣ Für 1 🪙 10 Bilder abstimmen""\n2️⃣ Einen Freund für 3 🪙 einladen""\n3️⃣ Gewinne Wettbewerbe, um 20 🪙 zu erhalten\4️⃣Mitglieder des Kanals https://t.me/tasu_Channel erhalten +2 🪙"
                    "\n🛒 Tokens kaufen""\n""\n🥇 Gewinne den Wettbewerb, um neue Tokens zu erhalten! Wettbewerbe dauern eine Woche, und du kannst nur ein Bild einreichen."f"\n🪙 Tokens: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'ru':
            message = (f"Привет {first_name} 👋, отправь мне подсказку, чтобы создать изображение!""\n""\nЯ рекомендую отправлять короткие и простые подсказки для лучших изображений.""\n"
                    "\nПомни, что 1🪙 Токен равен одному изображению.""\n""\nЧтобы получить новые токены, ты можешь:""\n1️⃣ Проголосовать за 10 изображений за 1 🪙""\n2️⃣ Пригласить друга за 3 🪙""\n3️⃣ Выиграть конкурсы, чтобы получить 20 🪙\n4️⃣Участники канала https://t.me/tasu_Channel получат +2 🪙"
                    "\n🛒 Купить Токены""\n""\n🥇 Выиграйте конкурс, чтобы получить новые токены! Конкурсы длится неделю, и вы можете отправить только одно изображение."f"\n🪙 Токены: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'uk':
            message = (f"Привіт {first_name} 👋, надішліть мені запит, щоб створити зображення!""\n""\nЯ рекомендую надсилати короткі та прості запити для кращих зображень.""\n"
                    "\nЗапам'ятайте, що 1🪙 Токен дорівнює одному зображенню.""\n""\nЩоб отримати нові токени, ви можете:""\n1️⃣ Проголосувати за 10 зображень за 1 🪙""\n2️⃣ Запросити друга за 3 🪙""\n3️⃣ Вигравати конкурси, щоб отримати 20 🪙\n4️⃣Учасники каналу https://t.me/tasu_Channel отримають +2 🪙"
                    "\n🛒 Купити Токени""\n""\n🥇 Виграйте конкурс, щоб отримати нові токени! Конкурси тривають тиждень, і ви можете надіслати лише одне зображення."f"\n🪙 Токени: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'zh':
            message = (f"你好 {first_name} 👋，发送一个提示给我生成一张图片吧！""\n""\n我建议您发送简短且简单的提示以获得更好的图片。""\n"
                    "\n请记住，1🪙 代币等于一张图片。""\n""\n要获取新代币，您可以：""\n1️⃣ 为 1 🪙 投票 10 张图片""\n2️⃣ 邀请一个朋友来 3 🪙""\n3️⃣ 赢得比赛获得 20 🪙\n4️⃣频道 https://t.me/tasu_Channel 的成员将额外获得 +2 🪙"
                    "\n🛒 购买代币""\n""\n🥇 赢得比赛获得新代币！比赛持续一周，您只能提交一张图片。"f"\n🪙 代币: {total_token}"
                    "\n@tasu_openai_result")
        elif language_code == 'ar':
            message = (f"مرحبًا {first_name} 👋، أرسل لي موجِّهًا لإنشاء صورة!""\n""\nأوصي بإرسال موجِّهات قصيرة وبسيطة للحصول على صور أفضل.""\n"
                    "\nتذكّر، 1🪙 توكن يُعادل صورة واحدة.""\n""\nللحصول على توكنات جديدة يمكنك:""\n1️⃣ التصويت على 10 صور مقابل 1 🪙""\n2️⃣ دعوة صديق للحصول على 3 🪙""\n3️⃣ الفوز في المسابقات للحصول على 20 🪙\n4️⃣ سيحصل أعضاء القناة https://t.me/tasu_Channel على +2 🪙 إضافية"
                    "\n🛒 شراء التوكنات""\n""\n🥇 اربح المسابقة للحصول على توكنات جديدة! تستمر المسابقات لمدة أسبوع، ويمكنك تقديم صورة واحدة فقط."f"\n🪙 التوكنات: {total_token}"
                    "\n@tasu_openai_result")
        else:       
            message = eng
        return message
        
    def you_already_voted(self, language_code):
        eng = (f'''You have already voted for this!''')
        if language_code == 'it':
            message = f'''Hai già votato questo!'''
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = (f'''आपने पहले से ही इसके लिए वोट किया है!''')
        elif language_code == 'es':
            message = (f'''¡Ya has votado por esto!''')
        elif language_code == 'fr':
            message = (f'''Vous avez déjà voté pour cela !''')
        elif language_code == 'de':
            message = (f'''Du hast bereits dafür abgestimmt!''')
        elif language_code == 'ru':
            message = (f'''Вы уже проголосовали за это!''')
        elif language_code == 'uk':
            message = (f'''Ви вже голосували за це!''')
        elif language_code == 'zh':
            message = (f'''您已经为此投过票了！''')
        elif language_code == 'ar':
            message = (f'''لقد صوتت بالفعل لهذا!''')
        else:
            message = eng
        return message
    
    def waiting(self, language_code):
        eng = "Waiting..."
        if language_code == 'it':
            message = "Attendi..."
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "रुको..."
        elif language_code == 'es':
            message = "Esperando..."
        elif language_code == 'fr':
            message = "En attente..."
        elif language_code == 'de':
            message = "Warten..."
        elif language_code == 'ru':
            message = "Ожидание..."
        elif language_code == 'uk':
            message = "Очікування..."
        elif language_code == 'zh':
            message = "等待中..."
        elif language_code == 'ar':
            message = "انتظار..."
        else:
            message = eng
        return message    
    
    def error_generation(self, language_code):
        eng = "Oops.. Something went wrong. I recommend that prompts adhere to OpenAI's policies, explicit and violent content is not allowed!"
        if language_code == 'it':
            message = "Ops.. Qualcosa è andato storto. Ti raccomando che i prompt devono rispettare le policy di OpenAI, i contenuti espliciti e violenti non sono ammessi!"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "उप्स.. कुछ गलत हो गया। मैं सुझाव दूँ कि प्रॉम्प्ट्स को ओपनएआई की नीतियों का पालन करना चाहिए, स्पष्ट और हिंसात्मक सामग्री की अनुमति नहीं है!"
        elif language_code == 'es':
            message = "Ups.. Algo salió mal. Te recomiendo que los comandos sigan las políticas de OpenAI, ¡no se permite contenido explícito y violento!"
        elif language_code == 'fr':
            message = "Oups.. Quelque chose s'est mal passé. Je recommande que les invites respectent les politiques d'OpenAI, le contenu explicite et violent n'est pas autorisé!"
        elif language_code == 'de':
            message = "Hoppla.. Da ist etwas schief gelaufen. Ich empfehle, dass die Eingabeaufforderungen den Richtlinien von OpenAI entsprechen, explizite und gewalttätige Inhalte sind nicht erlaubt!"
        elif language_code == 'ru':
            message = "Упс.. Что-то пошло не так. Я рекомендую, чтобы запросы соответствовали политике OpenAI, явное и насильственное содержание не допускается!"
        elif language_code == 'uk':
            message = "Ой.. Щось пішло не так. Рекомендую, щоб запити відповідали політиці OpenAI, явний і насильницький вміст не допускається!"
        elif language_code == 'zh':
            message = "哎呀.. 出了点问题。我建议提示符遵循OpenAI的政策，不允许明确和暴力内容！"
        elif language_code == 'ar':
            message = "أوبس.. حدث خطأ ما. أنصح بأن تلتزم الاستفسارات بسياسات OpenAI، لا يُسمح بالمحتوى الصريح والعنيف!"
        else:
            message = eng
        return message
    
    def you_win(self, language_code):
        eng = "You Win! Token: +20 🎉"
        if language_code == 'it':
            message = "Hai Vinto! Token: +20 🎉"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "आप जीते हैं! टोकन: +20 🎉"
        elif language_code == 'es':
            message = "¡Has ganado! Token: +20 🎉"
        elif language_code == 'fr':
            message = "Vous avez gagné! Jeton: +20 🎉"
        elif language_code == 'de':
            message = "Du hast gewonnen! Token: +20 🎉"
        elif language_code == 'ru':
            message = "Вы победили! Токен: +20 🎉"
        elif language_code == 'uk':
            message = "Ви перемогли! Токен: +20 🎉"
        elif language_code == 'zh':
            message = "你赢了！代币：+20 🎉"
        elif language_code == 'ar':
            message = "أنت الرابح! رمز: +20 🎉"
        else:
            message = eng
        return message

    def give_referral(self, language_code, referral):        
        eng = (f"\nThis is your referral code! 👇\n"
            f"\n{referral}\n" 
            f"\nSend it to a friend, if they start the bot, you'll get 3 tokens 🪙"
            f"\nAlternatively, you can buy a pack at https://t.me/TasuPremiumBot to get exclusive access to premium content and tokens! 🪙"
            f"\nAlways vote for others' images to earn tokens! 🪙")
        if language_code == 'it':
            message = (f"\nQuesto è il tuo codice referral! 👇\n"
                    f"\n{referral}\n" 
                    f"\nInvialo ad un amico, se avvia il bot otterrai 3 token 🪙"
                    f"\nAltrimenti puoi comprare un pacchetto su https://t.me/TasuPremiumBot ottenendo accesso esclusivo a contenuti premium e token! 🪙"
                    f"\nVota sempre le immagini degli altri per ottenere token! 🪙")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = ("यह आपका रेफरल कोड है! 👇\n"
                    f"\n{referral}\n" 
                    f"\nइसे एक दोस्त को भेजें, यदि वह बॉट शुरू करता है, तो आपको 3 टोकन मिलेंगे 🪙"
                    f"\nवैकल्पिक रूप से, आप https://t.me/TasuPremiumBot पर एक पैक खरीद सकते हैं, प्रीमियम सामग्री और टोकन के लिए अनूठी पहुंच प्राप्त करें! 🪙"
                    f"\nहमेशा दूसरों की छवियों के लिए वोट करें टोकन कमाने के लिए! 🪙")
        elif language_code == 'es':
            message = (f"\n¡Este es tu código de referencia! 👇\n"
                    f"\n{referral}\n" 
                    f"\nEnvíalo a un amigo, si comienza el bot, ¡obtendrás 3 tokens! 🪙"
                    f"\nAlternativamente, puedes comprar un paquete en https://t.me/TasuPremiumBot para obtener acceso exclusivo a contenido premium y tokens! 🪙"
                    f"\n¡Siempre vota por las imágenes de los demás para ganar tokens! 🪙")
        elif language_code == 'fr':
            message = (f"\nVoici votre code de parrainage ! 👇\n"
                    f"\n{referral}\n" 
                    f"\nEnvoyez-le à un ami, s'il démarre le bot, vous obtiendrez 3 jetons 🪙"
                    f"\nAlternativement, vous pouvez acheter un pack sur https://t.me/TasuPremiumBot pour obtenir un accès exclusif au contenu premium et des jetons! 🪙"
                    f"\nVotez toujours pour les images des autres pour gagner des jetons! 🪙")
        elif language_code == 'de':
            message = (f"\nDas ist dein Empfehlungscode! 👇\n"
                    f"\n{referral}\n" 
                    f"\nSenden Sie es einem Freund, wenn er den Bot startet, erhalten Sie 3 Token 🪙"
                    f"\nAlternativ können Sie ein Paket auf https://t.me/TasuPremiumBot kaufen, um exklusiven Zugriff auf Premium-Inhalte und Tokens zu erhalten! 🪙"
                    f"\nStimmen Sie immer für die Bilder anderer ab, um Tokens zu verdienen! 🪙")
        elif language_code == 'ru':
            message = (f"\nВот ваш реферальный код! 👇\n"
                    f"\n{referral}\n" 
                    f"\nОтправьте его другу, если он запустит бот, вы получите 3 токена 🪙"
                    f"\nВ альтернативном случае вы можете купить пакет на https://t.me/TasuPremiumBot, чтобы получить эксклюзивный доступ к премиум-контенту и токенам! 🪙"
                    f"\nВсегда голосуйте за изображения других, чтобы заработать токены! 🪙")
        elif language_code == 'uk':
            message = (f"\nОсь ваш реферальний код! 👇\n"
                    f"\n{referral}\n" 
                    f"\nНадішліть його другу, якщо він запустить бота, ви отримаєте 3 токени 🪙"
                    f"\nАльтернативно, ви можете придбати пакет на https://t.me/TasuPremiumBot, щоб отримати ексклюзивний доступ до преміум-контенту та токенів! 🪙"
                    f"\nЗавжди голосуйте за зображення інших, щоб заробити токени! 🪙")
        elif language_code == 'zh':
            message = (f"\n这是您的推荐代码！👇\n"
                    f"\n{referral}\n" 
                    f"\n将其发送给朋友，如果他们启动了机器人，您将获得3个代币 🪙"
                    f"\n或者，您可以在 https://t.me/TasuPremiumBot 购买一个包，以获得独家访问高级内容和代币！ 🪙"
                    f"\n始终为他人的图像投票以赚取代币！ 🪙")
        elif language_code == 'ar':
            message = (f"\nهذا هو رمز الإحالة الخاص بك! 👇\n"
                    f"\n{referral}\n" 
                    f"\nأرسله إلى صديق ، إذا بدأ البوت ، ستحصل على 3 رموز 🪙"
                    f"\nبدلاً من ذلك ، يمكنك شراء حزمة على https://t.me/TasuPremiumBot للحصول على وصول حصري إلى المحتوى الرئيسي والرموز! 🪙"
                    f"\nصوت دائمًا لصور الآخرين لكسب الرموز! 🪙")
        else:
            message = eng
        return message
    
    def wait_for_next(self, language_code, contest):
        eng = f"You have already submitted an image to the channel,\nplease wait for the next contest.\nEstimated time for the next contest: {contest}\n"
        if language_code == 'it':
            message = (f"Hai già inviato un'immagine al canale,\n"
                       "per favore attendi il prossimo concorso.\n"
                    f"Tempo stimato per il prossimo concorso: {contest}\n")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"आपने पहले ही चैनल को एक छवि भेज दी है,\nकृपया अगले प्रतियोगिता का इंतजार करें।\nअगले प्रतियोगिता के लिए अनुमानित समय: {contest}\n"
        elif language_code == 'es':
            message = f"Ya has enviado una imagen al canal,\npor favor espera al próximo concurso.\nTiempo estimado para el próximo concurso: {contest}\n"
        elif language_code == 'fr':
            message = f"Vous avez déjà soumis une image au canal,\nveuillez attendre le prochain concours.\nTemps estimé pour le prochain concours: {contest}\n"
        elif language_code == 'de':
            message = f"Du hast bereits ein Bild an den Kanal gesendet,\nbitte warte auf den nächsten Wettbewerb.\nGeschätzte Zeit für den nächsten Wettbewerb: {contest}\n"
        elif language_code == 'ru':
            message = f"Вы уже отправили изображение в канал,\nпожалуйста, подождите следующего конкурса.\nПредполагаемое время следующего конкурса: {contest}\n"
        elif language_code == 'uk':
            message = f"Ви вже надіслали зображення до каналу,\nбудь ласка, зачекайте на наступний конкурс.\nОчікуваний час наступного конкурсу: {contest}\n"
        elif language_code == 'zh':
            message = f"您已经向频道提交了一张图片，\n请等待下一场比赛。\n下一场比赛的预计时间: {contest}\n"
        elif language_code == 'ar':
            message = f"لقد قمت بإرسال صورة بالفعل إلى القناة،\nيرجى الانتظار للمسابقة القادمة.\nالوقت المقدر للمسابقة القادمة: {contest}\n"
        else:
            message = eng
        return message

    def your_friend_joined(self, language_code):
        eng = "Congratulation your friend joined!, now you have +3 Token🎉"
        if language_code == 'it':
            message = "Congratulazioni, il tuo amico si è unito, ora hai +3 Token🎉"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "बधाई हो, आपका दोस्त शामिल हो गया है, अब आपके पास +3 टोकन हैं🎉"
        elif language_code == 'es':
            message = "¡Felicidades, tu amigo se unió!, ¡ahora tienes +3 Tokens🎉!"
        elif language_code == 'fr':
            message = "Félicitations, votre ami a rejoint !, maintenant vous avez +3 Tokens🎉"
        elif language_code == 'de':
            message = "Herzlichen Glückwunsch, dein Freund ist beigetreten!, jetzt hast du +3 Tokens🎉"
        elif language_code == 'ru':
            message = "Поздравляем, ваш друг присоединился!, теперь у вас есть +3 Токена🎉"
        elif language_code == 'uk':
            message = "Вітаємо, ваш друг приєднався!, зараз у вас є +3 Токени🎉"
        elif language_code == 'zh':
            message = "恭喜您的朋友加入了！现在你有 +3 代币🎉"
        elif language_code == 'ar':
            message = "تهانينا انضم صديقك!, الآن لديك +3 رمز🎉"
        else:
            message = eng
        return message

    def competition(self, language_code):
        eng = "Send to participate in the competition! 🎁"
        if language_code == 'it':
            message = "Invia per partecipare al concorso! 🎁"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "प्रतियोगिता में भाग लेने के लिए भेजें! 🎁"
        elif language_code == 'es':
            message = "¡Envía para participar en el concurso! 🎁"
        elif language_code == 'fr':
            message = "Envoyez pour participer au concours! 🎁"
        elif language_code == 'de':
            message = "Senden Sie, um am Wettbewerb teilzunehmen! 🎁"
        elif language_code == 'ru':
            message = "Отправьте, чтобы участвовать в конкурсе! 🎁"
        elif language_code == 'uk':
            message = "Надішліть, щоб прийняти участь у конкурсі! 🎁"
        elif language_code == 'zh':
            message = "发送参加比赛！🎁"
        elif language_code == 'ar':
            message = "أرسل للمشاركة في المسابقة! 🎁"
        else:
            message = eng
        return message

    def have_not_token(self, language_code):
        eng = "Oops... You don't have any more tokens! Purchase them at https://t.me/TasuPremiumBot or follow the instructions with /start"
        if language_code == 'it':
            message = "Ops... Non hai più token! Acquistali su https://t.me/TasuPremiumBot o segui le istruzioni con /start"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "उपस्थिति नहीं... आपके पास और कोई टोकन नहीं हैं! उन्हें https://t.me/TasuPremiumBot पर खरीदें या /start के साथ निर्देशों का पालन करें"
        elif language_code == 'es':
            message = "¡Vaya... No tienes más tokens! Adquiérelos en https://t.me/TasuPremiumBot o sigue las instrucciones con /start"
        elif language_code == 'fr':
            message = "Oops... Vous n'avez plus de jetons ! Achetez-les sur https://t.me/TasuPremiumBot ou suivez les instructions avec /start"
        elif language_code == 'de':
            message = "Hoppla... Du hast keine Token mehr! Kaufe sie unter https://t.me/TasuPremiumBot oder befolge die Anweisungen mit /start"
        elif language_code == 'ru':
            message = "Упс... У вас больше нет токенов! Приобретите их на https://t.me/TasuPremiumBot или следуйте инструкциям с помощью /start"
        elif language_code == 'uk':
            message = "Упс... У вас більше немає токенів! Придбайте їх на https://t.me/TasuPremiumBot або дотримуйтеся інструкцій за допомогою /start"
        elif language_code == 'zh':
            message = "糟糕... 你没有更多的代币了！在 https://t.me/TasuPremiumBot 购买或按照 /start 的说明操作"
        elif language_code == 'ar':
            message = "وجه السهو... ليس لديك المزيد من التوكنات! اشترِها على https://t.me/TasuPremiumBot أو اتبع التعليمات باستخدام /start"
        else:
            message = eng
        return message
    
    def send_for_contest(self, language_code, estimated_time):
        eng = f"The contest ends on {estimated_time}, until then you cannot send any more images.\nDo you want to continue?"
        if language_code == 'it':
            message = (f"Il concorso finisce il {estimated_time} fino ad allora non potrai inviare altre immagini.\nVuoi continuare?")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"कॉन्टेस्ट समाप्त होता है {estimated_time} को, तब तक आप और छवियाँ नहीं भेज सकते।\nक्या आप जारी रखना चाहते हैं?"
        elif language_code == 'es':
            message = f"El concurso finaliza el {estimated_time}, hasta entonces no podrás enviar más imágenes.\n¿Deseas continuar?"
        elif language_code == 'fr':
            message = f"Le concours se termine le {estimated_time}, jusqu'à cette date, vous ne pourrez pas envoyer d'autres images.\nSouhaitez-vous continuer?"
        elif language_code == 'de':
            message = f"Der Wettbewerb endet am {estimated_time}, bis dahin können Sie keine weiteren Bilder senden.\nMöchten Sie fortfahren?"
        elif language_code == 'ru':
            message = f"Конкурс заканчивается {estimated_time}, до этого времени вы не можете отправлять больше изображений.\nХотите продолжить?"
        elif language_code == 'uk':
            message = f"Конкурс закінчується {estimated_time}, до цього часу ви не можете надсилати інші зображення.\nБажаєте продовжити?"
        elif language_code == 'zh':
            message = f"比赛截止日期为{estimated_time}，在此之前您将无法发送更多图片。\n您要继续吗？"
        elif language_code == 'ar':
            message = f"ينتهي المسابقة في {estimated_time}، حتى ذلك الوقت لن تتمكن من إرسال المزيد من الصور.\nهل ترغب في الاستمرار؟"
        else:
            message = eng
        return message
    
    def send_for_contest_v2(self, language_code):
        eng = f"The contest ends in one week, until then you cannot send any more images.\nDo you want to continue?"
        if language_code == 'it':
            message = (f"Il concorso finisce tra una settimana, fino ad allora non potrai inviare altre immagini.\nVuoi continuare?")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"कॉन्टेस्ट एक सप्ताह में समाप्त होता है, तब तक आप और छवियाँ नहीं भेज सकते।\nक्या आप जारी रखना चाहते हैं?"
        elif language_code == 'es':
            message = f"El concurso termina en una semana, hasta entonces no podrás enviar más imágenes.\n¿Deseas continuar?"
        elif language_code == 'fr':
            message = f"Le concours se termine dans une semaine, jusqu'à cette date, vous ne pourrez pas envoyer d'autres images.\nSouhaitez-vous continuer?"
        elif language_code == 'de':
            message = f"Der Wettbewerb endet in einer Woche, bis dahin können Sie keine weiteren Bilder senden.\nMöchten Sie fortfahren?"
        elif language_code == 'ru':
            message = f"Конкурс заканчивается через неделю, до этого времени вы не можете отправлять больше изображений.\nХотите продолжить?"
        elif language_code == 'uk':
            message = f"Конкурс закінчується через тиждень, до цього часу ви не можете надсилати інші зображення.\nБажаєте продовжити?"
        elif language_code == 'zh':
            message = f"比赛将在一周内结束，在此之前您将无法发送更多图片。\n您要继续吗？"
        elif language_code == 'ar':
            message = f"ينتهي المسابقة في غضون أسبوع واحد، حتى ذلك الوقت لن تتمكن من إرسال المزيد من الصور.\nهل ترغب في الاستمرار؟"
        else:
            message = eng
        return message

    
    def yes(self, language_code):
        eng = f"Yes ✅"
        if language_code == 'it':
            message = f"Si ✅"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"हां ✅"
        elif language_code == 'es':
            message = f"Sí ✅"
        elif language_code == 'fr':
            message = f"Oui ✅"
        elif language_code == 'de':
            message = f"Ja ✅"
        elif language_code == 'ru':
            message = f"Да ✅"
        elif language_code == 'uk':
            message = f"Так ✅"
        elif language_code == 'zh':
            message = f"是 ✅"
        elif language_code == 'ar':
            message = f"نعم ✅"
        else:
            message = eng
        return message

    def no(self, language_code):
        eng = f"No ❌"
        if language_code == 'it':
            message = f"No ❌"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"नहीं ❌"
        elif language_code == 'es':
            message = f"No ❌"
        elif language_code == 'fr':
            message = f"Non ❌"
        elif language_code == 'de':
            message = f"Nein ❌"
        elif language_code == 'ru':
            message = f"Нет ❌"
        elif language_code == 'uk':
            message = f"Ні ❌"
        elif language_code == 'zh':
            message = f"不 ❌"
        elif language_code == 'ar':
            message = f"لا ❌"
        else:
            message = eng
        return message
    
    def send_to_channel(self, language_code):
        eng = f"Participate in the contest 🎁"
        if language_code == 'it':
            message = f"Partecipa al concorso 🎁"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"कॉन्टेस्ट में भाग लें 🎁"
        elif language_code == 'es':
            message = f"Participa en el concurso 🎁"
        elif language_code == 'fr':
            message = f"Participez au concours 🎁"
        elif language_code == 'de':
            message = f"Nehmen Sie am Wettbewerb teil 🎁"
        elif language_code == 'ru':
            message = f"Участвуйте в конкурсе 🎁"
        elif language_code == 'uk':
            message = f"Беріть участь у конкурсі 🎁"
        elif language_code == 'zh':
            message = f"参加比赛 🎁"
        elif language_code == 'ar':
            message = f"شارك في المسابقة 🎁"
        else:
            message = eng
        return message
