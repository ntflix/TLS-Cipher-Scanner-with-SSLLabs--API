FROM python:3.12-slim

# Create an application directory
WORKDIR /app

# Copy all in ./ to the container's workdir
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run our script
CMD ["python", "main.py"]