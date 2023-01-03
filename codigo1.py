print('***Bem vindo a Loja do Aelton Wernek Mattos***') #Nome do aluno
valor_unidade = float(input('Entre com o valor do produto: ')) #
valor_quantidade = int(input('Entre com o quantidade do produto: '))
sub_total = float(valor_quantidade * valor_unidade) # Multiplica os valores recebidos pelo input.

frete1 = 30.00
frete2 = 60.00
frete3 = 120.00
frete4 = 240.00

if 0 <= valor_quantidade < 11: #Se a quantidade estiver entre 0 e 11 vai executar esse if.
  total = sub_total + frete1
  print('Valor sem o frete foi: R$ {:.2f} \nValor com o frete foi: R$ {:.2f}   (Valor do frete: R$ {})'.format(sub_total,total,frete1))
