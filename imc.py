import streamlit as st

imc = 0
imc_delta = 0


with st.sidebar:
    st.title("Cálculadora IMC")

    st.header("IMC: Definição?")

    st.write("Indice de massa corporal (IMC)")

    st.write("É um índice que relaciona peso e altura de uma pessoa")

    st. write("É utilizado como uma medida de saúde geral e para determinar se uma pessoa está em um peso ideal.")

    st.divider()
    st.write("Python com Streamlit by Maurilio Benevento em 06/09/2024")


st.title("Calcule o seu IMC")

peso = st.number_input("Digite o seu peso em kg", min_value=0.0)
altura = st.number_input("Digite a sua altura em metros", min_value=0.0)

if st.button("Calcular"):
    imc = peso / (altura ** 2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal

if imc < 18.5:
    resultado = {
        "classe": 'Abaixo do peso',
        "delta": imc_delta
    }
elif imc >= 18.5 and imc < 25:
    resultado = {
        "classe": 'Peso ideal',
        "delta": imc_delta
    }
elif imc >= 25 and imc < 30:
    resultado = {
        "classe": 'Sobrepeso',
        "delta": imc_delta
    }
elif imc >=30 and imc < 35:
    resultado = {
        "classe": 'Obesidade',
        "delta": imc_delta
    }
else:
    resultado = {
        "classe": 'Morbida',
        "delta": imc_delta
    }


st.write(f"O resultado é {resultado}")

col1, col2 = st.columns(2)

col1.metric("IMC Classificado", resultado["classe"], resultado["delta"], delta_color="inverse")
col2.metric("IMC Calculado", round(imc, 2), delta_color="off")


st.divider()
st.text("fonte:" )
st.image("./img.png")

