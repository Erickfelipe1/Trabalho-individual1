################################################### 
# SENAC/RESILIA - Formação em Análise de Dados (FAD) #
# Projeto Individual 1 - Módulo 2 - Deu Match! #
# nome : Erick dos santos silva felipe #
###################################################


print("Seja bem vindo ao seletor de candidatos DEU MATCH !!")
print("-"*50)

import pandas as pd 


seleçao = []          

while True:
  nome = str.title(input("Digite o nome do candidato: "))                                          
  e = int(input("Digite a avaliação da entrevista: "))      
  t = int(input("Digite a avaliação da teste teórico: "))   
  p = int(input("Digite a avaliação da teste prático: "))  
  s = int(input("Digite a avaliação da soft skills: "))     
  seleçao.append([nome,e,t,p,s,f"e{e}_t{t}_p{p}_s{s}"]) 
  
  sair = str.upper(input("Deseja inserir dados de mais candidatos? [S/N] ")) 
  if sair == "N":     
    break
  else:
    pass
  
def encontrar (lista):                 
    
    a=int(input("Vamos começar a pesquisa. Por favor nos diga a nota da entrevista: "))                                                                   
    b = int(input("Agora do teste teórico: "))                                                                                                                 
    c = int(input("E do teste prático? "))                                                                                                                   
    d = int(input("Finalmente a ultima, nos diga a nota do teste de soft skills: "))     
    df = pd.DataFrame(lista)                       
    dff = df[(df[1] >= a) & (df[2] >= b) & (df[3] >= c) & (df[4] >= d)]    
    dff.columns = ["Candidato","e","t","p","s","Resultado"]                   
    dff = dff.drop(["e","t","p","s"], 1)                             
    print("Os candidatos que atendem aos requisitos são :")          
    return (print(dff))                                                     

encontrar (seleçao)              


