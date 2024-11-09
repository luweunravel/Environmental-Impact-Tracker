from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to allow cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes to allow requests from frontend

# Sample data for demonstration; replace with actual calculation logic or model as needed
activity_footprint_factors = {
    "car": 0.21,      # Example factor: car emits 0.21 kg CO2 per km
    "flight": 0.25,   # Example factor: flight emits 0.25 kg CO2 per km
    "train": 0.1      # Example factor: train emits 0.1 kg CO2 per km
}

@app.route('/api/v1/calculate', methods=['POST'])
def calculate_footprint():
    try:
        # Get data from the request
        data = request.get_json()
        activity = data.get("activity")
        amount = data.get("amount")

        # Check if data is provided
        if not activity or amount is None:
            return jsonify({"error": "Please provide both activity and amount."}), 400

        # Calculate the carbon footprint using predefined factors
        factor = activity_footprint_factors.get(activity.lower())
        if factor is None:
            return jsonify({"error": f"Activity '{activity}' is not recognized."}), 400

        footprint = factor * amount

        # Generate a recommendation based on footprint
        recommendation = (
            "Consider reducing your usage of this activity." if footprint > 10 else
            "Your carbon footprint for this activity is relatively low."
        )

        # Return response as JSON
        return jsonify({
            "activity": activity,
            "amount": amount,
            "footprint": round(footprint, 2),
            "recommendation": recommendation
        })

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
