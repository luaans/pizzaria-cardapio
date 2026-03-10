import {useState} from "react"
import StepQuantidade from "./components/StepQuantidade"
import StepPizza from "./components/StepPizza"
import StepBebidas from "./components/StepBebidas"
import StepCliente from "./components/StepCliente"
import StepResumo from "./components/StepResumo"


function App() {

  const [step, setStep] = useState(1) // COntrola qual tela aparece
  const [quantidade, setQuantidade] = useState(0) // Guarda a quantidade de pizzas que o cliente escolheu 
    
  return(

    <div>
       <h1>🍕 Pizzaria Shabaz!</h1>

       {step === 1 && (<StepQuantidade setStep={setStep} setQuantidade={setQuantidade}/>)}

       {step === 2 && <StepPizza setStep={setStep}/>}
       {step === 3 && <StepBebidas setStep={setStep}/>}
       {step === 4 && <StepCliente setStep={setStep}/>}
       {step === 5 && <StepResumo setStep={setStep}/>}
    </div>
  )

}

export default App