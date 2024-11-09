from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

activity_footprint_factors = {
    "car": 0.21,      
    "flight": 0.25,   
    "train": 0.1      
}

@app.route('/api/v1/calculate', methods=['POST'])
def calculate_footprint():
    try:
        data = request.get_json()
        activity = data.get("activity")
        amount = data.get("amount")

        if not activity or amount is None:
            return jsonify({"error": "Please provide both activity and amount."}), 400

        factor = activity_footprint_factors.get(activity.lower())
        if factor is None:
            return jsonify({"error": f"Activity '{activity}' is not recognized."}), 400

        footprint = factor * amount

        recommendation = (
            "Consider reducing your usage of this activity." if footprint > 10 else
            "Your carbon footprint for this activity is relatively low."
        )

        return jsonify({
            "activity": activity,
            "amount": amount,
            "footprint": round(footprint, 2),
            "recommendation": recommendation
        })
        
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
