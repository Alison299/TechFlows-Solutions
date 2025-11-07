from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'chaveultrasecreta'

PEDIDOS_MOCK = {
    "12345": {"status": "Em processamento", "nota_fiscal": "NF-001"},
    "67890": {"status": "Enviado",           "nota_fiscal": "NF-002"},
    "ABCDE": {"status": "Entregue",         "nota_fiscal": "NF-003"},
    "99999": {"status": "Aguardando pagamento", "nota_fiscal": "NF-004"}
}

def buscar_por_nota_fiscal(nf):
    for pedido_id, dados in PEDIDOS_MOCK.items():
        if dados["nota_fiscal"] == nf:
            return pedido_id, dados
    return None, None

@app.route('/', methods=['GET', 'POST'])
def rastreio():
    if request.method == 'POST':
        pedido_id_form = request.form.get('pedido_id')
        nota_fiscal_form = request.form.get('nota_fiscal')
        
        pedido_encontrado = None
        id_encontrado = None

        if pedido_id_form:
            if pedido_id_form in PEDIDOS_MOCK:
                id_encontrado = pedido_id_form
                pedido_encontrado = PEDIDOS_MOCK[pedido_id_form]

        elif nota_fiscal_form:
             id_encontrado, pedido_encontrado = buscar_por_nota_fiscal(nota_fiscal_form)

        if pedido_encontrado:
            mensagem = f"Status do Pedido {id_encontrado}: {pedido_encontrado['status']}"
            flash(mensagem, 'success')
        else:
            mensagem = "Pedido nao encontrado (ID ou Nota Fiscal invalidos)."
            flash(mensagem, 'error')
        
        return redirect(url_for('rastreio'))

    return render_template('rastreio.html')

if __name__ == '__main__':
    app.run(debug=True)