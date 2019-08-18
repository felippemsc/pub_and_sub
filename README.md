TODO:

* Abstrair mudança de status via model 
(colocar funções de mudanças de status no model)

* Implementar redis mais apropriadamente
* Implementar consumer
    * Quando for implementar o schema, serializar a 
      mensagem enviada e instanciar o objeto, dessa maneira
      recuperando o status do mesmo.
* Fazer teste de carga
* Ver limite da fila