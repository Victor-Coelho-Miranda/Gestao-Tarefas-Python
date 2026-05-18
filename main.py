tarefas = []

def adicionar_tarefa(descricao, prazo="Sem prazo", urgencia="Normal"):
    """
    Adiciona uma nova tarefa à lista.

    Parâmetros:
    descricao (str): descrição da tarefa
    prazo (str): prazo final da tarefa
    urgencia (str): nível de urgência

    Retorno:
    descrição: tarefa criada
    """

    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "prazo": prazo,
        "urgencia": urgencia,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    return tarefa


def listar_tarefas():
    """
    Lista todas as tarefas cadastradas.
    """

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        print(f"""
ID: {tarefa["id"]}
Descrição: {tarefa["descricao"]}
Prazo: {tarefa["prazo"]}
Urgência: {tarefa["urgencia"]}
Status: {tarefa["status"]}
-----------------------------
""")


def concluir_tarefa(id_tarefa):
    """
    Marca uma tarefa como concluída.

    Parâmetros:
    id_tarefa (int): ID da tarefa
    """

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "Concluída"
            print("\nTarefa concluída com sucesso!\n")
            return

    print("\nTarefa não encontrada.\n")


def remover_tarefa(id_tarefa):
    """
    Remove uma tarefa da lista.

    Parâmetros:
    id_tarefa (int): ID da tarefa
    """

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            print("\nTarefa removida com sucesso!\n")
            return

    print("\nTarefa não encontrada.\n")

while True:

    print("""
===== MENU =====

1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        descricao = input("Descrição da tarefa: ")
        prazo = input("Prazo da tarefa: ")
        urgencia = input("Urgência (Baixa/Normal/Alta): ")

        adicionar_tarefa(
            descricao=descricao,
            prazo=prazo,
            urgencia=urgencia
        )

        print("\nTarefa adicionada com sucesso!\n")

    elif opcao == "2":

        listar_tarefas()

    elif opcao == "3":

        id_tarefa = int(input("Digite o ID da tarefa: "))
        concluir_tarefa(id_tarefa)

    elif opcao == "4":

        id_tarefa = int(input("Digite o ID da tarefa para remover: "))
        remover_tarefa(id_tarefa)

    elif opcao == "5":

        print("\nEncerrando sistema...")
        break

    else:

        print("\nOpção inválida.\n")