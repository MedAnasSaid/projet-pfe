from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/run_test', methods=['POST'])
def run_test():
    # Récupérer le code envoyé depuis la requête POST
    code = request.json.get('code')

    # Ici, vous pouvez exécuter le code reçu, par exemple :
    try:
        # Exécutez le code sans afficher le résultat
        exec(code, {}, {})
        # Pour l'exemple, nous renvoyons simplement un message de succès
        return jsonify({'message': 'Test exécuté avec succès !'}), 200
    except Exception as e:
        # En cas d'erreur, renvoyer un message d'erreur
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    # Page d'accueil qui renvoie le contenu HTML
    return render_template('index.html')

@app.route('/extract_generated_code', methods=['POST'])
def extract_generated_code():
    if request.method == 'POST':
        html_content = request.form['html_content']
        soup = BeautifulSoup(html_content, 'html.parser')
        generated_code_element = soup.find(id='generatedCode')
        if generated_code_element:
            generated_code = generated_code_element.get_text()
            # Utilisez generated_code comme vous le souhaitez ici
            print("Generated code:", generated_code)
            return "Generated code extracted successfully!"
        else:
            return "Element with ID 'generatedCode' not found in HTML content."
    else:
        return "Only POST requests are allowed for this endpoint."

if __name__ == '__main__':
    app.run(debug=True)
