from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ton_secret_key_à_remplacer'  # indispensable pour utiliser flash

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/produits')
def produits():
    return render_template('produits.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Ici tu peux faire du traitement (envoi mail, stockage, etc)
        flash("Merci pour votre message, nous vous répondrons rapidement !", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

if __name__ == '__main__':
    app.run(debug=True)
