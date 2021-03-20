# Pull official base image
FROM continuumio/miniconda3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY environment.yml requirements.txt /
RUN conda env create -f /environment.yml

# Make RUN commands use the new environment
RUN echo "conda activate ml-api-env" >> ~/.bashrc
ENV PATH /opt/conda/envs/ml-api-env/bin:$PATH

# Activate the environment, and make sure it's activated
RUN echo "Make sure flask is installed:"
RUN python -c "import pandas"

# The code to run when container is started
COPY . /app
WORKDIR /app

ENTRYPOINT [ "./gunicorn.sh" ]