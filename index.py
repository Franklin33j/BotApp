from  telegram import Update
from  telegram.ext  import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN='6577319166:AAGR34qIvs_yrkZ0mBQDRlwBzV7HQf9h2Hg'
USUARIO='Franklinbot'




async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Hola, soy Franklin Boot hecho para vos Azucena, ingresa el comando proporcionado')

async def micumple24(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
    Quiero desearte ante todo Feliz Cumpleaños 🎈🎈🎉✨🎁🎁🎀.\n Te deseo lo mejor por ser una gran amiga perseverante, por ser una gran persona, ojala y me apartes pastel, jajaja.Te escribo 5 razones por la que sos una persona valiosa para mi, para leerlas escribe por ejemplo /reason1 hasta /reason5, con todo cariño.
    """
    await update.message.reply_text( text)


async def reason1(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
    Tu autenticidad es algo que realmente admiro. Tienes esa maravillosa capacidad de ser tú misma en todo momento, sin la necesidad de pretender ser alguien que no eres. Es algo que te hace tan única y especial para mí, sabiendo que siempre puedo contar contigo siendo genuina y auténtica    
    """
    await update.message.reply_text( text)


async def reason2(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
   Tu forma de ver la vida es realmente inspiradora para mí. Siempre tienes una perspectiva positiva y optimista, incluso en medio de los desafíos más grandes. 
    """
    await update.message.reply_text( text)


async def reason3(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
   Quiero que sepas lo mucho que valoro tu apoyo incondicional. Siempre estás presente para mí, brindándome tu apoyo y cariño sin importar las circunstancias. Tu lealtad y amistad son realmente invaluables para mí 
    """
    await update.message.reply_text( text)


async def reason4(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
   Tu sentido del humor es algo que realmente ilumina mis días. Siempre encuentras la manera de hacerme reír incluso en los momentos más difíciles. Tu humor único y contagioso hace que la vida sea mucho más alegre y divertida. (todos tus supuestos enamorados )
    """
    await update.message.reply_text( text)

async def reason5(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text="""
    Mas que una razon, solo quiero agradecerte por soportarme, gracias azucena por aguantarme, me alegra haber coincido con vos en esta vida, si algun momento nos distanciamos por cosas de la vida, siempre estaras presente en mi ❤.\nTe adjunto un enlace con un pastel(espero lo disfrutes jajajajaj): https://65e72269c2449c0c1ab2d563--nimble-khapse-2ed8d6.netlify.app/ \nUn Par de flores amarilas(huelen rico:): https://flores-azucena.netlify.app/flores. \nPdt: Lo siento por no poder acompañarte.
    """
    await update.message.reply_text( text)

if __name__== '__main__':
    app= Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("micumple24", micumple24))
    app.add_handler(CommandHandler("reason1", reason1))
    app.add_handler(CommandHandler("reason2", reason2))
    app.add_handler(CommandHandler("reason3", reason3))
    app.add_handler(CommandHandler("reason4", reason4))
    app.add_handler(CommandHandler("reason5", reason5))
    app.run_polling(poll_interval=2)