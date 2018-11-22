filenames = ['PacientePossuiCaracteristica.xml', 
                'Classificacao.xml', 
                    'Paciente.xml', 
                        'ClassificacaoTemSintoma.xml',
                            'Caracteristica.xml',
                                'Sintoma.xml']
with open('column.xml', 'w') as outfile:
    outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n<root>\n')
    for fname in filenames:
        with open(fname) as infile:
            next(infile)
            for line in infile:
                outfile.write(line)
    outfile.write('\n</root>\n')
