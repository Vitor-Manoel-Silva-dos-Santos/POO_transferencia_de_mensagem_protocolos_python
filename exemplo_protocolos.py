import time
class Transferencia(object):
    '''-    Transferências de mensagens: para que seja enviado uma mensagem deve-se seguir alguns parâmetros, onde
    cada parâmetro possui uma camada.
    -    Ao instânciar um objeto, deve-se passar os parâmetros mensagem, eletronica, endereco, internet, enviar, receber.
    ***Todos os parâmetros devem ser verdadeiros para que ocorra o envio da mensagem.
        eletronica: Estado do Hardware
        endereço: Ip ou número de telefone
        internet: Conexão com internet
        Enviar: deve-se enviar?
        Receber: deve-se receber?'''
    def __init__(self, mensagem='Não foi passado nenhuma mensagem', eletronica = False, endereco = '19216810101', internet = False, enviar = False, receber = False):
        self.mensagem = mensagem
        #camada 1
        self.eletronica = eletronica
        #camada 2
        self.endereco = endereco
        #camada 3
        self.internet = internet
        #camada 4
        self.enviar = enviar
        self.receber = receber
        self.dic = {'Tipo mensagem': type(self.mensagem), 'Estado hardware': self.eletronica, 'Destinatário': self.endereco, 'Conexão com internet': self.internet, 'Enviar': self.enviar, 'Receber': self.receber}

    def __str__(self):
        return f'Existe uma mensagem querendo ser enviada para o destinátario. Chame a função enviar.\n{self.dic}'

    def envie(self):
        '-  Utilizado quando se deseja enviar uma mensagem.'
        self.camadaum()

    def camadaum(self):
        '''-    Verifica se o hardware está coerente.'''
        if self.eletronica == True :
            self.camadadois()
        else:
            print('...Error... A transmissão não respeitou a primeira camada do protocolo!')

    def camadadois(self):
        '''-    verifica se o endereço do destinatário está coerente.'''
        if len(self.endereco) > 5 and len(self.endereco) < 12:
            self.camadatres()
        else:
            print('...Error... A transmissão não respeitou a segunda camada do protocolo!')

    def camadatres(self):
        '''-    Verifica conexão com internet e faz a separação da mensagem em pacotes ao qual será enviada.'''
        self.lista = []
        if self.internet == True:
            for self.valor in self.mensagem:
                self.lista.append(self.valor)
                self.camadaquatro()
        else:
            print('...Error... A transmissão não respeitou a terceira camada do protocolo!')

    def camadaquatro(self):
        '''-    Verifica se a mensagem deve ser enviada e recebida e envia a mensagem para camada 5.'''
        self.a = 0
        self.recebimento = []
        if self.enviar == True and self.receber == True:

            while self.a < len(self.lista):
                time.sleep(0.3)
                self.recebimento.append(self.lista[self.a])
                self.a += 1
                if self.a == len(self.lista):
                    break

        else:
            print('...Error... A transmissão não respeitou a quarta camada do protocolo!')

        self.camadacinco()

    def camadacinco(self):
        '''-    verifica se todos os parâmetros realmente são verdadeiros, assim, unindo os pacotes e enviando a mensagem.'''
        if self.eletronica and self.internet and self.enviar and self.receber == True:
            self.b = ' '
            print(self.recebimento)
            for self.valor in self.recebimento:
                self.b += self.valor
            print('-' * len(self.b))
            print(self.b)
            print('-' * len(self.b))
        else:
            print("...Error... Ocorreu algum erro em alguma camada do protocolo.")

umamensagem = Transferencia('Olá Mundo',True,'123456789',True,True,True)
#print(umamensagem)
#umamensagem.envie()
help(Transferencia)