ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

COPY --chown=appuser:appuser requirements.txt .
RUN python -m pip install -r requirements.txt
USER appuser
COPY --chown=appuser:appuser . .

EXPOSE 5000

CMD python app.py
