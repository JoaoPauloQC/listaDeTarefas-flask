document.addEventListener('DOMContentLoaded',()=>{
    document.querySelectorAll('.check-tarefa').forEach(checkbox =>{

        checkbox.addEventListener('change',()=>{

            console.log(checkbox)
            console.log(this.dataset)
            const tarefa_id = this.dataset.tarefa_id
            const textoTarefa = document.getElementById(`texto-tarefa-${tarefa_id}`)

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