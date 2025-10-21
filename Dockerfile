FROM python:3.11-slim-bookworm

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y build-essential \
    vim

COPY . .

RUN pip install --no-cache-dir -r deps.txt

CMD ["bash"]