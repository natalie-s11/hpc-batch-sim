FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ ./src
COPY run.sh ./

# Make run.sh executable
RUN chmod +x run.sh

# Expose port for API
EXPOSE 8080

# Default command
CMD ["bash", "run.sh"]
