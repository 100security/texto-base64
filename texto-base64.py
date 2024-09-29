# 100SECURITY
# Converter Textos e Arquivos <> Base64
# Por: Marcos Henrique
# Site: www.100security.com.br

import base64
import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')

clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.GREEN}Converter Textos e Arquivos <> Base64"
github = f"{Style.BRIGHT}{Fore.WHITE}GitHub: {Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-base64"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Função para converter texto em Base64
def text_to_base64(text):
    base64_encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return base64_encoded

# Função para converter Base64 para texto
def base64_to_text(base64_text):
    text_decoded = base64.b64decode(base64_text.encode('utf-8')).decode('utf-8')
    return text_decoded

# Função para converter arquivo de texto em Base64
def text_file_to_base64(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        base64_encoded = text_to_base64(text)
        return base64_encoded
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter Base64 de arquivo para texto
def base64_file_to_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            base64_text = file.read().strip()
        return base64_to_text(base64_text)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo do arquivo.")

# Função para converter arquivos binários em Base64
def file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        base64_encoded = base64.b64encode(binary_data).decode('utf-8')
        return base64_encoded
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter Base64 de um arquivo para arquivo binário
def base64_file_to_binary(input_file, output_file):
    try:
        # Ler o conteúdo Base64 do arquivo
        with open(input_file, 'r', encoding='utf-8') as file:
            base64_data = file.read().strip()

        # Converter o conteúdo Base64 de volta para binário
        binary_data = base64.b64decode(base64_data)
        
        # Escrever os dados binários no arquivo de saída
        with open(output_file, 'wb') as file:
            file.write(binary_data)
        
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Arquivo {output_file} criado com sucesso!")
    except base64.binascii.Error:
        print(f"{Style.BRIGHT}{Fore.RED}Erro ao converter Base64 para binário. Verifique o conteúdo do arquivo {input_file}.")
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo {input_file} não encontrado.")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.RED}# - - - - - - - - - M E N U - - - - - - - - - #\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Base64")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Base64 {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto.txt {Fore.WHITE}para {Fore.LIGHTYELLOW_EX}Base64")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}base64.txt {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Arquivos {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Base64")
    print(f"{Style.BRIGHT}{Fore.WHITE}6 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Base64 {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Arquivo")
    print(f"{Style.BRIGHT}{Fore.WHITE}7 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para Base64: ")
            base64_result = text_to_base64(texto)
            salvar_em_arquivo('base64.txt', base64_result)
            print(f"Texto original: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
            print(f"Conversão para Base64: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{base64_result}")
        
        elif opcao == '2':
            base64_input = input("Digite o valor Base64: ")
            try:
                texto_result = base64_to_text(base64_input)
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Valor Base64: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{base64_input}")
                print(f"Conversão para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}Entrada inválida. Por favor, insira um Base64 válido.")
        
        elif opcao == '3':
            file_path = input("Digite o nome do arquivo de texto (.txt): ")
            base64_result = text_file_to_base64(file_path)
            if base64_result:
                salvar_em_arquivo('base64.txt', base64_result)
                print(f"Conversão de {file_path} para Base64: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{base64_result}")
        
        elif opcao == '4':
            file_path = input("Digite o nome do arquivo de Base64 (.txt): ")
            texto_result = base64_file_to_text(file_path)
            if texto_result:
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Conversão de {file_path} para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '5':
            file_path = input("Digite o nome do arquivo (ex: imagem.png, arquivo.pdf): ")
            base64_result = file_to_base64(file_path)
            if base64_result:
                salvar_em_arquivo('base64.txt', base64_result)
                print(f"Conversão de {file_path} para Base64: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{base64_result}")
        
        elif opcao == '6':
            input_file = input("Digite o nome do arquivo Base64 (ex: base64.txt): ")
            output_file = input("Digite o nome do arquivo de saída (ex: imagem.png, arquivo.pdf): ")
            base64_file_to_binary(input_file, output_file)

        elif opcao == '7':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
