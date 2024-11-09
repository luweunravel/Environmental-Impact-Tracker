document.getElementById('carbonForm').addEventListener('submit', async function(event) {
    event.preventDefault();
  
    const activity = document.getElementById('activity').value;
    const amount = parseInt(document.getElementById('amount').value);
  
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ activity, amount }),
      });
  
      if (!response.ok) {
        throw new Error('Failed to calculate the carbon footprint.');
      }
  
      const data = await response.json();
  
      // Display the results
      document.getElementById('result').classList.remove('hidden');
      document.getElementById('result-activity').textContent = `Activity: ${data.activity}`;
      document.getElementById('result-amount').textContent = `Amount: ${data.amount}`;
      document.getElementById('result-footprint').textContent = `Footprint: ${data.footprint} kg CO₂`;
      document.getElementById('result-recommendation').textContent = `Recommendation: ${data.recommendation}`;
    } catch (error) {
      alert(error.message);
    }
  });
  