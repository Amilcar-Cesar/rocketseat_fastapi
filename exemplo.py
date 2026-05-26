class ContextoSimples:
    def __enter__(self):
        print("Iniciar conexão")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finalizar conexão")
        return self
    
with ContextoSimples() as cs:
    print("Execucao em banco de dados")