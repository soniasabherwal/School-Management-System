
# Step 1: Use a lightweight Python base image
FROM python:3.9-slim

# Step 2: Set environment variables to ensure Python behaves properly
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents creation of .pyc files
ENV PYTHONUNBUFFERED 1        # Ensures logs are streamed directly

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY . /app/

# Step 6: Expose the port your Flask app runs on
EXPOSE 5000

# Step 7: Command to run the Flask application
CMD ["python", "app.py"]
