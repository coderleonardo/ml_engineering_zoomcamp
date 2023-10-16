FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install "pipenv>2021.11.15,<2023.8.19"

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["bank_credit_scoring.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "bank_credit_scoring:app"]