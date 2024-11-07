# Build the python server application
FROM python:3.9.20-bullseye AS server

# Expose port 5000
EXPOSE 5000

# Set working directory
WORKDIR /usr/src/app

# Copy the required files 
COPY . .

# Install modules
RUN pip install --no-cache-dir -r requirements.txt

# Run the server
CMD [ "python", "-m","flask","run", "--host=0.0.0.0"]
