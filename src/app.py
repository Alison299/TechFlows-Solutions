from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'chaveultrasecreta'

PEDIDOS_MOCK = {
    "12345": "Em processamento",
    "67890": "Enviado",
    "ABCDE": "Entregue",
    "99999": "Aguardando pagamento"
}

@app.route('/', methods=['GET', 'POST'])
def rastreio():
    if request.method == 'POST':
        pedido_id = request.form.get('pedido_id')

        if pedido_id in PEDIDOS_MOCK:
            status = PEDIDOS_MOCK[pedido_id]
            mensagem = f"Status do Pedido {pedido_id}: {status}"
            flash(mensagem, 'success')
        else:
            mensagem = f"Pedido {pedido_id} nao encontrado."
            flash(mensagem, 'error')
        
        return redirect(url_for('rastreio'))

    return render_template('rastreio.html')

if __name__ == '__main__':
    app.run(debug=True)