# Use a base image
FROM python:3.9.12

# Set the working directory in the container
WORKDIR /home

# Copy the project files to the working directory
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose a port (if needed)
EXPOSE 8000

# Define the command to run when the container starts
CMD ["streamlit", "run", "streamlit_code.py"] && ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
