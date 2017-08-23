import urllib.request
from mattermost_bot.bot import listen_to

url = "https://openapi.naver.com/v1/papago/n2mt"
client_id = "wKOZcCkGQxiGdupU8v3r"
client_secret = "IarhyEUKru"


@listen_to('enko (.*)')
def En2ko(message,input):
    data = "source=en&target=ko&text=" + input
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        input = response_body.decode('utf-8')
        splited = input.split('translatedText":"')
        moresplited = splited[1].split('"}}}')
        message.reply('%s' % moresplited[0])
    else:
        print("Error Code:" + rescode)


En2ko.__doc__ = "Translate English to Korean"
