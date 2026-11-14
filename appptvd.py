from flask import Flask, jsonify, render_template

app = Flask(__name__)

DADOS_BRASIL = {
    "fonte": "Boletim Oficial ANP & Relatório Petrobras (Dados Consolidados)",
    "producao_diaria": {
        "pre_sal_mbpd": 2.24,
        "pos_sal_mbpd": 0.54,
        "gas_natural_mm3d": 108.2
    },
    "balanca_comercial": {
        "labels": ["2020", "2021", "2022", "2023", "2024", "2025"],
        "exportacao_bruto_mbpd": [1.38, 1.32, 1.35, 1.61, 1.74, 1.85],
        "importacao_derivados_mbpd": [0.42, 0.51, 0.55, 0.53, 0.49, 0.46]
    },
    "precos_medios_distribuidoras": {
        "gasolina_a": "R$ 3,02 / litro (Refinaria)",
        "diesel_s10": "R$ 3,48 / litro (Refinaria)",
        "glp_13kg": "R$ 36,90 / botijão (Refinaria)"
    },
    "metas_ambientais_petrobras": [
        {"indicador": "Redução de emissões operacionais (até 2030)", "valor": "30%"},
        {"indicador": "Investimento em baixo carbono (Plano Estratégico)", "valor": "US$ 11,5 bi"},
        {"indicador": "Intensidade de carbono no Pré-Sal (kg CO2e/boe)", "valor": "10,2 kg (Média global: 17 kg)"}
    ]
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/dados-brasil")
def api_dados_brasil():
    return jsonify(DADOS_BRASIL)


if __name__ == "__main__":
    app.run(debug=True, port=5000)