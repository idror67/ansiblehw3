from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        # בדוק אם הכותרת מתאימה
        if request.content_type != 'application/json':
            return 'Invalid Content-Type. Expected application/json', 400
        
        try:
            webhook_data = request.get_json()
        except Exception as e:
            return f'Failed to parse JSON: {str(e)}', 400
        
        if webhook_data:
            with open('webhook_data.json', 'w') as f:
                json.dump(webhook_data, f, indent=4)
            return 'Webhook received and saved', 200
        
        return 'No data', 400

    return 'Use POST to send data', 405  # החזר שגיאה אם לא מדובר בבקשת POST

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
