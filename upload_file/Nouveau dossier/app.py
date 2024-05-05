from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_and_execute_script():
    if 'file' not in request.files:
        return 'Aucun fichier sélectionné'

    file = request.files['file']
    if file.filename == '':
        return 'Aucun fichier sélectionné'

    # Sauvegardez le fichier temporairement
    file_path = 'uploaded_script.py'
    file.save(file_path)

    # Exécutez le script Python
    try:
        exec(open(file_path).read())
        return 'Script exécuté avec succès'
    except Exception as e:
        return f'Erreur lors de l\'exécution du script : {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
