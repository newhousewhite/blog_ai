from flask import Flask, request, jsonify
from main import BlogWriter


blog = BlogWriter()


app = Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>Hello world</h1>"


@app.route('/title', methods=['POST'])
def title():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Ensure the 'text' key exists in the data
        if 'text' not in data:
            # 400
            return jsonify({"error": "Missing 'text' field"})

        # Convert the string to lowercase
        out_text = blog.run(data['text'], data['type'])

        # Return the lowercase string as JSON
        return jsonify({"llm_output": out_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
