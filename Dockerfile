# Use the official Python image
FROM python:3.9-slim
# Set working directory
WORKDIR /app
# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# Copy the app and the HTML file
COPY app.py /app/
COPY index.html /app/
#this is for nginx##COPY ondc-site-verification.html /app/new/
# Expose port 8080 for Cloud Run
EXPOSE 8080
# Run the app
CMD ["python", "app.py"]
