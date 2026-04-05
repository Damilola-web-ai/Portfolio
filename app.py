from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app) # Opens up the server to accept requests from your HTML file

# --- YOUR GMAIL CREDENTIALS ---
# Important: You must use a "Google App Password", not your normal login password!
MY_EMAIL = "damiola09054@gmail.com" 
MY_APP_PASSWORD = "jjph qbxk wxdv utzg"

@app.route('/')
def home():
    return "My Python Backend is running perfectly! 🚀"

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    name = data.get('name')
    sender_email = data.get('email')
    user_message = data.get('message')

    # Format the email content
    email_body = f"New message from your Portfolio!\n\nName: {name}\nEmail: {sender_email}\n\nMessage:\n{user_message}"
    
    msg = MIMEText(email_body)
    msg['Subject'] = f"Portfolio Lead: {name}"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL # Sending it to yourself

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() # Secure the connection
            server.login(MY_EMAIL, MY_APP_PASSWORD)
            server.send_message(msg)
            
        return jsonify({"success": True, "message": "Email sent successfully!"}), 200
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": "Failed to send email."}), 500

if __name__ == '__main__':
    app.run(debug=True)