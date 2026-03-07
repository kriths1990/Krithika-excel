# Use lightweight python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
#CMD ["python", "app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]