print('Saiba se você passou de ano:')
nota1 = float(input('Primeira nota'))
nota2 = float(input('Segunda nota'))
nota3 = float(input('Terceira nota'))
media = (nota1 + nota2 + nota3) / 2
print ('Tirando {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, nota3, media))

if 6 > media:
    print('Você foi REPROVADO, não fique triste.')

elif 6 < media:
    print('Você foi APROVADO, parabéns!')
