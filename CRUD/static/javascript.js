(function(win, doc){
    'use strict'
    if(doc.querySelector('.btn_deletar')){
        let btn_deletar = doc.querySelectorAll('.btn_deletar');
        for(let i=0; i < btn_deletar.length; i++){
            btn_deletar[i].addEventListener('click', function(event){
                if(confirm('Deseja Continuar? Esta ação não poderá ser desfeita!')){
                    return true;
                }else{
                    event.preventDefault();
                }
            }
            )
        }
    }

    //Ajax form
    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        function sendForm(event){
            event.preventDefault()
            let data = new FormData(form)
            let ajax = new XMLHttpRequest()
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action)
            ajax.setRequestHeader('X-CSRF-TOKEN', token)
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    let resultado = doc.querySelector('#resultado')
                    resultado.innerHTML = 'Cadastro realizado com sucesso'
                    resultado.classList.add('alert')
                    resultado.classlist.add('alert-success')
                }
            }
            ajax.send(data)
            form.reset()
        }
        form.addEventListener('submit', sendForm, false)
    }

})(window, document);