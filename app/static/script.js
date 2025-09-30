document.addEventListener('DOMContentLoaded',()=>{
    document.querySelectorAll('.check-tarefa').forEach(checkbox =>{

        checkbox.addEventListener('change',function(){

            console.log(checkbox)
            console.log(this.dataset)
            const tarefa_id = this.dataset.tarefaId
            const textoTarefa = document.getElementById(`texto-tarefa-${tarefa_id}`)
            console.log(this.dataset.tarefaId)
            fetch(`/tarefa/concluir/${tarefa_id}`, {
                method: "POST"
            }).then(res => res.json()).then(data=>{
                if(data.status === 'sucesso'){
                    textoTarefa.classList.toggle('concluida',data.concluida)
                }

            }).catch(error=> console.error("Ocorreu um erro: "+ error))

        })

    })
















})