import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')
        
    def abrirConexao(self):
        try:
          self.connection = psycopg2.connect(user="postgres",
                                  password="110793",
                                  host="localhost",
                                  port="5432",
                                  database="aplication")
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

#Seleciona todos os Clientes
                
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
    
            print("Selecionando todos os produtos")
            sql_select_query = """select * from cliente """
                    
            
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()             
            print(registros)
                
    
        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)
    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

#Inserir Cliente
                
    def inserirDados(self, cod_cliente, nome, email):
        try:
          self.abrirConexao()
          cursor = self.connection.cursor()
          postgres_insert_query = """ INSERT INTO cliente
          ("cod_cliente", "nome", "email") VALUES (%s,%s,%s)"""
          record_to_insert = (cod_cliente, nome, email)
          cursor.execute(postgres_insert_query, record_to_insert)
          self.connection.commit()
          count = cursor.rowcount
          print (count, "Registro inserido com successo na tabela")
        except (Exception, psycopg2.Error) as error :
          if(self.connection):
              print("Falha ao inserir registro na tabela", error)
        finally:
            #closing database connection.
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
                

#Atualizar Cliente
              
    def atualizarDados(self, cod_cliente, nome, email):
        try:
            self.abrirConexao()    
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from cliente
            where "cod_cliente" = %s"""
            cursor.execute(sql_select_query, (cod_cliente,))
            record = cursor.fetchone()
            print(record)    
            # Atualizar registro
            sql_update_query = """Update cliente set "nome" = %s, 
            "email" = %s where "cod_cliente" = %s"""
            cursor.execute(sql_update_query, (nome, email, cod_cliente))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")    
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from cliente"
            where "cod_cliente" = %s"""
            cursor.execute(sql_select_query, (cod_cliente,))
            record = cursor.fetchone()
            print(record)    
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")


#Excluir Cliente
             
    def excluirDados(self, cod_cliente):
        try:
            self.abrirConexao()    
            cursor = self.connection.cursor()    
            # Atualizar registro
            sql_delete_query = """Delete from cliente
            where "cod_cliente" = %s"""
            cursor.execute(sql_delete_query, (cod_cliente, ))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")        
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
                

