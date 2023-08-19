import base64
from hoshino import Service
from nonebot.message import CQEvent
from hoshino.typing import MessageSegment

sv = Service('尊嘟假嘟转换器', enable_on_default=True)
help_txt = """
h2z[人类语]:人类语转尊嘟语(human to zundu)
z2h[尊嘟语]:尊嘟语转人类语(zundu to human)
""".strip()

#GPT转换的源码
b64 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
leftEye = ['o', '0', 'O', 'Ö']
mouth = ['w', 'v', '.', '_']
rightEye = ['o', '0', 'O', 'Ö']
table = []

separator = ' '

def makeTable():
  for i in range(4):
    for j in range(4):
      for k in range(4):
        table.append(leftEye[i] + mouth[j] + rightEye[k])

makeTable()

def addCalls(t):
  return t

def human2zdjd(t):
  t = base64.b64encode(t.encode('utf-8')).decode('utf-8')
  lent = len(t)
  arr = []

  for i in range(lent):
    c = t[i]
    n = b64.index(c)
    arr.append(table[n])

  data = separator.join(arr)
  return addCalls(data)

def zdjd2human(t):
  arr = t.split(separator)
  lent = len(arr)
  resultArr = []
  
  for i in range(lent):
    c = arr[i]
    if not c:
      continue
    n = table.index(c)
    if n < 0:
      raise ValueError('Invalid zdjd code')
    resultArr.append(b64[n])

  t = ''.join(resultArr)
  t = base64.b64decode(t).decode('utf-8')
  return t

def isZdjd(t):
  try:
    zdjd2human(t)
    return True
  except:
    return False
#GPT转换的源码

#人类语转尊嘟语
@sv.on_prefix('h2z')
async def h2z(bot,ev):
    msg = ev.message.extract_plain_text().strip()
    if msg == '':
        msg = '你所热爱的就是你的生活'
    msg = human2zdjd(msg)
    await bot.send(ev,msg)

#尊嘟语转人类语
@sv.on_prefix('z2h')
async def z2h(bot,ev):
    msg = ev.message.extract_plain_text().strip()
    if msg == '':
        await bot.send(ev,'ov0 O_Ö owO 0wo ovO O_O Ö_O owo ov0 Ö_o Ö_O 0v0 ovO O_O Ö_O o_0 ovO o.Ö 0wO 0_0')
        return
    is_zd = isZdjd(msg)
    if not is_zd:
        await bot.send(ev,'你这是假的尊嘟语!')
        return
    msg = zdjd2human(msg)
    await bot.send(ev,msg)