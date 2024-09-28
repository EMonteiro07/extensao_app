import tkinter as tk
from tkinter import ttk
import crud as crud
from tkinter import messagebox as mb

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()  
        #componentes
        self.lbCod_cliente=tk.Label(win, text='Código do Cliente:')
        self.lblNome=tk.Label(win, text='Nome:')
        self.lblEmail=tk.Label(win, text='E-mail:')
        
        self.txtCod_cliente=tk.Entry(bd=3, width=30)
        self.txtNome=tk.Entry(width=30)
        self.txtEmail=tk.Entry(width=30)        
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarCliente, cursor="hand2")        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarCliente, cursor="hand2")        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirCliente, cursor="hand2")        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela, cursor="hand2")     
                   
        #ComponenteTreeVie
        self.dadosColunas =("Código Cliente", "Nome", "E-mail")            
                
        self.treeProdutos = ttk.Treeview(win, 
                                       columns=self.dadosColunas,
                                       selectmode='browse', show='headings')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='right', fill ='x')
                                
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        
        self.treeProdutos.heading("Código Cliente", text="Código Cliente")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("E-mail", text="E-mail")

        
        self.treeProdutos.column("Código Cliente",minwidth=0,width=100, anchor="center")
        self.treeProdutos.column("Nome",minwidth=0,width=200)
        self.treeProdutos.column("E-mail",minwidth=0,width=220)
        self.treeProdutos.pack(padx=10, pady=10)
        
        self.treeProdutos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados)                  
         
        #posicionamento dos componentes na janela
                    
        self.lbCod_cliente.place(x=100, y=50)
        self.txtCod_cliente.place(x=250, y=50)
        
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        
        self.lblEmail.place(x=100, y=150)
        self.txtEmail.place(x=250, y=150)
               
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
                   
        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)        
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            cod_cliente,nome,email = item["values"][0:3]  
            self.txtCod_cliente.insert(0, cod_cliente)  
            self.txtNome.insert(0, nome)  
            self.txtEmail.insert(0, email)  

    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros=self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              cod_cliente=item[0]
              nome=item[1]
              email=item[2]
              print("Código Cliente = ", cod_cliente)
              print("Nome = ", nome)
              print("E-mail  = ", email, "\n")
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(cod_cliente,
                                           nome,
                                           email))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar')            

#LerDados da Tela
          
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          cod_cliente = int(self.txtCod_cliente.get())
          print('codigo Cliente', cod_cliente)
          nome=self.txtNome.get()
          print('nome', nome)
          email=self.txtEmail.get()          
          print('E-mail', email)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return cod_cliente, nome, email

#Cadastrar Cliente
        
    def fCadastrarCliente(self):
        try:
          print("************ dados dsponíveis ***********") 
          cod_cliente, nome, email= self.fLerCampos()                    
          self.objBD.inserirDados(cod_cliente, nome, email)                    
          self.treeProdutos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(cod_cliente,
                                        nome,
                                        email))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fLimparTela()
          mb.showinfo("Sucesso","Cliente cadastrado com sucesso")
          print('Cliente Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')

#Atualizar Cliente
        
    def fAtualizarCliente(self):
        try:
          if mb.askyesno("Verificar", "Deseja realmente atualizar o Cliente?"):
            print("************ dados dsponíveis ***********")        
            cod_cliente, nome, email= self.fLerCampos()
            self.objBD.atualizarDados(cod_cliente, nome, email)          
            #recarregar dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children()) 
            self.carregarDadosIniciais()
            self.fLimparTela()
            mb.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            print('Cliente Atualizado com Sucesso!')
          else:
             mb.showinfo("no", "Atualização foi cancelada")        
        except:
          print('Não foi possível fazer a atualização.')

#Excluir Cliente
                
    def fExcluirCliente(self):
        try:
          if mb.askyesno("Verificar", "Deseja realmente excluir o Cliente?"):
            print("************ dados dsponíveis ***********")        
            cod_cliente, nome, email= self.fLerCampos()
            self.objBD.excluirDados(cod_cliente)          
            #recarregar dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children()) 
            self.carregarDadosIniciais()
            self.fLimparTela()
            mb.showinfo("Sucesso","Cliente excluido com sucesso")
            print('Cliente Excluído com Sucesso!')
          else:
             mb.showinfo("No", "A exclusão foi cancelada")
        except:
          print('Não foi possível fazer a exclusão do produto.')
        

#Limpar Tela
           
    def fLimparTela(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtCod_cliente.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtEmail.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')

 

    

#Programa Principal

            
janela=tk.Tk()
principal=PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("720x600+10+10")
janela.mainloop()

