tarefa1 = {
    "nome": "Estudar Python",
    "categoria": "Estudos",
    "prioridade": "Alta",
    "status": "Concluído"
}

tarefa2 = {
    "nome": "Fazer compras",
    "categoria": "Pessoal",
    "prioridade": "Média",
    "status": "A fazer"
}

tarefa3 = {
    "nome": "Reunião com equipe",
    "categoria": "Trabalho",
    "prioridade": "Alta",
    "status": "Aguardando"
}


tarefas = [tarefa1, tarefa2, tarefa3]

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    categoria = input("Digite a categoria da tarefa: ")
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    status = input("Digite o status (Pendente, Concluído, Aguardando, A fazer): ")

    tarefa = {
        "nome": nome,
        "categoria": categoria,
        "prioridade": prioridade,
        "status": status,
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso btl!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        print("\n Lista de tarefas: ")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['nome']} - {tarefa['categoria']}")
            print(f"(Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']})")

def remover_tarefa():
    listar_tarefas()
    if tarefas:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f" Tarefa '{tarefa_removida['nome']}' removida com sucesso!\n")
        else:
            print("Número inválido man .\n")

def menu():
    while True:
        print("\n=== MENU DE COMANDOS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção ai man: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print(" Saindo do programa...")
            break
        else:
            print(" Opção inválida. Tente novamente.\n")


menu()
