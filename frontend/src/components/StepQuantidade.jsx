function StepQuantidade({ setStep, setQuantidade }) {

    function escolherQuantidade(qtd){
        setQuantidade(qtd)
        setStep(2)
    }

    return (

        <div>
        
           <h2>Quantas pizzas você deseja ?</h2>

           <button onClick={() => escolherQuantidade(1)}> 1 Pizza </button>
           <button onClick={() => escolherQuantidade(2)}> 2 Pizzas </button>
           <button onClick={() => escolherQuantidade(3)}> 3 Pizzas </button>

        </div>
    )
}

export default StepQuantidade