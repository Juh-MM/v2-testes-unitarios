from classe import GerenciamentoNotas

def test_media_correta():
    aluno = GerenciamentoNotas()
    assert aluno.calcular_media(8, 6) == 7

def test_aprovado():
    aluno = GerenciamentoNotas()
    assert aluno.validar_nota(8) == "Foi aprovado!"

def test_recuperacao():
    aluno = GerenciamentoNotas()
    assert aluno.validar_nota(6) == "Está em recuperação!"

def test_reprovado():
    aluno = GerenciamentoNotas()
    assert aluno.validar_nota(4) == "Foi reprovado!"