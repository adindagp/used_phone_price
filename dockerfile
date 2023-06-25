# Use a base image
FROM python:3.9.12

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY requirements.txt /app
COPY streamlit_code.py /app
COPY api.py /app
COPY DecisionTreeModel.pkl /app
COPY phone_final_filtered.csv /app

# Install project dependencies
RUN pip install -r requirements.txt

# Expose a port (if needed)
EXPOSE 8000
EXPOSE 8501

# Define the command to run when the container starts
CMD streamlit run streamlit_code.py & uvicorn api:app --host 0.0.0.0 --port 8000

