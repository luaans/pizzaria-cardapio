import {useState} from "react"

function StepPizza({ setStep }) {

    const [tamanho, setTamanho] = useState("")
    const [sabor, setSabor] = useState("")
    const [borda, setBorda] = useState("")

    const [tamanhos, setTamanhos] = useState([])
    const [sabores, setSabores] = useState([])
    const [bordas, setBordas] = useState([])

    useEffect(() => {

        fetch("http://127.0.0.1:8000/api/cardapio/")
        .then(res => res.json())
        .then(data =>{
            setTamanhos(data.tamanhos)
            setSabores(data.sabores)
            setBordas(data.bordas)
        })
    }, [])

    function continuar() {

        const pizza = {
            tamanho,
            sabor,
            borda
        }

        console.log("Pizza criada:", pizza)

        setStep(3)

        const saboresAgrupados = {
            tradicional: [],
            especial1: [],
            especial2: [],
            doce: []
        }

        sabores.forEach((sabor) => {

            if (saboresAgrupados[sabor.categoria]){
                saboresAgrupados[sabor.categoria].push(sabor)
            }
        }) 
    }

    return(
        
        <div>
 
           <h2>Monte sua pizza 🍕</h2>

           {/* Tamanho */}

           <h3>Tamanho</h3>

           <select value={tamanho} onChange={(e) => setTamanho(e.target.value)}>
            <option value="">Escolha o tamanho</option>
            {tamanhos.map((t, index) =>(
                <option key={index} value={t}>{t}</option>
            ))}
           </select>

           {/* SABOR */}
           
           <h3>Sabor</h3>

            <select
            value={sabor}
            onChange={(e) => setSabor(e.target.value)}
            >

            <option value="">Escolha o sabor</option>

            <optgroup label="Tradicionais">
            {saboresAgrupados.tradicional.map((s) => (
                <option key={s.id} value={s.nome}>
                {s.nome}
                </option>
            ))}
            </optgroup>

            <optgroup label="Especiais 1">
            {saboresAgrupados.especial1.map((s) => (
                <option key={s.id} value={s.nome}>
                {s.nome}
                </option>
            ))}
            </optgroup>

            <optgroup label="Especiais 2">
            {saboresAgrupados.especial2.map((s) => (
                <option key={s.id} value={s.nome}>
                {s.nome}
                </option>
            ))}
            </optgroup>

            <optgroup label="Doces">
            {saboresAgrupados.doce.map((s) => (
                <option key={s.id} value={s.nome}>
                {s.nome}
                </option>
            ))}
            </optgroup>

            </select>

           {/* BORDA */}

           <h3>Sabor</h3>

           <select value={borda} onChange={(e) => setBorda(e.target.value)}>
            <option value="">Escolha a borda</option>

            {bordas.map((b, index) =>(
                <option key={index} value={b}>{b}</option>
            ))}

           </select>



        </div>

    )
}