TODO:
* Implementar tratamento de status quando o get for None
(Talvez dar um retry para salvar caso não esteja lá,
Fazer uma função apropriada de inicialização de status,
no caso de falha reutilizar ela)
* Implementar status, ideia de schema abaixo
* Implementar serializacao parcial

numbers = fields.List(fields.Float())

{
    "status": 
        {
            "situacao": "P",
	    "porcentagem": 75,
	    "id_ultima_etapa": 1,
	    "ultimo_log": "Aguardando processamento em fila",
	    "logs": [
                {
                    "id_etapa": 1,
                    "logs_etapa": [
                        "log teste um",
                        "log teste dois"
                    ]
                },
                {
                    "id_etapa": 2,
		    "logs_etapa": [
                        "log teste um",
                        "log teste dois"
                    ]
                }
            ],
        }
}

* Colocar no objeto um atributo de status que é obtido
no NOSQL pelo serializer
* Implementar serializer marshmallow
* Implementar redis mais apropriadamente
* Implementar put
* Fazer teste de carga
* Ver limite da fila