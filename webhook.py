from flask import Flask, request


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_data = request.get_json()

    if webhook_data:
        with open('webhook_data.json', 'w') as f:
            json.dump(webhook_data, f, indent=4)
        return 'Webhook received and saved', 200

    return 'No data', 400





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)