# SIM Card System

Hosted at - https://digiitplus.pythonanywhere.com/

## Stack - 
Flask,
MySQL,
Postman (for testing API endpoint),
HTML,
CSS,
JS,

## Functionality of Routes -
/ - to serve the index.html<br>
/add-sim - to add sim card details<br>
/activate - to activate sim card<br>
/deactivate - to deactivate sim card<br>
/sim-details/<sim-number> - to see sim card details

## Postman Curls to Test APIs

### Add Sim
curl -X POST https://digiitplus.pythonanywhere.com/add-sim \
-H "Content-Type: application/json" \
-d '{"sim_number": "1234567890", "phone_number": "5551234567"}'

### Activate Sim
curl -X POST https://digiitplus.pythonanywhere.com/activate \
-H "Content-Type: application/json" \
-d '{"sim_number": "1234567890"}'

### Deactivate Sim
curl -X POST https://digiitplus.pythonanywhere.com/deactivate \
-H "Content-Type: application/json" \
-d '{"sim_number": "1234567890"}'

### Sim Details
curl -X GET https://digiitplus.pythonanywhere.com/sim-details/1234567890

## To Run the Code Locally

### To Setup the Database
Open MySQL console and create a database called sim_cards with the schema given in the repository.

### To Run The App
1. Clone the repository
2. Change directory to the cloned repository
3. Install requirements using "pip install -r requirements.txt"
4. Run Flask app using - "flask --app flask_app run"
5. The application will run on port 5000 by default.
