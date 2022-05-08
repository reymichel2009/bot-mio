import requests
import hello
import perfil
import config

print ('Este es un bot de prueba toca el comando /help')

# comandos de admin
        if '/add' in msgText:
            isadmin = jdb.is_admin(username)
            if isadmin:
                try:
                    user = str(msgText).split(' ')[1]
                    jdb.create_user(user)
                    jdb.save()
                    msg = 'Ahora @'+user+' tiene acceso al bot temporalmente'
                    bot.sendMessage(update.message.chat.id,msg)
                except:
                    bot.sendMessage(update.message.chat.id,f'❌Error en el comando /add user❌')
            else:
                bot.sendMessage(update.message.chat.id,'❌Usted no tiene los privilegios para usar este comando❌')
            return

 # comandos de usuario
        if '/help' in msgText:
            tuto = open('help.txt','r')
            bot.sendMessage(update.message.chat.id,tuto.read())
            tuto.close()
            return