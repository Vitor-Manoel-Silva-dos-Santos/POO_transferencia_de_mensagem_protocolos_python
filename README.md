# Transferências de mensagens:
## para que seja enviado uma mensagem deve-se seguir alguns parâmetros, onde cada parâmetro possui uma camada.
### Ao instânciar um objeto, deve-se passar os parâmetros mensagem, eletronica, endereco, internet, enviar, receber. 
###     ***Todos os parâmetros devem ser verdadeiros para que ocorra o envio da mensagem.

    -   eletronica: Estado do Hardware 
    -   endereço: Ip ou número de telefone 
    -   internet: Conexão com internet 
    -   Enviar: deve-se enviar? 
    -   Receber: deve-se receber?

### Camadas dos protocolos:
- camadaum(self)
    -    Verifica se o hardware está coerente.
- camadadois(self)
    -   verifica se o endereço do destinatário está coerente.
- camadatres(self)
    -   Verifica conexão com internet e faz a separação da mensagem em pacotes ao qual será enviada.
-   camadaquatro(self)
    -   Verifica se a mensagem deve ser enviada e recebida e envia a mensagem para camada 5.
-   camadacinco(self)
    -   verifica se todos os parâmetros realmente são verdadeiros, assim, unindo os pacotes e enviando a mensagem.
    