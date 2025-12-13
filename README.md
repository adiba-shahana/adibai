# Centralized Portfolio Web Application

A modern, high-conversion portfolio for an AI Strategist & Engineer, built with Next.js and FastAPI.

## Project Structure

- `frontend/`: Next.js 14 application (TypeScript, Tailwind CSS)
- `backend/`: FastAPI application (Python)

## Local Development

1.  **Backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    Runs on `http://localhost:8000`.

2.  **Frontend**
    ```bash
    cd frontend
    npm install
    npm run dev
# Centralized Portfolio Web Application

A modern, high-conversion portfolio for an AI Strategist & Engineer, built with Next.js and FastAPI.

## Project Structure

- `frontend/`: Next.js 14 application (TypeScript, Tailwind CSS)
- `backend/`: FastAPI application (Python)

## Local Development

1.  **Backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    Runs on `http://localhost:8000`.

2.  **Frontend**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
    Runs on `http://localhost:3000`.

## Deployment

### Backend (Docker)
1. Build the image:
   ```bash
   docker build -t portfolio-backend .
   ```
2. Run the container (ensure you pass environment variables):
   ```bash
   docker run -p 8000:8000 --env-file .env portfolio-backend
   ```

### Email Configuration
To enable email notifications for contact form submissions:
1. Copy `.env_template` to `.env`.
2. Generate a Google App Password (if using Gmail).
3. Fill in the `SENDER_EMAIL`, `SENDER_PASSWORD`, and `RECEIVER_EMAIL` in `.env`.

### Frontend (Next.js)
1. Build the project:
   ```bash
   npm run build
   ```
2. Start the production server:
   ```bash
   npm start
   ```

## Azure Functions / Cloud Run
- The backend is stateless and ready for serverless deployment.
- Ensure environment variables are set in your cloud provider's dashboard.
- Update the frontend API URL to point to your deployed backend URL.

## Features
- **Project Showcase**: Dynamic project cards with detailed case studies.
- **Contact Form**: Integrated with Python backend for handling submissions.
- **Responsive Design**: Optimized for all devices with a dark-tech aesthetic.
