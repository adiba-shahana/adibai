from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = FastAPI(title="Adiba Khan Portfolio API")

# Configure CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: str
    company: str | None = None
    role: str | None = None
    subject: str
    project_type: str
    description: str
    budget: str
    timeline: str

def send_email_notification(form: ContactForm):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    if not all([sender_email, sender_password, receiver_email]):
        print("Email configuration missing. Skipping email notification.")
        return

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"NEW AI FREELANCE LEAD: {form.subject}"

    body = f"""
    New Lead Details:
    -----------------
    Name: {form.name}
    Email: {form.email}
    Company: {form.company or 'N/A'}
    Role: {form.role or 'N/A'}
    
    Project Info:
    -------------
    Subject: {form.subject}
    Type: {form.project_type}
    Budget: {form.budget}
    Timeline: {form.timeline}
    
    Description:
    ------------
    {form.description}
    """
    
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Email notification sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Portfolio Backend is running"}

@app.post("/api/contact")
def submit_contact(form: ContactForm):
    try:
        # Log to console
        print(f"[{datetime.now()}] New Lead:")
        print(f"Name: {form.name}")
        print(f"Email: {form.email}")
        print(f"Company: {form.company}")
        print(f"Role: {form.role}")
        print(f"Subject: {form.subject}")
        print(f"Type: {form.project_type}")
        print(f"Budget: {form.budget}")
        print(f"Timeline: {form.timeline}")
        print(f"Description: {form.description}")
        
        # Append to log file
        with open("contact_submissions.log", "a") as f:
            f.write(f"[{datetime.now()}] {form.name} ({form.email}) - {form.subject} | Budget: {form.budget}\n")
            
        # Send Email Notification
        send_email_notification(form)
            
        return {"status": "success", "message": "Lead received successfully"}
    except Exception as e:
        print(f"Error processing contact form: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
