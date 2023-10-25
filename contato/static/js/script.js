document.addEventListener('DOMContentLoaded', function(){
    const formulario = document.getElementById('formulario__deletar')
    const botao =  document.getElementById('botao__deletar')

    botao.addEventListener('click', function(){
        const confirmacao = confirm('Tem certeza que deseja deletar esse contato?')
        if (confirmacao){
            formulario.submit()
        }
    })
})