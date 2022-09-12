class jogador:
  def __init__(self, nome, idade, time):
      self.nome = nome
      self.idade = idade
      self.time = time


class jogadas(jogador):
  def __init__(self,ass, ft, ff, gol, rb, fd, pe, ca, cv, gc, fc, pp, i):
      self.ass = ass
      self.ft = ft
      self.ff = ff
      self.gol = gol
      self.rb = rb
      self.fd = fd
      self.pe = pe
      self.ca = ca
      self.cv = cv
      self.gc = gc
      self.fc = fc
      self.pp = pp
      self.i = i


  def jogada(self):
      pontosn = float(self.pe * -0.3) + (self.ca * -2) + (self.cv * -5) + (self.gc * -5) + (self.fc * -0.5) + (self.pp * -4) + (self.i * -0.5)
      pontop = float(self.ass * 3) + (self.ft * 3) + (self.ff * 0.8) + (self.gol * 8) + (self.rb * 1.5) + (self.fd * 1.2)
      cal = pontop - pontosn
      while cal > 50:
          print("bom desempenho")
          break
      if cal <= 50 :
          print("desempenho mediano")
      elif cal < 10:
          print('pessimo rendimento')
      return cal

n1 = (input("Nome do jogador: "))
i1 = (input("Idade: "))
t1 = (input("Time: "))

print('+=+=+=++=+==++=+=+=+=+')
print('        JOGADAS       ')
print('+=+=+=++=+==++=+=+=+=+')

ass = float(input("NÚMERO DE ASSISTÊNCIA: "))
ft = float(input("NÚMERO DE FINALIZAÇÕES NA TRAVE: "))
ff = float(input("NÚMERO DE FINALIZAÇÕES PARA FORA: "))
gol = float(input("NÚMERO DE GOLS: "))
rb = float(input("NÚMERO DE ROUBADAS DE BOLAS: "))
fd = float(input("NÚMERO DE FINALIZAÇÕES DEFENDIDAS: "))
pe = float(input('PASSES ERRADOS:'))
ca = float(input('CARTÃO AMARELO:'))
cv = float(input('CARTÃO VERMELHO:'))
gc = float(input('GOLS CONTRA'))
fc = float(input('FALTAS COMETIDAS'))
pp = float(input('PENALTI PERDIDO'))
i = float(input('IMPEDIMENTO'))


jb = jogadas(ass, ft, ff, gol, rb, fd, pe, ca, cv, gc, fc, pp, i)

print('+=+=+=++=+==++=+=+=+=+')
print('       PONTUAÇÃO      ')
print('+=+=+=++=+==++=+=+=+=+')

print("NOME:{}".format(n1))
print('idade:{}'.format(i1))
print('time:{}'.format(t1))
print("pontução da semana:{}".format(jb.jogada()))



