class GerenciamentoNotas:
    def calcular_media(self, n1, n2):
        media = (n1 + n2)/2 
        return media

    def validar_nota(self, media):
        if media >= 7:
            return "Foi aprovado!"
        elif media < 7 and media >= 5:
            return "Está em recuperação!"
        else: 
            return "Foi reprovado!"


            

        