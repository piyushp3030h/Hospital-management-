FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN cd PatientPro && python manage.py collectstatic --noinput

# Start the server (migrate, create superuser, then run gunicorn)
CMD cd PatientPro && python manage.py migrate --noinput && python manage.py create_superuser_auto && gunicorn PatientPro.wsgi --bind 0.0.0.0:$PORT
